
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'TRUE FALSE IF ELSE ELSEIF ECHO FUNCTION NFUNCTION INCLUDE INTEGER LPARENT RPARENT LCURBRACE RCURBRACE LCORCHETE RCORCHETE STRING STRINGG ID DOSPUNTOS EQUAL MINUS PLUS TIMES DIV MODULO EXPONENCIACION IGUAL NOIGUAL IDENTICO MAYOR MAYORIG MENOR MENORIG AND OR XOR NOT CONCATSTR WHILE DO FOR CIERREprogram : declaracion_sentenciasdeclaracion_sentencias : bloques declaracion_sentencias\n                                | bloquesbloques : importimport : INCLUDE STRINGG CIERRE'
    
_lr_action_items = {'CIERRE':([7,],[8,]),'$end':([1,2,3,5,6,8,],[0,-3,-1,-4,-2,-5,]),'STRINGG':([4,],[7,]),'INCLUDE':([0,2,5,8,],[4,4,-4,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaracion_sentencias':([0,2,],[3,6,]),'import':([0,2,],[5,5,]),'bloques':([0,2,],[2,2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaracion_sentencias','program',1,'p_inicio','phpparser.py',12),
  ('declaracion_sentencias -> bloques declaracion_sentencias','declaracion_sentencias',2,'p_declaracion_sentencias','phpparser.py',16),
  ('declaracion_sentencias -> bloques','declaracion_sentencias',1,'p_declaracion_sentencias','phpparser.py',17),
  ('bloques -> import','bloques',1,'p_bloques','phpparser.py',21),
  ('import -> INCLUDE STRINGG CIERRE','import',3,'p_import','phpparser.py',27),
]
