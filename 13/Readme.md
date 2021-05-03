## Ambiguidade

Considere a seguinte gramática:

```Python
grammar1 = [ 
      ("S", "aS" ), #rule 0           
      ("S", "aSbS"   ), #rule 1 
      ("S", ""   ), #rule 2                
]
initial = "S"

```

Apresente duas derivações mais à direita para a string aab.


Utilize o seguinte código Python
```Python
# encoding: iso-8859-1


def check_derivation(grammar, sentencial_form, derivation, string):
  print (sentencial_form)
  
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
      print ("derivacao mal formada")
      return 

    print ("=>" + sentencial_form)        
  
  if sentencial_form == string:
    print ("derivacao completa")
  else:
    print ("derivacao imcompleta") 




 
#Considere a seguinte gramática:
grammar1 = [ 
      ("S", "aS" ), #rule 0           
      ("S", "aSbS"   ), #rule 1 
      ("S", ""   ), #rule 2                
]
initial = "S"

#Apresente duas derivações mais à direita para a string aab


X1 = []
check_derivation(grammar1, "S", X1, "aab")

X2 = []
check_derivation(grammar1, "S", X2, "aab")

print(X1 != X2)

```

O seu programa deve gerar a seguinte saída:

```Python
S
=>aSbS
=>aaSbS
=>aabS
=>aab
derivacao completa
S
=>aS
=>aaSbS
=>aabS
=>aab
derivacao completa
True
```

