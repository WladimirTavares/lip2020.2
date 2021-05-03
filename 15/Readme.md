# Analisador Descendente Recursivo 

O processo de parsing consiste em analisar uma sequência de tokens para determinar se sua estrutura gramatical está de acordo com uma determinada gramática.


Considere a gramática cujos os símbolos são `(` e `)` e a linguagem descrita por ela seja dos parênteses balanceados. 

```Python
1. B -> ( RB 
2. B -> epsilon
3. R -> )    
4. R -> ( RR 
```

Quando podemos construir a derivação mais à esquerda verificando apenas o primeiro caractere da string a ser gerada, dizemos que a gramática é `LL(1)`. Como vimos anteriormente, a gramática acima tem essa propriedade. Quando a gramática tem essa propriedade, podemos realizar o processo de análise com o auxílio de uma tabela e uma pilha.

|     | (    |  )  | $       |
| --- | ---  | --- | --      | 
| B   | (RB |     | epsilon |
| R   | (RR |  )   |  |
 

Nessa tabela, para cada não-terminal  (B ou R) e não terminal ( `(`, `)` ou `$`), temos uma regra que deve ser aplicada.

O processo de parsing pode ser realizado da seguinte maneira:

| Pilha  | String | 
| -----  | ------ | 
| $B      | ()$   |

Observe que o topo da pilha é B e o primeiro caractere da string é (. Consultando a tabela, temos que B precisa ser substituído por (RB. No caso, desempilhamos B e empilhamos `B`, `R` e `(`. Note que os símbolos são empilhados na ordem contrária.

| Pilha  | String | 
| -----  | ------ | 
| $B      | ()$   |
| $BR(   | ()$   |

Agora, o topo da pilha coincide com o primeiro caractere da string atual, então desempilhamos e removemos o caractere da string.

| Pilha  | String | 
| -----  | ------ | 
| $B      | ()$   |
| $BR(   | ()$   |
| $BR     | )$   |

No topo da pilha temos R e o primeiro caractere da string é (. Consultando a tabela, temos que R precisa ser substituído por ).

| Pilha  | String | 
| -----  | ------ | 
| $B      | ()$   |
| $BR(   | ()$   |
| $B)     | )$   |

O processo completo é o seguinte:

| Pilha  | String | 
| -----  | ------ | 
| $B      | ()$   |
| $BR(   | ()$   |
| $B)     | )$   |
| $B     | $   |
| $     | $   |

O processo termina quando a pilha temos na pilha `$` e a string é apenas '$'.

Durante o processo de parsing, temos a seguinte linha:

| Pilha  | String | 
| -----  | ------ | 
| $BRRR      | )))$   |

Qual é a string inicial?