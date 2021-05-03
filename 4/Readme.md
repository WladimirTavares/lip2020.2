# Expresão Regular

A função *re.findall(pattern, string)* recebe uma expressão regular (pattern) e devolve uma lista de strings de todos os casamentos sem sobreposição da expresão regular na *string*.

Por exemplo, 

```Python
re.findall(r'[0-9]', "123") == ['1','2','3']
re.findall(r'[0-9]', "12,3")== ['1', '2', '3']
```

Agora, vamos fazer o padrão de dois dígitos consecutivos:

```Python
re.findall(r'[0-9][0-9]', "123") == ['12']
```

Note como não temos sobreposição, ele devolve a primeira ocorrência de dois dígitos consecutivos.

Qual das seguintes strings são retornadas pela função

*re.findall(r"[a-z][0-9]","a1 2b cc3 44d")*



