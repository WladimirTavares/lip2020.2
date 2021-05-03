## Derivação mais à esquerda

Na nossa modelagem da gramática livre de contexto em Python, fizemos as seguintes conveções:

* Os símbolos não-terminais serão representados por letras maiscúlas. 
* Os símbolos terminais por letras minúsculas. 
* Cada regra será representada por um par ordenado. O primeiro elemento do par será o lado esquerdo da regra e o segundo será o lado direito da regra.

A seguir, um exemplo de uma gramática:

```Python
grammar1 = [ 
      ("S", "aS" ), #rule 0           
      ("S", ""   ), #rule 1               
]
initial = "S"
```

Um derivação será uma lista de índices das regras da gramática. Por exemplo, `[0,0,0,1]` é uma derivação do string `"aaa"`.

Na saída, o programa escreverá a derivação mais à esquerda para gerar a string `"aaa"`.


```
S
=>aS
=>aaS
=>aaaS
=>aaa
derivacao completa

```

Considere a seguinte gramática:

```
grammar2 = [ 
      ("E", "E+T"  ), #rule 0           
      ("E",  "T"   ), #rule 1
      ("T",  "T*F" ), #rule 2           
      ("T",  "F"   ), #rule 3               
      ("F",  "(E)" ), #rule 4               
      ("F",  "a"   ), #rule 5               
]
```

Construa a derivação para as seguintes strings:

1. a+a+a
2. a+a*a


Código Python
```
# encoding: iso-8859-1
# Todo nao terminal será representado por uma letra maiúscula
# Todo terminal será representado por uma letra minúsculas
# O conjunto de regras é representado por uma lista de pares ordenado

#Considere a seguinte gramática:
grammar1 = [ 
      ("S", "aS" ), #rule 0           
      ("S", ""   ), #rule 1               
]
initial = "S"

#
#[0,0,0,1] é uma derivacao para "aaa"
#S => aS => aaS => aaaS => aaa    
#  0     0      0       1
# X = [0,0,0,1]
#> check_derivation(grammar, "S", [0,0,0,1], "aaa")
#> S
#=>aS
#=>aaS
#=>aaaS
#=>aaa
#derivacao completa


def check_derivation(grammar, sentencial_form, derivation, string):
  print sentencial_form
  
  for i in range(len(derivation)):
    rule_index = derivation[i]    
    found = False    
    for pos in range( len(sentencial_form) ):      
      symbol = sentencial_form[pos]
      if symbol == grammar[rule_index][0]:
        sentencial_form = sentencial_form[0:pos] + grammar[rule_index][1] + sentencial_form[pos+1:]
        found = True
        break
    
    if not found:
      print "derivacao mal formada"
      return 

    print "=>" + sentencial_form        
  
  if sentencial_form == string:
    print "derivacao completa"
  else:
    print "derivacao imcompleta" 




 
#Considere a seguinte gramatica


grammar2 = [ 
      ("E", "E+T"  ), #rule 0           
      ("E",  "T"   ), #rule 1
      ("T",  "T*F" ), #rule 2           
      ("T",  "F"   ), #rule 3               
      ("F",  "(E)" ), #rule 4               
      ("F",  "a"   ), #rule 5               
]

# Construa uma derivacao para a + a + a
# Coloque aqui sua derivacao

X = []
check_derivation(grammar2, "E", X, "a+a+a")

X = []
check_derivation(grammar2, "E", X, "a+a*a")
```

