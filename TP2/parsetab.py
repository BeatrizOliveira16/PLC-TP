
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "GEQ_operator LEQ_operator assignment_operator comment diferent_operator do else fi float float_const id_const if int int_const od primitive_id_const str str_const then while\n    prog : commands ';'\n    \n    commands : commands ';' command\n    \n    commands : command\n    \n    command : declaration\n            | assignment\n            | flux_control\n            | prim_func_call\n    \n    stype : int\n          | float\n          | str\n    \n    sconst : float_const\n    \n    sconst : int_const\n    \n    sconst : str_const\n    \n    declaration : id_const ':' stype\n    \n    declaration : id_const ':' stype declaration_array_subscript_seq\n    \n    ref : id_ref\n        | array_ele_ref\n    \n    id_ref : id_const\n    \n    array_subscript : '[' expression ']'\n    \n    array_1d_subscript : array_subscript\n    \n    array_2d_subscript : array_1d_subscript array_subscript\n    \n    array_1d_ref : id_const array_1d_subscript\n    \n    array_2d_ref : id_const array_2d_subscript\n    \n    array_ele_ref : array_1d_ref\n                  | array_2d_ref\n    \n    declaration_array_subscript : '[' int_const ']'\n    \n    declaration_array_subscript_seq : declaration_array_subscript\n    \n    declaration_array_subscript_seq : declaration_array_subscript_seq declaration_array_subscript\n    \n    assignment : id_ref assignment_operator expression\n    \n    assignment : array_ele_ref assignment_operator expression\n    \n    expression : sconst\n               | prim_func_call\n               | ref_value\n               | arithmetic_exp_p0\n    \n    arithmetic_exp_p0 : arithmetic_exp_p1\n    \n    arithmetic_exp_p0 : arithmetic_exp_p0 relational_operator arithmetic_exp_p1\n    \n    arithmetic_exp_p1 : arithmetic_exp_p2\n    \n    arithmetic_exp_p1 : arithmetic_exp_p1 '+' arithmetic_exp_p2\n    \n    arithmetic_exp_p1 : arithmetic_exp_p1 '-' arithmetic_exp_p2\n    \n    arithmetic_exp_p2 : arithmetic_exp_p3\n    \n    arithmetic_exp_p2 : arithmetic_exp_p2 '*' arithmetic_exp_p3\n    \n    arithmetic_exp_p2 : arithmetic_exp_p2 '/' arithmetic_exp_p3\n    \n    arithmetic_exp_p2 : arithmetic_exp_p2 '%' arithmetic_exp_p3\n    \n  arithmetic_exp_p3 : arithmetic_exp_p4\n  \n  arithmetic_exp_p3 : '!' arithmetic_exp_p4\n  \n    arithmetic_exp_p4 : ref_value\n                      | sconst\n                      | prim_func_call\n                      | '(' expression ')'\n    \n    relational_operator : '='\n                        | diferent_operator\n                        | '<'\n                        | '>'\n                        | GEQ_operator\n                        | LEQ_operator\n    \n    ref_value : array_ele_ref\n    \n    ref_value : id_ref\n    \n    flux_control : if_command\n                 | while_command\n    \n    if_command : if_then\n               | if_then_else\n    \n    if_then : if expression then commands fi\n    \n    if_then_else : if expression then commands else commands fi\n    \n    while_command : while expression do commands od\n    \n    prim_func_call : primitive_id_const '(' func_args ')'\n    \n    func_args : func_arg\n    \n    func_args : func_args ',' func_arg\n    \n    func_args :\n    \n    func_arg : expression\n    "
    
_lr_action_items = {'id_const':([0,18,19,20,25,26,27,28,37,45,59,60,61,62,63,64,65,66,68,69,70,71,72,77,83,97,99,],[8,41,41,8,41,41,41,41,41,41,8,41,-50,-51,-52,-53,-54,-55,41,41,41,41,41,8,41,8,8,]),'primitive_id_const':([0,18,19,20,25,26,27,28,37,45,59,60,61,62,63,64,65,66,68,69,70,71,72,77,83,97,99,],[13,13,13,13,13,13,13,13,13,13,13,13,-50,-51,-52,-53,-54,-55,13,13,13,13,13,13,13,13,13,]),'while':([0,20,59,77,97,99,],[18,18,18,18,18,18,]),'if':([0,20,59,77,97,99,],[19,19,19,19,19,19,]),'$end':([1,20,],[0,-1,]),';':([2,3,4,5,6,7,11,12,14,15,16,17,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,47,48,49,50,51,52,54,55,73,74,75,76,78,79,81,82,84,85,86,87,88,89,90,91,92,93,96,98,100,101,102,],[20,-3,-4,-5,-6,-7,-58,-59,-24,-25,-60,-61,-22,-23,-20,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-2,-14,-8,-9,-10,-21,-29,-30,-45,-46,-47,-48,-15,-27,-19,-65,97,-36,-49,-38,-39,-41,-42,-43,97,-28,-64,-62,-26,97,-63,]),'od':([3,4,5,6,7,11,12,14,15,16,17,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,47,48,49,50,51,52,54,55,73,74,75,76,78,79,81,82,84,85,86,87,88,89,90,91,93,96,98,100,102,],[-3,-4,-5,-6,-7,-58,-59,-24,-25,-60,-61,-22,-23,-20,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-2,-14,-8,-9,-10,-21,-29,-30,-45,-46,-47,-48,-15,-27,-19,-65,96,-36,-49,-38,-39,-41,-42,-43,-28,-64,-62,-26,-63,]),'fi':([3,4,5,6,7,11,12,14,15,16,17,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,47,48,49,50,51,52,54,55,73,74,75,76,78,79,81,82,85,86,87,88,89,90,91,92,93,96,98,100,101,102,],[-3,-4,-5,-6,-7,-58,-59,-24,-25,-60,-61,-22,-23,-20,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-2,-14,-8,-9,-10,-21,-29,-30,-45,-46,-47,-48,-15,-27,-19,-65,-36,-49,-38,-39,-41,-42,-43,98,-28,-64,-62,-26,102,-63,]),'else':([3,4,5,6,7,11,12,14,15,16,17,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,47,48,49,50,51,52,54,55,73,74,75,76,78,79,81,82,85,86,87,88,89,90,91,92,93,96,98,100,102,],[-3,-4,-5,-6,-7,-58,-59,-24,-25,-60,-61,-22,-23,-20,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-2,-14,-8,-9,-10,-21,-29,-30,-45,-46,-47,-48,-15,-27,-19,-65,-36,-49,-38,-39,-41,-42,-43,99,-28,-64,-62,-26,-63,]),':':([8,],[21,]),'assignment_operator':([8,9,10,14,15,22,23,24,52,81,],[-18,26,27,-24,-25,-22,-23,-20,-21,-19,]),'[':([8,22,24,41,48,49,50,51,78,79,81,93,100,],[25,25,-20,25,80,-8,-9,-10,80,-27,-19,-28,-26,]),'(':([13,18,19,25,26,27,28,37,45,60,61,62,63,64,65,66,68,69,70,71,72,83,],[28,37,37,37,37,37,37,37,37,37,-50,-51,-52,-53,-54,-55,37,37,37,37,37,37,]),'do':([14,15,22,23,24,29,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,59,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,]),'*':([14,15,22,23,24,30,31,32,34,35,36,38,39,41,42,43,44,52,73,74,75,76,81,82,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,-11,-12,-13,-56,-57,-18,70,-40,-44,-21,-45,-46,-47,-48,-19,-65,-49,70,70,-41,-42,-43,]),'/':([14,15,22,23,24,30,31,32,34,35,36,38,39,41,42,43,44,52,73,74,75,76,81,82,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,-11,-12,-13,-56,-57,-18,71,-40,-44,-21,-45,-46,-47,-48,-19,-65,-49,71,71,-41,-42,-43,]),'%':([14,15,22,23,24,30,31,32,34,35,36,38,39,41,42,43,44,52,73,74,75,76,81,82,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,-11,-12,-13,-56,-57,-18,72,-40,-44,-21,-45,-46,-47,-48,-19,-65,-49,72,72,-41,-42,-43,]),'+':([14,15,22,23,24,30,31,32,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,-11,-12,-13,-56,-57,68,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,68,-49,-38,-39,-41,-42,-43,]),'-':([14,15,22,23,24,30,31,32,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,-11,-12,-13,-56,-57,69,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,69,-49,-38,-39,-41,-42,-43,]),'=':([14,15,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,61,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,]),'diferent_operator':([14,15,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,62,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,]),'<':([14,15,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,63,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,]),'>':([14,15,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,64,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,]),'GEQ_operator':([14,15,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,65,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,]),'LEQ_operator':([14,15,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-47,-48,-46,66,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,]),'then':([14,15,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,46,52,73,74,75,76,81,82,85,86,87,88,89,90,91,],[-24,-25,-22,-23,-20,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,77,-21,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,]),']':([14,15,22,23,24,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,53,73,74,75,76,81,82,85,86,87,88,89,90,91,94,],[-24,-25,-22,-23,-20,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,81,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,100,]),')':([14,15,22,23,24,28,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,56,57,58,67,73,74,75,76,81,82,85,86,87,88,89,90,91,95,],[-24,-25,-22,-23,-20,-68,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,82,-66,-69,86,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,-67,]),',':([14,15,22,23,24,28,30,31,32,33,34,35,36,38,39,40,41,42,43,44,52,56,57,58,73,74,75,76,81,82,85,86,87,88,89,90,91,95,],[-24,-25,-22,-23,-20,-68,-31,-32,-33,-34,-11,-12,-13,-56,-57,-35,-18,-37,-40,-44,-21,83,-66,-69,-45,-46,-47,-48,-19,-65,-36,-49,-38,-39,-41,-42,-43,-67,]),'float_const':([18,19,25,26,27,28,37,45,60,61,62,63,64,65,66,68,69,70,71,72,83,],[34,34,34,34,34,34,34,34,34,-50,-51,-52,-53,-54,-55,34,34,34,34,34,34,]),'int_const':([18,19,25,26,27,28,37,45,60,61,62,63,64,65,66,68,69,70,71,72,80,83,],[35,35,35,35,35,35,35,35,35,-50,-51,-52,-53,-54,-55,35,35,35,35,35,94,35,]),'str_const':([18,19,25,26,27,28,37,45,60,61,62,63,64,65,66,68,69,70,71,72,83,],[36,36,36,36,36,36,36,36,36,-50,-51,-52,-53,-54,-55,36,36,36,36,36,36,]),'!':([18,19,25,26,27,28,37,60,61,62,63,64,65,66,68,69,70,71,72,83,],[45,45,45,45,45,45,45,45,-50,-51,-52,-53,-54,-55,45,45,45,45,45,45,]),'int':([21,],[49,]),'float':([21,],[50,]),'str':([21,],[51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'commands':([0,59,77,99,],[2,84,92,101,]),'command':([0,20,59,77,97,99,],[3,47,3,3,47,3,]),'declaration':([0,20,59,77,97,99,],[4,4,4,4,4,4,]),'assignment':([0,20,59,77,97,99,],[5,5,5,5,5,5,]),'flux_control':([0,20,59,77,97,99,],[6,6,6,6,6,6,]),'prim_func_call':([0,18,19,20,25,26,27,28,37,45,59,60,68,69,70,71,72,77,83,97,99,],[7,31,31,7,31,31,31,31,31,76,7,76,76,76,76,76,76,7,31,7,7,]),'id_ref':([0,18,19,20,25,26,27,28,37,45,59,60,68,69,70,71,72,77,83,97,99,],[9,39,39,9,39,39,39,39,39,39,9,39,39,39,39,39,39,9,39,9,9,]),'array_ele_ref':([0,18,19,20,25,26,27,28,37,45,59,60,68,69,70,71,72,77,83,97,99,],[10,38,38,10,38,38,38,38,38,38,10,38,38,38,38,38,38,10,38,10,10,]),'if_command':([0,20,59,77,97,99,],[11,11,11,11,11,11,]),'while_command':([0,20,59,77,97,99,],[12,12,12,12,12,12,]),'array_1d_ref':([0,18,19,20,25,26,27,28,37,45,59,60,68,69,70,71,72,77,83,97,99,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'array_2d_ref':([0,18,19,20,25,26,27,28,37,45,59,60,68,69,70,71,72,77,83,97,99,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'if_then':([0,20,59,77,97,99,],[16,16,16,16,16,16,]),'if_then_else':([0,20,59,77,97,99,],[17,17,17,17,17,17,]),'array_1d_subscript':([8,41,],[22,22,]),'array_2d_subscript':([8,41,],[23,23,]),'array_subscript':([8,22,41,],[24,52,24,]),'expression':([18,19,25,26,27,28,37,83,],[29,46,53,54,55,58,67,58,]),'sconst':([18,19,25,26,27,28,37,45,60,68,69,70,71,72,83,],[30,30,30,30,30,30,30,75,75,75,75,75,75,75,30,]),'ref_value':([18,19,25,26,27,28,37,45,60,68,69,70,71,72,83,],[32,32,32,32,32,32,32,74,74,74,74,74,74,74,32,]),'arithmetic_exp_p0':([18,19,25,26,27,28,37,83,],[33,33,33,33,33,33,33,33,]),'arithmetic_exp_p1':([18,19,25,26,27,28,37,60,83,],[40,40,40,40,40,40,40,85,40,]),'arithmetic_exp_p2':([18,19,25,26,27,28,37,60,68,69,83,],[42,42,42,42,42,42,42,42,87,88,42,]),'arithmetic_exp_p3':([18,19,25,26,27,28,37,60,68,69,70,71,72,83,],[43,43,43,43,43,43,43,43,43,43,89,90,91,43,]),'arithmetic_exp_p4':([18,19,25,26,27,28,37,45,60,68,69,70,71,72,83,],[44,44,44,44,44,44,44,73,44,44,44,44,44,44,44,]),'stype':([21,],[48,]),'func_args':([28,],[56,]),'func_arg':([28,83,],[57,95,]),'relational_operator':([33,],[60,]),'declaration_array_subscript_seq':([48,],[78,]),'declaration_array_subscript':([48,78,],[79,93,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> commands ;','prog',2,'p_prog','yac1.py',59),
  ('commands -> commands ; command','commands',3,'p_commands_2','yac1.py',68),
  ('commands -> command','commands',1,'p_commands_1','yac1.py',77),
  ('command -> declaration','command',1,'p_command','yac1.py',86),
  ('command -> assignment','command',1,'p_command','yac1.py',87),
  ('command -> flux_control','command',1,'p_command','yac1.py',88),
  ('command -> prim_func_call','command',1,'p_command','yac1.py',89),
  ('stype -> int','stype',1,'p_stype','yac1.py',97),
  ('stype -> float','stype',1,'p_stype','yac1.py',98),
  ('stype -> str','stype',1,'p_stype','yac1.py',99),
  ('sconst -> float_const','sconst',1,'p_sconst_float','yac1.py',105),
  ('sconst -> int_const','sconst',1,'p_sconst_int','yac1.py',113),
  ('sconst -> str_const','sconst',1,'p_sconst_str','yac1.py',121),
  ('declaration -> id_const : stype','declaration',3,'p_declaration_simple','yac1.py',129),
  ('declaration -> id_const : stype declaration_array_subscript_seq','declaration',4,'p_declaration_array','yac1.py',138),
  ('ref -> id_ref','ref',1,'p_ref','yac1.py',147),
  ('ref -> array_ele_ref','ref',1,'p_ref','yac1.py',148),
  ('id_ref -> id_const','id_ref',1,'p_id_ref','yac1.py',156),
  ('array_subscript -> [ expression ]','array_subscript',3,'p_array_subscript','yac1.py',165),
  ('array_1d_subscript -> array_subscript','array_1d_subscript',1,'p_array_1d_subscript','yac1.py',173),
  ('array_2d_subscript -> array_1d_subscript array_subscript','array_2d_subscript',2,'p_array_2d_subscript','yac1.py',181),
  ('array_1d_ref -> id_const array_1d_subscript','array_1d_ref',2,'p_array_1d_ref','yac1.py',189),
  ('array_2d_ref -> id_const array_2d_subscript','array_2d_ref',2,'p_array_2d_ref','yac1.py',197),
  ('array_ele_ref -> array_1d_ref','array_ele_ref',1,'p_array_ele_ref','yac1.py',206),
  ('array_ele_ref -> array_2d_ref','array_ele_ref',1,'p_array_ele_ref','yac1.py',207),
  ('declaration_array_subscript -> [ int_const ]','declaration_array_subscript',3,'p_declaration_array_subscript','yac1.py',216),
  ('declaration_array_subscript_seq -> declaration_array_subscript','declaration_array_subscript_seq',1,'p_declaration_array_subscript_seq_1','yac1.py',224),
  ('declaration_array_subscript_seq -> declaration_array_subscript_seq declaration_array_subscript','declaration_array_subscript_seq',2,'p_declaration_array_subscript_seq_2','yac1.py',232),
  ('assignment -> id_ref assignment_operator expression','assignment',3,'p_assignment','yac1.py',240),
  ('assignment -> array_ele_ref assignment_operator expression','assignment',3,'p_assignment_array','yac1.py',248),
  ('expression -> sconst','expression',1,'p_expression','yac1.py',256),
  ('expression -> prim_func_call','expression',1,'p_expression','yac1.py',257),
  ('expression -> ref_value','expression',1,'p_expression','yac1.py',258),
  ('expression -> arithmetic_exp_p0','expression',1,'p_expression','yac1.py',259),
  ('arithmetic_exp_p0 -> arithmetic_exp_p1','arithmetic_exp_p0',1,'p_arithmetic_exp_p0_1','yac1.py',267),
  ('arithmetic_exp_p0 -> arithmetic_exp_p0 relational_operator arithmetic_exp_p1','arithmetic_exp_p0',3,'p_arithmetic_exp_p0_2','yac1.py',275),
  ('arithmetic_exp_p1 -> arithmetic_exp_p2','arithmetic_exp_p1',1,'p_arithmetic_exp_p1_1','yac1.py',296),
  ('arithmetic_exp_p1 -> arithmetic_exp_p1 + arithmetic_exp_p2','arithmetic_exp_p1',3,'p_arithmetic_exp_p1_add','yac1.py',304),
  ('arithmetic_exp_p1 -> arithmetic_exp_p1 - arithmetic_exp_p2','arithmetic_exp_p1',3,'p_arithmetic_exp_p1_sub','yac1.py',312),
  ('arithmetic_exp_p2 -> arithmetic_exp_p3','arithmetic_exp_p2',1,'p_arithmetic_exp_p2_1','yac1.py',320),
  ('arithmetic_exp_p2 -> arithmetic_exp_p2 * arithmetic_exp_p3','arithmetic_exp_p2',3,'p_arithmetic_exp_p2_mul','yac1.py',328),
  ('arithmetic_exp_p2 -> arithmetic_exp_p2 / arithmetic_exp_p3','arithmetic_exp_p2',3,'p_arithmetic_exp_p2_div','yac1.py',336),
  ('arithmetic_exp_p2 -> arithmetic_exp_p2 % arithmetic_exp_p3','arithmetic_exp_p2',3,'p_arithmetic_exp_p2_mod','yac1.py',344),
  ('arithmetic_exp_p3 -> arithmetic_exp_p4','arithmetic_exp_p3',1,'p_arithmetic_exp_p3_1','yac1.py',352),
  ('arithmetic_exp_p3 -> ! arithmetic_exp_p4','arithmetic_exp_p3',2,'p_arithmetic_exp_p3_not','yac1.py',360),
  ('arithmetic_exp_p4 -> ref_value','arithmetic_exp_p4',1,'p_arithmetic_exp_p4','yac1.py',368),
  ('arithmetic_exp_p4 -> sconst','arithmetic_exp_p4',1,'p_arithmetic_exp_p4','yac1.py',369),
  ('arithmetic_exp_p4 -> prim_func_call','arithmetic_exp_p4',1,'p_arithmetic_exp_p4','yac1.py',370),
  ('arithmetic_exp_p4 -> ( expression )','arithmetic_exp_p4',3,'p_arithmetic_exp_p4','yac1.py',371),
  ('relational_operator -> =','relational_operator',1,'p_relational_operator','yac1.py',379),
  ('relational_operator -> diferent_operator','relational_operator',1,'p_relational_operator','yac1.py',380),
  ('relational_operator -> <','relational_operator',1,'p_relational_operator','yac1.py',381),
  ('relational_operator -> >','relational_operator',1,'p_relational_operator','yac1.py',382),
  ('relational_operator -> GEQ_operator','relational_operator',1,'p_relational_operator','yac1.py',383),
  ('relational_operator -> LEQ_operator','relational_operator',1,'p_relational_operator','yac1.py',384),
  ('ref_value -> array_ele_ref','ref_value',1,'p_ref_value_array','yac1.py',392),
  ('ref_value -> id_ref','ref_value',1,'p_ref_value_id','yac1.py',400),
  ('flux_control -> if_command','flux_control',1,'p_flux_control','yac1.py',408),
  ('flux_control -> while_command','flux_control',1,'p_flux_control','yac1.py',409),
  ('if_command -> if_then','if_command',1,'p_if_command','yac1.py',417),
  ('if_command -> if_then_else','if_command',1,'p_if_command','yac1.py',418),
  ('if_then -> if expression then commands fi','if_then',5,'p_if_then','yac1.py',426),
  ('if_then_else -> if expression then commands else commands fi','if_then_else',7,'p_if_then_else','yac1.py',435),
  ('while_command -> while expression do commands od','while_command',5,'p_while_do','yac1.py',445),
  ('prim_func_call -> primitive_id_const ( func_args )','prim_func_call',4,'p_prim_func_call','yac1.py',455),
  ('func_args -> func_arg','func_args',1,'p_func_args_1','yac1.py',463),
  ('func_args -> func_args , func_arg','func_args',3,'p_func_args_2','yac1.py',471),
  ('func_args -> <empty>','func_args',0,'p_func_args_empty','yac1.py',479),
  ('func_arg -> expression','func_arg',1,'p_func_arg','yac1.py',487),
]