import ply.lex as lex
import sys




#list of tokens
tokens = [
#simbolos reservados
'INICIOETIQUETA',
'FINETIQUETA',
'TRUE',
'FALSE',

#simbolos
'MINUS',
'PLUS',
'INTEGER',
'CIERRE'
]


t_MINUS = r'\-'
t_PLUS = r'\+'
t_TRUE = r'TRUE|true|True'
t_FALSE = r'FALSE|False|false'
t_INICIOETIQUETA = r'<\?php'
t_FINETIQUETA = r'\?>'
t_INTEGER = r'\d+'

t_CIERRE = r';'


t_ignore = ' \t'


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
