// Genera la carátula exterior (cover/Caratulafinal.pdf) reproduciendo el generador web de la
// Biblioteca UADE:
//   https://biblioteca.uade.edu.ar/custom/web/content/biblioteca/pdf/tif-pfi/generarCaratulas/crearCaratula.html
// Mismo algoritmo que su función generarPDF() para la opción "Facultad de Ingeniería y Ciencias
// Exactas - PROYECTO FINAL DE INGENIERÍA" (plantilla PFI-FAIN.pdf): mismas fuentes, tamaños,
// coordenadas y corte del título en líneas de 40 caracteres.
//
// El título se lee de la macro \UmbralTitulo de main.tex, para que la carátula no se desincronice
// de la portada ni del encabezado. Si cambia el título, volver a ejecutar este script.
//
// Uso:
//   1. Descargar la plantilla:
//      https://biblioteca.uade.edu.ar/custom/web/content/biblioteca/pdf/tif-pfi/generarCaratulas/PFI-FAIN.pdf
//   2. npm install pdf-lib@1.16.0   (misma versión que usa la web; fuera del repo)
//   3. NODE_PATH=<carpeta>/node_modules node cover/generar_caratula.js <PFI-FAIN.pdf> cover/Caratulafinal.pdf

const fs = require('fs');
const path = require('path');
const { PDFDocument, StandardFonts, rgb } = require('pdf-lib');

// Datos del formulario (iguales a los de la carátula anterior)
const autores = [
  { autor: 'Mociulsky Santiago', legajo: '1158033' },
  { autor: 'Muntaabski Federico', legajo: '1158981' },
];
const carrera = 'Ingeniería en Informática';
const tutor = 'Borchert Hugo Alejandro';
const fecha = '2026';

function leerTitulo() {
  const main = fs.readFileSync(path.join(__dirname, '..', 'main.tex'), 'utf8');
  const m = main.match(/^\\newcommand\{\\UmbralTitulo\}\{(.+)\}\s*$/m);
  if (!m) throw new Error('No se encontró \\newcommand{\\UmbralTitulo}{...} en main.tex');
  if (m[1].includes('\\')) throw new Error('El título contiene comandos LaTeX; no se puede pasar tal cual a la carátula');
  return m[1];
}

// Corte del título igual al de la web: líneas de hasta 40 caracteres sin partir palabras
function cortarTitulo(titulo, maxLineLength = 40) {
  const lines = [];
  let currentLine = '';
  for (const word of titulo.split(' ')) {
    if (currentLine.length + word.length <= maxLineLength) {
      if (currentLine.length > 0) currentLine += ' ';
      currentLine += word;
    } else {
      lines.push(currentLine);
      currentLine = word;
    }
  }
  if (currentLine.length > 0) lines.push(currentLine);
  return lines;
}

async function main() {
  const [plantilla, salida] = process.argv.slice(2);
  if (!plantilla || !salida) {
    console.error('Uso: node cover/generar_caratula.js <PFI-FAIN.pdf> <salida.pdf>');
    process.exit(1);
  }

  const titulo = leerTitulo();
  const pdfDoc = await PDFDocument.load(fs.readFileSync(plantilla));
  const firstPage = pdfDoc.getPages()[0];
  const { width } = firstPage.getSize();
  const negro = rgb(0, 0, 0);
  const helvetica = await pdfDoc.embedFont(StandardFonts.Helvetica); // fuente por defecto de drawText
  const helveticaBold = await pdfDoc.embedFont(StandardFonts.HelveticaBold);

  // Título: Helvetica 25 pt desde (80, 680), 25 pt entre líneas
  const x = 80;
  const fontSize = 25;
  const lineHeight = 25;
  let yPosition = 680;
  for (const line of cortarTitulo(titulo)) {
    const ancho = helvetica.widthOfTextAtSize(line, fontSize);
    if (x + ancho > width - 20) {
      throw new Error(`La línea "${line}" desborda la página (${(x + ancho).toFixed(1)} pt de ${width.toFixed(1)} pt)`);
    }
    firstPage.drawText(line, { x, y: yPosition, size: fontSize, font: helvetica, color: negro });
    yPosition -= lineHeight;
  }

  let orden = 500;
  firstPage.drawText('Autor/es: ', { x: 100, y: 500, size: 20, color: negro, font: helveticaBold });
  orden -= 20;
  const authorsText = autores.map((a) => `${a.autor} - LU: ${a.legajo}`).join('\n');
  firstPage.drawText(authorsText, { x: 100, y: orden - 20, size: 18, font: helvetica, color: negro });

  orden -= 40 + 22 * autores.length;
  firstPage.drawText('Carrera:  ', { x: 100, y: orden, size: 20, color: negro, font: helveticaBold });
  orden -= 20;
  firstPage.drawText(carrera, { x: 100, y: orden, size: 18, font: helvetica, color: negro });

  orden -= 40;
  firstPage.drawText('Tutor/es: ', { x: 100, y: orden, size: 20, color: negro, font: helveticaBold });
  orden -= 20;
  firstPage.drawText(tutor, { x: 100, y: orden, size: 18, font: helvetica, color: negro });

  orden -= 40;
  firstPage.drawText('Año: ', { x: 100, y: orden, size: 20, color: negro, font: helveticaBold });
  orden -= 20;
  firstPage.drawText(fecha, { x: 100, y: orden, size: 18, font: helvetica, color: negro });

  fs.writeFileSync(salida, await pdfDoc.save());
  console.log(`Carátula generada en ${salida}:\n  ${cortarTitulo(titulo).join('\n  ')}`);
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
