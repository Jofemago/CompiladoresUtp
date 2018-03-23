import sys
import ply.lex as lex

'''
PRESENTADO POR:

JOHAN FELIPE MARIN GONZALEZ
JOSE DANIEL MELO FARA
CRISNAYLER GALLEGO OCAMPO
'''
#Lista de tokens
tokens = ['NUMERO', 'SUM', 'RES', 'MUL', 'DIV', 'APAREN', 'CPAREN', 'PUNTO', 'EXPONENTE', ]


#Reglas de expresiones regulares para tokens simples
t_ignore = ' \t'
t_SUM    = r'\+'
t_RES    = r'-'
t_MUL    = r'\*'
t_DIV    = r'/'
t_APAREN = r'\('
t_CPAREN = r'\)'
t_PUNTO = r'\.'
t_EXPONENTE = r'e|E'

#t_ENTERO = r'-?[1-9][0-9]*'

def t_NUMERO(t):
    r'\d+'
    value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Definicion de error que se va a mostrar cuando un caracter ingresado no es valido
def t_error(t):
	print("******Caracter no valido: {}".format(t.value[0]))
	t.lexer.skip(1)
	return t

lex.lex()


#Funcion para recibir la operacion a calcular y
#definir donde hay errores lexicos segun los caracteres ingresados
while True:
	try:
		s = input('operacion > ')
	except EOFError:
		break
	if not s:
		continue


# Almacena la operacion en s
	lex.input(s)


# Muestra todos los tokens en la operacion
	while True:
		tok = lex.token()

		if not tok:
			break
		print(tok)
