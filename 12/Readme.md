## Árvore sintática

Considere a seguinte gramática:

```Python
grammar1 = [ 
      ("S", "aS" ), #rule 0           
      ("S", ""   ), #rule 1               
]
initial = "S"
```

Considere a árvore sintática da string `"a"`:
```
         S
        / \
       a  S
           \
           ""
```

Representaremos essa árvore da seguinte maneira:
```
tree1 = ["S", "a", ["S", ""]  ]
```

Agora, chegou a sua vez de exercitar:

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

Construa a árvore sintática de 
1. a+a
2. a+a*a
3. a+a*a+a

Código Python

```
# encoding: iso-8859-1
# Todo nao terminal será representado por uma letra maiúscula
# Todo terminal será representado por uma letra minúsculas
# O conjunto de regras é representado por uma lista de pares ordenado


#terminais = [chr(x) for x in range(ord('a'), ord('z')+1)] 

#terminais.append('+')

  

def resultado(tree):
  res = ""  
  for r in tree:
    if type(r) is list:
      res = res + resultado(r)
    else:
      if r in terminais:
        res = res + r
  return res


def check_tree(grammar, tree ):
  print ("checando arvore: " + str(tree))  
  for rule in grammar:
    if rule[0] == tree[0]:
      #print "testando regra" + str(rule)
      zipped = zip(rule[1], tree[1:])
      ok = True
      i = 0     
      for (a,b) in zipped:
        if type(b) is not list:
          if a != b:
            ok = False
        else:
          #print tree[i+1]
          ok = ok and check_tree(grammar, tree[i+1])
        i = i + 1
      if ok :
        return ok    

def parser_tree(grammar, tree, string):
  print ("resultado: " + resultado(tree)) 
  if resultado(tree) == string:
    return check_tree(grammar, tree)
  else:
    print("Arvore invalida")
    return False

grammar1 = [ 
      ("S", "aS" ), #rule 0           
      ("S", ""   ), #rule 1               
]

initial = "S"

#Uma árvore sintática será representada por uma lista da seguinte maneira
#         S
#        / \
#       a  S
#           \
#           ''
#> tree1 = ["S", "a", ["S", "a",["S",""] ]  ]
#> print parser_tree(grammar1, tree1, "aa")
#> true


grammar2 = [ 
      ("E", "E+T"  ), #rule 0           
      ("E",  "T"   ), #rule 1
      ("T",  "T*F" ), #rule 2           
      ("T",  "F"   ), #rule 3               
      ("F",  "(E)" ), #rule 4               
      ("F",  "a"   ), #rule 5               
]

terminais = ["a","+","*"]

# Construa a árvore sintática da a+a

tree1 = [ ]  

print (parser_tree(grammar2,tree1, "a+a"))


# Construa a árvore sintática da a+a

tree2 = [ ]  

print (parser_tree(grammar2,tree2, "a+a*a"))


# Construa a árvore sintática da a+a

tree3 = []  

print (parser_tree(grammar2,tree3, "a+a*a+a"))


```






