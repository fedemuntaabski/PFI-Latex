# Renderiza cada .mmd de esta carpeta: mmdc -> SVG (tamaño natural) -> PDF vectorial en pdf/.
# Requisito: npm i @mermaid-js/mermaid-cli en una carpeta fuera del repo; pasar esa carpeta en -Modules.
param([string]$Modules = "$env:LOCALAPPDATA\Temp\mmd\node_modules")
$dir = $PSScriptRoot
$env:MMD_MODULES = $Modules
New-Item -ItemType Directory -Force "$dir\pdf", "$dir\svg" | Out-Null
Get-ChildItem "$dir\*.mmd" | ForEach-Object {
  & "$Modules\.bin\mmdc.cmd" -q -i $_.FullName -o "$dir\svg\$($_.BaseName).svg" -c "$dir\config.json"
  node "$dir\svg2pdf.js" "$dir\svg\$($_.BaseName).svg" "$dir\pdf\$($_.BaseName).pdf"
  Write-Host "ok $($_.BaseName)"
}
