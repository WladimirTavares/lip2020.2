# Análise Léxica

A análise léxica pode ser realizada utilizando expressões regulares para descrição dos tokens. Considere o seguinte trecho de código:

```ADA
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
```

A análise léxica vai "quebrar" o código em tokens. Por exemplo,

```
Token(type='IF', value='IF', line=1, column=4)
Token(type='ID', value='quantity', line=1, column=7)
Token(type='THEN', value='THEN', line=1, column=16)
Token(type='ID', value='total', line=2, column=8)
Token(type='ASSIGN', value=':=', line=2, column=14)
Token(type='ID', value='total', line=2, column=17)
Token(type='OP', value='+', line=2, column=23)
Token(type='ID', value='price', line=2, column=25)
Token(type='OP', value='*', line=2, column=31)
Token(type='ID', value='quantity', line=2, column=33)
Token(type='END', value=';', line=2, column=41)
Token(type='ID', value='tax', line=3, column=8)
Token(type='ASSIGN', value=':=', line=3, column=12)
Token(type='ID', value='price', line=3, column=15)
Token(type='OP', value='*', line=3, column=21)
Token(type='NUMBER', value=0.05, line=3, column=23)
Token(type='END', value=';', line=3, column=27)
Token(type='ENDIF', value='ENDIF', line=4, column=4)
Token(type='END', value=';', line=4, column=9)
```

Observe que cada lexema da linguagem está classificado em um token. Observe também que podemos ter vários lexemas associado a um mesmo tipo de token.

O seguinte código python faz essa classificação:

```Python
import sys
import re

class Token():
  def __init__(self,type, value, line, column):
    self.type = type
    self.value = value
    self.line = line
    self.column = column
  def __str__(self):
    return "Token(type='%s', value='%s', line=%d, column=%d)" % (self.type, self.value,self.line, self.column) 

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

data = sys.stdin.readlines()

code = ''.join(data)

for token in tokenize(code):
    print(token)
```

Agora, chegou a sua vez de fazer a análise léxica. Modifique o código acima para fazer a análise léxica do seguinte código:

```C
if(quantity){ 
  total = total + price * quantity; 
}
```

Produzindo a seguinte saída:
```
Token(type='if', value='if', line=1, column=0)
Token(type='AP', value='(', line=1, column=2)
Token(type='ID', value='quantity', line=1, column=3)
Token(type='FP', value=')', line=1, column=11)
Token(type='AC', value='{', line=1, column=12)
Token(type='ID', value='total', line=2, column=2)
Token(type='ASSIGN', value='=', line=2, column=8)
Token(type='ID', value='total', line=2, column=10)
Token(type='OP', value='+', line=2, column=16)
Token(type='ID', value='price', line=2, column=18)
Token(type='OP', value='*', line=2, column=24)
Token(type='ID', value='quantity', line=2, column=26)
Token(type='END', value=';', line=2, column=34)
Token(type='FC', value='}', line=3, column=0)
```

Observação: para usar o parênteses e chaves nas expressões regulares, você precisa usar o caractere de escape 
```
r'\(\)\{\}'
```








