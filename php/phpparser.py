import ply.yacc as yacc
from phplex import tokens
import phplex
import sys

VERBOSE = 1

val=False


def p_inicio(p):
    'program : declaracion_sentencias'
    pass

def p_declaracion_sentencias(p):
    '''declaracion_sentencias : bloques declaracion_sentencias
                                | bloques'''


def p_bloques(p):
    '''bloques : import'''
    pass


#importaciones dentro de php
def p_import(p):
    '''import : INCLUDE STRINGG CIERRE'''


# Error rule for syntax errors
def p_error(p):
    global val
    val = True
    print('ERROR DE SINTAXIS')

# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'CodigosPrueba/basico.phpipe'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	if not val :
		print("Tu parser reconocio correctamente todo")
	#input()
