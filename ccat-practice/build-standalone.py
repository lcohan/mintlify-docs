#!/usr/bin/env python3
"""Genera la versión descargable a partir de index.html.

index.html se publica como artifact: la plataforma le agrega el <!doctype>,
el <head> y el meta viewport. Un archivo suelto no recibe nada de eso, así
que sin encabezado propio el celular lo dibuja a 980px de ancho y se ve
diminuto. Este script arma el documento completo para abrir desde disco.

    python3 build-standalone.py
"""
import pathlib

HERE = pathlib.Path(__file__).parent
SRC = HERE / "index.html"
OUT = HERE / "entrenador-ccat.html"

# En index.html todo lo anterior a este div es contenido de <head>.
BODY_STARTS_AT = '<div id="drain"'

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="Simulador de practica del CCAT: 50 preguntas en 15 minutos, con preguntas nuevas en cada intento.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="CCAT">
<meta name="mobile-web-app-capable" content="yes">
<style>html{-webkit-text-size-adjust:100%}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
"""

def main():
    src = SRC.read_text(encoding="utf-8")
    if BODY_STARTS_AT not in src:
        raise SystemExit("No encuentro donde empieza el cuerpo (%s). Revisar index.html." % BODY_STARTS_AT)
    cut = src.index(BODY_STARTS_AT)
    head, body = src[:cut], src[cut:]
    OUT.write_text(HEAD + head + "</head>\n<body>\n" + body + "</body>\n</html>\n", encoding="utf-8")
    print("%s -> %s (%.0f KB)" % (SRC.name, OUT.name, OUT.stat().st_size / 1024))

if __name__ == "__main__":
    main()
