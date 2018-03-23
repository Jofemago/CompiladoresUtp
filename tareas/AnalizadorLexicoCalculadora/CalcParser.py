import ply.yacc as yacc
from CalcLex import tokens
import CalcLex
import sys




def p_expresion_suma(p):
    'exp : exp SUM term'
    #p[0] = p[1] + p[3]


def p_expresion_resta(p):
    'exp : exp RES term'
    #p[0] = p[1] - p[3]

def p_exp_term(p):
    'exp : term'
    #p[0] = p[1]

def p_term_times(p):
    'term : term MUL factor'
    #p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIV factor'
    #p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    #p[0] = p[1]

def p_factor_num(p):
    'factor : NUMERO'
    #p[0] = p[1]

def p_factor_exp(p):
    'factor : APAREN exp CPAREN'
    #p[0] =  p[2]

# Error rule for syntax errors
def p_error(p):
    print ("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print (result)
