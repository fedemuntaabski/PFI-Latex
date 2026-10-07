"""Verifica que la edición de las transcripciones (Anexos C a F) solo cambió
puntuación y mayúsculas iniciales, salvo los restos de transcripción
automática aprobados para borrar.

Uso: python documentacion/scripts/verificar_transcripciones.py [commit_base]

Para cada anexo compara el cuerpo de la transcripción (entorno description,
sin las etiquetas \\item[...] de los interlocutores) en el commit base y en el
árbol de trabajo:
  1. Secuencia de palabras en minúsculas y sin puntuación: solo se admiten
     borrados, y cada bloque borrado debe estar en la lista aprobada.
  2. Mayúsculas: una palabra solo puede cambiar de caja si queda al inicio de
     una oración (precedida por . ? ! : ¿ o al inicio del turno).
"""
import difflib
import re
import subprocess
import sys

BASE = sys.argv[1] if len(sys.argv) > 1 else '87af6b0'

ANEXOS = {
    'C': 'chapters/appendix/interview_1_pablo.tex',
    'D': 'chapters/appendix/interview_2_jacubovich.tex',
    'E': 'chapters/appendix/interview_3_guillermo.tex',
    'F': 'chapters/appendix/interview_4_pena.tex',
}

# Restos de transcripción automática aprobados para borrar (en minúsculas).
BORRADOS_APROBADOS = {
    'C': ['perfect', 'yeah', 'it', 'okay here you', 'okay thank you', 'the win'],
    'D': [],
    'E': [],
    'F': ['yeah', 'dizzy', 'perfect', 'belly', 'that', 'but', 'thank you',
          'think so yeah', 'say it la milandia'],
}

WORD = re.compile(r'\w+')


def cuerpo(texto):
    """Texto de los turnos, sin etiquetas de interlocutor ni comandos LaTeX."""
    m = re.search(r'\\begin\{description\}(?:\[[^\]]*\])?(.*)\\end\{description\}',
                  texto, re.S)
    t = m.group(1)
    t = re.sub(r'\\item\[[^\]]*\]', ' \n¶ ', t)   # ¶ marca inicio de turno
    t = re.sub(r'\\[a-zA-Z]+', ' ', t)
    return t


def tokens(t):
    """Lista de (palabra, ¿inicio de oración?)."""
    out = []
    inicio = True
    for m in re.finditer(r'\w+|[.?!:¿¶]', t):
        s = m.group(0)
        if s in '.?!:¿¶':
            inicio = True
        else:
            out.append((s, inicio))
            inicio = False
    return out


def leer_base(ruta):
    return subprocess.run(['git', 'show', f'{BASE}:{ruta}'], capture_output=True,
                          check=True).stdout.decode('utf8')


ok_global = True
for anexo, ruta in ANEXOS.items():
    antes = tokens(cuerpo(leer_base(ruta)))
    despues = tokens(cuerpo(open(ruta, encoding='utf8').read()))
    a = [w.lower() for w, _ in antes]
    d = [w.lower() for w, _ in despues]

    borrados, problemas = [], []
    sm = difflib.SequenceMatcher(None, a, d, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for (wa, _), (wd, ini) in zip(antes[i1:i2], despues[j1:j2]):
                if wa != wd and not ini:
                    problemas.append(f'cambio de caja fuera de inicio de oración: {wa} -> {wd}')
        elif op == 'delete':
            borrados.append(' '.join(a[i1:i2]))
        else:
            problemas.append(f'{op}: "{" ".join(a[i1:i2])}" -> "{" ".join(d[j1:j2])}"')

    aprobados = BORRADOS_APROBADOS[anexo]
    no_aprobados = [b for b in borrados if b not in aprobados]
    problemas += [f'borrado no aprobado: "{b}"' for b in no_aprobados]

    print(f'Anexo {anexo} ({ruta})')
    print(f'  palabras antes: {len(a)}  después: {len(d)}  diferencia: {len(a) - len(d)}')
    print(f'  bloques borrados ({len(borrados)}): {borrados}')
    if problemas:
        ok_global = False
        print('  RESULTADO: DIFERENCIAS NO PERMITIDAS')
        for p in problemas:
            print(f'    - {p}')
    else:
        print('  RESULTADO: IDÉNTICO salvo restos aprobados')
    print()

sys.exit(0 if ok_global else 1)
