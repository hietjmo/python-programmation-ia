# Expressiones regular

*Expressiones regular* es un linguage in linguage. Nos usa expressiones regular a identificar partes de sequentias de characteres.

In expression regular cata littera accepta le littera correspondente in sequentia de characteres. Preter isto nos ha characteres special: \"`.^$*+?{}[]\|()`\".

Nos ha listate le significantias de characteres special in tabella \ref{tab:re-special}.

Characteres    Significantia
-------------  -----------------------------------------
`.`            Qualcunque character.
`^`            Initio del texto.
`$`            Fin del texto.
`*`            Zero o plure apparentias.
`+`            Un o plure apparentias.
`?`            Zero o un apparentia.
`{m,n}`        A minime `m`, a maxime `n` apparentias.
`[`...`]`      Un classe de characteres.
`\`            Character a escappar.
`|`            Alternante (operator **or**).
`(`...`)`      Un gruppo.
-------------  -----------------------------------------

: Characteres special de expressiones regular. \label{tab:re-special}


Le expression regular `"e"` accepta le littera `e`. In tabella \ref{tab:re-examples} nos presenta altere exemplos.

--------------------------------------------------------------------
Sequentia      Significantia
-------------  -----------------------------------------------------
`"e"`          Le littera `e`.

`"[eaio]"`     Un de litteras `e`, `a`, `i`, `o`.

`"e*"`         Le littera `e` zero o plure vices.

`"e+"`         Le littera `e` un o plure vices.

`"[eaio]+"`    Iste litteras un o plure vices, per exemplo: 
               `"aeo"`, `"eei"`, `"i"`, `"iiiia"`, `"oaoao"`, ...
--------------------------------------------------------------------

: Exemplos de expressiones regular. \label{tab:re-examples}


