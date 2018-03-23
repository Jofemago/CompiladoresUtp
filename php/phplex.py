import ply.lex as lex
import sys


'''falta implementar arreglos'''
#dudas
#preguntar si hay que definir += , -= ... etc
#preguntar si definir aqui incremento == y decremento
#pregubtar sobre nombre de funciones
#problema archivo de concatenaciones

#list of tokens
tokens = [
#simbolos reservados
'INICIOETIQUETA',
'FINETIQUETA',
'TRUE',
'FALSE',
'IF',
'ELSE',
'ELSEIF',
'ECHO',
'FUNCTION',


#simbolos
#'FUNCNAME',
'INTEGER',#MEJORARLO COMO FUNCION
'LPARENT',
'RPARENT',
'LCURBRACE',
'RCURBRACE',
'LCORCHETE',
'RCORCHETE',
'STRING',  #MEJORARLO COMO FUNCION
'ID',
'DOSPUNTOS',

#operador de asingacion,
"EQUAL",

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


#operadoresde string

#operadores logicos
'AND',
'OR',
'XOR',
'NOT',


#operador de STRING
'CONCATSTR',


#estructuras de control
'WHILE',
'DO',
'FOR',


'CIERRE',
]



t_ignore = ' \t'


t_ID = r'\$(_)?[a-zA-Z][_a-zA-Z0-9]*'
#t_FUNCNAME = r'[a-zA-Z][_a-zA-Z0-9]*'
t_INICIOETIQUETA = r'<\?php'
t_FINETIQUETA = r'\?>'
t_TRUE = r'TRUE|true|True'
t_FALSE = r'FALSE|False|false'
t_IF = r'if'
t_ELSE = r'else'
t_ELSEIF = r'elseif'
t_ECHO = r'echo'
t_FUNCTION = r'function'#\ [a-zA-Z][_a-zA-Z0-9]*'
t_DOSPUNTOS = r':'

#t_FUNCNAME = r'[a-zA-Z][_a-zA-Z0-9]*'
#t_INTEGER = r'\d+'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LCURBRACE = r'\{'
t_RCURBRACE = r'\}'
t_LCORCHETE = r'\['
t_RCORCHETE = r']'
#t_STRING = r'\'(.)*\''

#operadores aritmeticos
t_MINUS = r'\-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIV   = r'/'
t_MODULO = r'%'
t_EXPONENCIACION = r'\*\*'

#OPERADORES de asignacion
t_EQUAL = r'='

#OPERADORES Comparacion
t_IDENTICO = r'==='
t_IGUAL = r'=='
t_NOIGUAL = r'!=='
t_MAYOR = r'>'
t_MAYORIG = r'>='
t_MENOR = r'<'
t_MENORIG = r'<='


#operadoreslogicos
t_AND = r'and|&&'
t_OR = r'or|\|\|'
t_NOT = r'!'
t_XOR = r'xor'

#OPERADORES DE STRING
t_CONCATSTR = r'\.'
t_CIERRE = r';'

#estructuras de control
t_WHILE = r'while'
t_DO = r'do'
t_FOR = r'for'



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
