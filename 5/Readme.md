
Uma expressão regular pode ser quantificada utilizando os quantificadores *, + e ?.

* *(pattern)?* representa que o resultado da expressão regular *pattern* pode ter 0 ou 1 ocorrência.
* *(pattern)+* representa que o resultado da expressão regular *pattern* pode ter 1 ou mais  ocorrência.
* *(pattern)** representa que o resultado da expressão regular *pattern* pode ter 0 ou mais  ocorrência.


Por exemplo, se quisermos encontrar todos os números em um texto, podemos fazer o seguinte:

```Python
re.findall(r'[0-9]+', "123") == ['123']
re.findall(r'[0-9]+', "12,34")== ['12', '34']
```

Se quisermos fazer uma expressão regular para um número ponto flutuante. Vamos considerar que um número ponto flutuante é um ou mais dígitos, seguido por um .,seguido por um ou mais dígitos. Como o ponto tem um significado especial, precisamos usar um caractere especial de escape \\.
Podemos usar também \\d que representa os dígitos de 0 até 9.


```Python
re.findall(r'[0-9]+\.[0-9]+', "12.34") == ['12.34']
re.findall(r'\d+\.\d+', "12.34") == ['12.34']

```


Qual das seguintes strings são retornadas pela função

```Python
re.findall(r"\d+\.\d+","2.34 5.3 .5 2. ")*
```


