// Convierte un SVG de Mermaid a PDF vectorial con el tamaño natural del diagrama.
// Uso: node svg2pdf.js entrada.svg salida.pdf   (requiere puppeteer de @mermaid-js/mermaid-cli)
const fs = require('fs');
const path = require('path');
const puppeteer = require(path.join(process.env.MMD_MODULES, 'puppeteer'));
(async () => {
  const [, , inp, out] = process.argv;
  const svg = fs.readFileSync(inp, 'utf8');
  const vb = svg.match(/viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"/);
  const w = Math.ceil(parseFloat(vb[3])) + 8, h = Math.ceil(parseFloat(vb[4])) + 8;
  const html = '<html><body style="margin:0">' + svg.replace(/width="100%"/, `width="${w}"`).replace(/max-width:[^;]*;/, '') + '</body></html>';
  const browser = await puppeteer.launch({ headless: 'shell', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: w, height: h });
  await page.setContent(html);
  await page.pdf({ path: out, width: w + 'px', height: h + 'px', printBackground: true, pageRanges: '1' });
  await browser.close();
})();
