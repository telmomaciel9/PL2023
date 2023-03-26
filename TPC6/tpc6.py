import subprocess
import sys
import ply.lex as lex
import re

tokens = (
  'FUNC_NAME',
  'CAST', 
  'VARIABLES', 
  'KEYWORDS', 
  'AUXILIAR_PROGRAM', 
  'PROGRAM', 
  'LOOPS_KEYWORDS', 
  'BRACKETS', 
  'CBRACKETS', 
  'RBRACKETS', 
  'RETS', 
  'NUMBER', 
  'COMMENT', 
  'MULTI_COMMENT', 
  "COMMA", 
  'LINE_END', 
  'LIST',
  'SET', 
  'OPERATION',
  'TUPLE'
)

t_VARIABLES = r' \w+(?=\[)*'
t_FUNC_NAME = r' \w+(?=[\{\(])' 
t_PROGRAM = r'program '
t_AUXILIAR_PROGRAM = r'function '
t_LINE_END = r'\;'
t_COMMA = r'\,'
t_LIST = r'\[.*,*\]'
t_SET =  r'\{.*,*\}'
t_TUPLE = r'\(.*,*\)'
t_BRACKETS = r'[\(\)]+'
t_CBRACKETS = r'[\{\}]+'
t_RBRACKETS = r'[\[\]]+'
t_COMMENT = r'//.*'
t_MULTI_COMMENT = r'/\*[\s\S]*?\*/'
t_OPERATION = r'[\=<>\+\*\-\/]+'
t_RETS = r'\.{2}'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)

    return t

def t_CAST(t):
    r'int|float|char|string|double|long|bool'
    return t

def t_KEYWORDS(t):
    r'if|in|or|else|elif|(else if)'
    return t

def t_LOOPS_KEYWORDS(t):
    r'for|while'
    return t

def t_error(t):
    if re.match(r'[ \t\n]', t.value[0]) == None:
      print(f"Unspecified token {t.value[0]}")
    t.lexer.skip(1)

example1 = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}

'''

example2 = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''

lexer = lex.lex()

opção = input("Escolha o exemplo a aplicar:\n")

if (opção == "1"):
    lexer.input(example1)
elif (opção == "2"):
    lexer.input(example2)
else:
    print("Opção inválida.\n")
    subprocess.call(['python3', 'tpc6.py'])
    sys.exit()


while tok := lexer.token():
    print(tok)

