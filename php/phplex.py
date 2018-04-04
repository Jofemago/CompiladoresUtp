import ply.lex as lex
import sys


#list of tokens
tokens = [
#simbolos reservados
'TRUE',
'FALSE',
'IF',
'ELSE',
'ELSEIF',
'ECHO',
'FUNCTION',
'NFUNCTION',


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
'STRINGG',
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



t_DOSPUNTOS = r':'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LCURBRACE = r'\{'
t_RCURBRACE = r'\}'
t_LCORCHETE = r'\['
t_RCORCHETE = r']'

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


#OPERADORES DE STRING
t_CONCATSTR = r'\.'
t_CIERRE = r';'



def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\"'
    t.value = str(t.value)
    return t

def t_STRINGG(t):
    r'\'[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\''
    t.value = str(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_FUNCTION(t):
    r'function'
    return t


def t_TRUE(t):
    r'TRUE|true|True'
    return t

def t_FALSE(t):
    r'FALSE|False|false'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_ECHO(t):
    r'echo'
    return t


#operadoreslogicos
def t_AND(t):
    r'and|&&'
    return t

def t_OR(t):
    r'or|\|\|'
    return t


def t_NOT(t):
    r'!'
    return t

def t_XOR(t):
    r'xor'
    return t
#estructuras de control
def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_FOR(t):
    r'for'
    return t

def t_ID(t):
    r'\$(_)?[a-zA-Z][a-zA-Z_0-9]*'
    return t

def t_NFUNCTION(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    return t
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
