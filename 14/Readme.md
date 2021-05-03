# Analisador Descendente Recursivo 

O processo de parsing consiste em analisar uma sequência de tokens para determinar se sua estrutura gramatical está de acordo com uma determinada gramática.


Considere a gramática cujos os símbolos são `(` e `)` e a linguagem descrita por ela seja dos parênteses balanceados. 

```Python
1. B -> ( RB 
2. B -> epsilon
3. R -> )    
4. R -> ( RR 
```

Na gramática acima, podemos construir uma derivação mais à esquerda para string `(())()` usando uma analisador descendente recursivo do tipo `LL(1)`. Neste tipo de analisador, cada não terminal é representado por um subprograma. Em cada subprograma, conseguimos escolher a regra apropriada verificando apenas o primeiro caractere da string atual.

```Python
# Analisador Descendente Recursivo
# B - > ( RB
# B -> epsilon
# R -> )
# R -> ( RR


def B():
  global string  
  print("Chamando B")
  if string[0] == '(':
    # Usando a regra  B - > ( RB   
    string = string[1:] # avanca caractere
    R()
    B()
  elif string[0] == '$':
    # B -> epsilon
    string = string[1:] # avanca caractere
  else:
    print("Erro sintático nao terminal B\n")    
  print("Saindo B")

def R():
  global string
  print("Chamando R")    
  if string[0] == ')':
    # Usando a regra  R - > (   
    string = string[1:] # avanca caractere
  elif string[0] == '(':
    # R -> ( RR
    string = string[1:] # avanca caractere
    R()
    R()  
  else:
    print("Erro sintático nao terminal R\n")  
  print("Saindo R")


string = "(())()$"
B()

```

No exemplo, acima temos a seguinte saída:

```Python
Chamando B
Chamando R
Chamando R
Saindo R
Chamando R
Saindo R
Saindo R
Chamando B
Chamando R
Saindo R
Chamando B
Saindo B
Saindo B
Saindo B
```

No caso de uma string que não está de acordo com as regras gramaticais um erro sintático é gerado.

Por exemplo, se analisamos a seguinte string `(())($`, teremos o seguinte relatório:

```
Chamando B
Chamando R
Chamando R
Saindo R
Chamando R
Saindo R
Saindo R
Chamando B
Chamando R
Erro sintático nao terminal R

Saindo R
Chamando B
Saindo B
Saindo B
Saindo B

```

Quando analisamos a seguinte string `(()))$`. O analisador acima, dará qual informação?


a. Nenhum erro sintático

b. Erro sintático nao terminal B

c. Erro sintático nao terminal R



