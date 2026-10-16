#!/bin/sh
# Equivalente POSIX de render.ps1. Uso: MMD_MODULES=/ruta/node_modules ./render.sh [archivo.mmd ...]
D=$(dirname "$0"); : "${MMD_MODULES:?definir MMD_MODULES}"
mkdir -p "$D/pdf" "$D/svg"
for f in ${@:-$D/*.mmd}; do b=$(basename "$f" .mmd)
  "$MMD_MODULES/.bin/mmdc.cmd" -q -i "$f" -o "$D/svg/$b.svg" -c "$D/config.json" && node "$D/svg2pdf.js" "$D/svg/$b.svg" "$D/pdf/$b.pdf" && echo "ok $b"
done
