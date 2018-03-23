import ply.lex as lex
import sys


'''falta implementar arreglos'''

#list of tokens
tokens = [
#simbolos reservados
'INICIOETIQUETA',
'FINETIQUETA',
'TRUE',
'FALSE',
'IF',
'ELSE',
'ECHO',
'FUNCTION',


#simbolos
#'FUNCNAME',
'INTEGER',#MEJORARLO COMO FUNCION
'LPARENT',
'RPARENT',
'LCURBRACE',
'RCURBRACE',
'STRING',  #MEJORARLO COMO FUNCION
'ID',

#operadores aritmeticos
'MINUS',
'PLUS',
'TIMES',
'DIV',
'MODULO',
'EXPONENCIACION',

#operadores
#Comparacion
'IGUAL',
'NOIGUAL',
'IDENTICO',
'MAYOR',
'MAYORIG',
'MENOR',
'MENORIG',

#operadores logicos
#'AND',
#'OR',
#'NOT',




'CIERRE',
]
t_ignore = ' \t'


t_ID = r'\$[a-zA-Z][_a-zA-Z0-9]*'

t_INICIOETIQUETA = r'<\?php'
t_FINETIQUETA = r'\?>'
t_TRUE = r'TRUE|true|True'
t_FALSE = r'FALSE|False|false'
t_IF = r'if'
t_ELSE = r'else'
t_ECHO = r'echo'
t_FUNCTION = r'function\ [a-zA-Z][_a-zA-Z0-9]*'

#t_FUNCNAME = r'[a-zA-Z][_a-zA-Z0-9]*'
#t_INTEGER = r'\d+'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LCURBRACE = r'\{'
t_RCURBRACE = r'\}'
#t_STRING = r'\'(.)*\''

#operadores aritmeticos
t_MINUS = r'\-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIV   = r'/'
t_MODULO = r'%'
t_EXPONENCIACION = r'\*\*'

#OPERADORES logicos
t_IDENTICO = r'==='
t_IGUAL = r'=='
t_NOIGUAL = r'!=='
t_MAYOR = r'>'
t_MAYORIG = r'>='
t_MENOR = r'<'
t_MENORIG = r'<='

'''t_AND = r''
t_OR = r''
t_NOT = r'''''


t_CIERRE = r';'





def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'(.)*\'|\"(.)*\"'
    t.value = str(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'CodigosPrueba/basico.phpipe'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	#input()
