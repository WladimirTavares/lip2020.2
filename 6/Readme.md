## Hexadecimal

Faça um programa que lê uma linha formada por várias strings e verifica se cada uma das strings corresponde a constante hexadecimal. Um constante hexadecimal começa com 0, seguido de x ou X, seguido dos dígitos de 0 até 9 ou os caracteres de a até z, maiúsculos ou minúsculos.

**Entrada**
```
0x23 0xFF 0x2F 0xG5 0xFF 0XA0000024
```

**Saída**
```
True
True
True
False
True
True

```

Use o seguinte programa em python:

```Python
import re


## Coloque aqui usa expressão regular
regexp = r''


for string in input().split(' '):
  print( re.fullmatch(regexp, string) != None)

```








