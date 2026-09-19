# Entrenador CCAT

Simulador de práctica para el **Criteria Cognitive Aptitude Test** (50 preguntas en 15 minutos).
Es un único archivo HTML sin dependencias: se abre con doble clic, funciona sin internet y no
manda nada a ningún servidor.

## Qué archivo usar

| Archivo | Para qué |
| --- | --- |
| `entrenador-ccat.html` | **El que se descarga y se abre.** Documento completo, con su propio `<head>`. |
| `index.html` | Sólo para publicar como artifact: la plataforma le agrega el `<head>` y el meta viewport. |
| `build-standalone.py` | Genera el primero a partir del segundo. Correlo después de tocar `index.html`. |

Sin el `<meta name="viewport">`, un celular dibuja la página a 980 px de ancho y se ve diminuta.
Por eso `index.html` suelto **no** sirve para abrir desde el teléfono: usá `entrenador-ccat.html`.

## Cómo usarlo

- **Desde la compu**: abrí `entrenador-ccat.html` en cualquier navegador.
- **Desde el celular**: copiá `entrenador-ccat.html` al teléfono (o abrí el link publicado) y
  agregalo a la pantalla de inicio para tenerlo a mano. La interfaz está probada en pantallas de 320, 360 y
  390 px: las figuras entran enteras, sin scroll lateral, y los controles llegan a 42 px de alto.

## Qué incluye

| Modo | Qué hace |
| --- | --- |
| Examen completo | 50 preguntas, 15:00 de reloj, sin volver atrás (igual que el examen real) |
| Simulacro corto | 15 preguntas en 4:30, mismo ritmo, para entrenar todos los días |
| Entrenamiento | Categoría, cantidad y reloj por pregunta a elección, con explicación en cada respuesta |

Las tres áreas del CCAT están cubiertas y se reparten como en el examen real. Son 59 generadores,
con los formatos que aparecen en los exámenes de práctica que circulan:

- **Verbal** (8): analogías de completar y analogías con pares de opciones (`MÉDICO es a HOSPITAL
  como…`), sinónimos, antónimos, intruso, completar con uno o dos blancos, y comparar dos columnas
  para contar cuántas filas son idénticas.
- **Numérico y lógico** (46): series numéricas y de letras (incluidos bloques tipo `AOHV, BPIW…`),
  porcentajes directos, inversos y encadenados, promedios, razones, trabajo y producción,
  velocidad y hora de llegada, interés, probabilidad simple y de dos eventos, combinatoria,
  edades, conjuntos, álgebra, lectura de tablas, acertijos de lógica con pistas y deducción
  (verdadero / falso / incierto).
- **Espacial** (5): series de rotación, figura intrusa, analogías de figuras y series de conteo.

Las preguntas se **generan en el momento**, así que no se repiten entre intentos. Cada respuesta
trae su explicación, el resultado muestra el desglose por categoría con un percentil estimado, y
el botón *Entrenar mis errores* arma una tanda nueva con los tipos de pregunta que fallaste.

El historial de intentos se guarda en el navegador (`localStorage`), sólo en ese dispositivo.

## De dónde salen las preguntas

Los moldes se modelaron sobre exámenes de práctica reales que circulan entre quienes ya rindieron
el CCAT, pero ninguna pregunta está copiada: cada generador arma el enunciado, los números y las
opciones en el momento. Eso evita dos problemas de los sets que circulan — son finitos y varios
traen la respuesta mal (por ejemplo, dos trabajadores de 3,5 h y 4 h en 56 horas hacen 30
reparaciones, no 34). Acá cada respuesta se calcula, no se transcribe.

Todos los generadores se verifican con una corrida de 40.000 preguntas en los dos idiomas, que
controla que cada pregunta tenga respuesta válida, opciones únicas y sin valores imposibles.

Las figuras espaciales se verifican aparte: se rasterizan los 16 estados de cada una (8 giros × con
y sin espejado) al tamaño real de un celular y se mide cuánto cambia el dibujo entre cada par. El
mínimo quedó en 11,7%, suficiente para distinguirlas de un vistazo en una pantalla chica.

## Idioma

Toda la aplicación —interfaz y preguntas— funciona en español o en inglés. El CCAT se suele rendir
en inglés, así que conviene practicar en el idioma en que se va a dar el examen.

## Nota

Práctica no oficial, sin relación con Criteria Corp. El percentil es una estimación orientativa a
partir de baremos publicados.
