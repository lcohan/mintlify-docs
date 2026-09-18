# Entrenador CCAT

Simulador de práctica para el **Criteria Cognitive Aptitude Test** (50 preguntas en 15 minutos).
Es un único archivo HTML sin dependencias: se abre con doble clic, funciona sin internet y no
manda nada a ningún servidor.

## Cómo usarlo

- **Desde la compu**: abrí `index.html` en cualquier navegador.
- **Desde el celular**: copiá el archivo al teléfono (o abrí el link publicado) y agregalo a la
  pantalla de inicio para tenerlo a mano.

## Qué incluye

| Modo | Qué hace |
| --- | --- |
| Examen completo | 50 preguntas, 15:00 de reloj, sin volver atrás (igual que el examen real) |
| Simulacro corto | 15 preguntas en 4:30, mismo ritmo, para entrenar todos los días |
| Entrenamiento | Categoría, cantidad y reloj por pregunta a elección, con explicación en cada respuesta |

Las tres áreas del CCAT están cubiertas y se reparten como en el examen real:

- **Verbal**: analogías, sinónimos, antónimos, intruso y completar oraciones.
- **Numérico y lógico**: series, porcentajes, promedios, razones, trabajo, velocidad, interés,
  probabilidad, edades, conjuntos, álgebra y deducción (verdadero / falso / incierto).
- **Espacial**: series de rotación, figura intrusa, analogías de figuras y series de conteo.

Las preguntas se **generan en el momento**, así que no se repiten entre intentos. Cada respuesta
trae su explicación, el resultado muestra el desglose por categoría con un percentil estimado, y
el botón *Entrenar mis errores* arma una tanda nueva con los tipos de pregunta que fallaste.

El historial de intentos se guarda en el navegador (`localStorage`), sólo en ese dispositivo.

## Idioma

Toda la aplicación —interfaz y preguntas— funciona en español o en inglés. El CCAT se suele rendir
en inglés, así que conviene practicar en el idioma en que se va a dar el examen.

## Nota

Práctica no oficial, sin relación con Criteria Corp. El percentil es una estimación orientativa a
partir de baremos publicados.
