# Compilador
<h2>Objetivo</h2>
<p>El objetivo de este trabajo es construir un analizador sintáctico descendente predictivo por tabla (parser), junto con un un analizador lexicográfico (lexer) que se implementará en el lenguaje de programación Python, para aceptar el lenguaje de programación PL-0 (lenguaje diseñado para entender los fundamentos de compiladores y teoría de lenguajes de programación).<br>
El software deberá aceptar como entrada una cadena que representa código escrito en el lenguaje
PL-0, y deberá para este código, interpretado como una cadena de caracteres ASCII o UTF-8,
indicar si dicha cadena pertenece al lenguaje generado por su gramática la cual está detallada más adelante en este README.md, y además deberá
indicar la derivación desde el símbolo distinguido para la cadena, en caso de pertenecer.<br>
En el pdf adjuntado ("informe.pdf") se detalla la gramática arreglada, pues la original tiene problemas de recursividad izquierda y factorizacion, los cuales deben ser eliminiados mediante los correspondientes algoritmos detallados en el libro del dragón para poder construir un analizador sintáctico con las características establecidas. También se puede ver la tabla de predicción calculada y tomada como base para la elaboración del parser a la hora de codificar.</p>

<h2>Gramática establecida PL-0</h2>
<img src="https://github.com/user-attachments/assets/9f5e2014-d9bb-40be-8cbe-8e2dd5140234">
