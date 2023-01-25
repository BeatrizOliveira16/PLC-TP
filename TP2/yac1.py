
import sys
import ply.yacc as yacc
from lexer import tokens
# ------------------------------------------------------------ Variable Class
class GlobalEnv(dict):
    def __init__(self):
        self.naddr = 0
        self.nlabels = 0

    @property
    def label(self):
        label = self.nlabels
        self.nlabels += 1
        return f'l{label}'

    @property
    def addr(self):
        addr = self.naddr
        self.naddr += 1
        return addr

    def decl(self,var_name,var_type,subtype=None,dims=None):
        if subtype is None:
            self.update({var_name : Var(self,var_type)})
        else:
            self.update({var_name : Array(self,var_type,subtype,dims)})

class Var:
    def __init__(self,env,var_type):
        self.addr = env.addr
        self.type = var_type
        self.size = 1

class Array(Var):
    def __init__(self,env,var_type,subtype,dims):
        from math import prod
        super().__init__(env,var_type)
        self.subtype = subtype
        self.dims = [int(dim) for dim in dims]
        self.size = prod(self.dims)
        env.naddr += self.size - 1

    def get(self,n):
        """Only makes sense for arrays. @n is an array of indexes."""
        if len(n) == 1:
            return n[0]
        if self.size >= 1:
            from math import prod
            N = self.dims
            d = len(self.dims)
            return sum(prod(N[j] for j in range(i,d)) * n[i] for i in range(d))//d
# ------------------------------------------------------------ Pre-defined functions
global_env = GlobalEnv()
global_debug = True
# ------------------------------------------------------------ commands
def p_prog(p):
    """
    prog : commands ';'
    """
    p[0] = p[1]
    if global_debug:
        print('p_prog')
    print(p[0])

def p_commands_2(p):
    """
    commands : commands ';' command
    """
    p[0] = p[1] + p[3]

    if global_debug:
        print('p_commands_2')

def p_commands_1(p):
    """
    commands : command
    """
    p[0] = p[1]
    if global_debug:
        print('p_commands_1')


def p_command(p):
    """
    command : declaration
            | assignment
            | flux_control
            | prim_func_call
    """
    p[0] = p[1]
    if global_debug:
        print('p_command')
# ------------------------------------------------------------ simple type
def p_stype(p):
    """
    stype : int
          | float
          | str
    """
    p[0] = p[1]

def p_sconst_float(p):
    """
    sconst : float_const
    """
    p[0] = f'PUSHF {p[1]}\n'
    if global_debug:
        print('p_sconst_float')

def p_sconst_int(p):
    """
    sconst : int_const
    """
    p[0] = f'PUSHI {p[1]}\n'
    if global_debug:
        print('p_sconst_int')

def p_sconst_str(p):
    """
    sconst : str_const
    """
    p[0] = f'PUSHS {p[1]}\n'
    if global_debug:
        print('p_sconst_str')
# ------------------------------------------------------------ declaration
def p_declaration_simple(p):
    """
    declaration : id_const ':' stype
    """
    global_env.decl(p[1],p[3])
    p[0] = f'PUSHI 0\n'
    if global_debug:
        print('p_declaration_simple')

def p_declaration_array(p):
    """
    declaration : id_const ':' stype declaration_array_subscript_seq
    """
    global_env.decl(p[1],'array',p[3],p[4])
    p[0] = f'PUSHN {global_env[p[1]].size}\n'
    if global_debug:
        print('p_declaration_array')
# ------------------------------------------------------------ refs
def p_ref(p):
    """
    ref : id_ref
        | array_ele_ref
    """
    p[0] = p[1]
    if global_debug:
        print('p_ref')

def p_id_ref(p):
    """
    id_ref : id_const
    """
    # p[0] = f'PUSHG {global_env[p[1]].addr}\n'
    p[0] = global_env[p[1]].addr
    if global_debug:
        print('p_id_ref')

def p_array_subscript(p):
    """
    array_subscript : '[' expression ']'
    """
    p[0] = p[2]
    if global_debug:
        print('p_array_subscript')

def p_array_1d_subscript(p):
    """
    array_1d_subscript : array_subscript
    """
    p[0] = p[1]
    if global_debug:
        print('p_array_1d_subscript')

def p_array_2d_subscript(p):
    """
    array_2d_subscript : array_1d_subscript array_subscript
    """
    p[0] = [p[1],p[2]]
    if global_debug:
        print('p_array_2d_subscript')

def p_array_1d_ref(p):
    """
    array_1d_ref : id_const array_1d_subscript
    """
    p[0] = f'PUSHGP\nPUSHI {global_env[p[1]].addr}\nPADD\n{p[2]}'
    if global_debug:
        print('p_array_1d_ref')

def p_array_2d_ref(p):
    """
    array_2d_ref : id_const array_2d_subscript
    """
    p[0] = f'PUSHGP\nPUSHG {global_env[p[1]].addr}\nPADD\nPUSHI{global_env[p[1]].dims[0]}\n{p[2][0]}\nMUL\n{p[2][1]}\nADD\n{p[2]}\n'
    if global_debug:
        print('p_array_2d_ref')


def p_array_ele_ref(p):
    """
    array_ele_ref : array_1d_ref
                  | array_2d_ref
    """
    p[0] = p[1]
    if global_debug:
        print('p_array_ele_ref')

# ------------------------------------------------------------ array
def p_declaration_array_subscript(p):
    """
    declaration_array_subscript : '[' int_const ']'
    """
    p[0] = p[2]
    if global_debug:
        print('p_declaration_array_subscript')

def p_declaration_array_subscript_seq_1(p):
    """
    declaration_array_subscript_seq : declaration_array_subscript
    """
    p[0] = [p[1]]
    if global_debug:
        print('p_declaration_array_subscript_seq_1')

def p_declaration_array_subscript_seq_2(p):
    """
    declaration_array_subscript_seq : declaration_array_subscript_seq declaration_array_subscript
    """
    p[0] = p[1] + [p[2]]
    if global_debug:
        print('p_declaration_array_subscript_seq_2')
# ------------------------------------------------------------ assignment
def p_assignment(p):
    """
    assignment : id_ref assignment_operator expression
    """
    p[0] = p[3] + f'STOREG {p[1]}\n'
    if global_debug:
        print('p_assignment')

def p_assignment_array(p):
    """
    assignment : array_ele_ref assignment_operator expression
    """
    p[0] = p[1] + p[3] + 'STOREN\n'
    if global_debug:
        print('p_assignment')
# ------------------------------------------------------------ expressions
def p_expression(p):
    """
    expression : sconst
               | prim_func_call
               | ref_value
               | arithmetic_exp_p0
    """
    p[0] = p[1]
    if global_debug:
        print('p_expression')
# ------------------------------------------------------------ arithmetic
def p_arithmetic_exp_p0_1(p):
    """
    arithmetic_exp_p0 : arithmetic_exp_p1
    """
    p[0] = p[1]
    if global_debug:
      print('p_arithmetic_exp_p0_1')

def p_arithmetic_exp_p0_2(p):
    """
    arithmetic_exp_p0 : arithmetic_exp_p0 relational_operator arithmetic_exp_p1
    """
    match p[2]:
        case '=':
            command = 'EQUAL'
        case '/=':
            command = 'EQUAL\n NOT'
        case '<':
            command = 'INF'
        case '>':
            command = 'SUP'
        case '>=':
            command = 'SUPEQ'
        case '<=':
            command = 'INFEQ'
    p[0] = p[1] + p[3] + command + '\n'
    if global_debug:
      print('p_arithmetic_exp_p0_2')

def p_arithmetic_exp_p1_1(p):
    """
    arithmetic_exp_p1 : arithmetic_exp_p2
    """
    p[0] = p[1]
    if global_debug:
      print('p_arithmetic_exp_p1_1')

def p_arithmetic_exp_p1_add(p):
    """
    arithmetic_exp_p1 : arithmetic_exp_p1 '+' arithmetic_exp_p2
    """
    p[0] = p[1] + p[3] + 'ADD\n'
    if global_debug:
      print('p_arithmetic_exp_p1_add')

def p_arithmetic_exp_p1_sub(p):
    """
    arithmetic_exp_p1 : arithmetic_exp_p1 '-' arithmetic_exp_p2
    """
    p[0] = p[1] + p[3] + 'SUB\n'
    if global_debug:
      print('p_arithmetic_exp_p1_sub')

def p_arithmetic_exp_p2_1(p):
    """
    arithmetic_exp_p2 : arithmetic_exp_p3
    """
    p[0] = p[1]
    if global_debug:
      print('p_arithmetic_exp_p2_1')

def p_arithmetic_exp_p2_mul(p):
    """
    arithmetic_exp_p2 : arithmetic_exp_p2 '*' arithmetic_exp_p3
    """
    p[0] = p[1] + p[3] + 'MUL\n'
    if global_debug:
      print('p_arithmetic_exp_p2_mul')

def p_arithmetic_exp_p2_div(p):
    """
    arithmetic_exp_p2 : arithmetic_exp_p2 '/' arithmetic_exp_p3
    """
    p[0] = p[1] + p[3] + 'DIV\n'
    if global_debug:
      print('p_arithmetic_exp_p2_div')

def p_arithmetic_exp_p2_mod(p):
    """
    arithmetic_exp_p2 : arithmetic_exp_p2 '%' arithmetic_exp_p3
    """
    p[0] = p[1] + p[3] + 'MOD\n'
    if global_debug:
      print('p_arithmetic_exp_p2_mod')

def p_arithmetic_exp_p3_1(p):
  """
  arithmetic_exp_p3 : arithmetic_exp_p4
  """
  p[0]= p[1]
  if global_debug:
    print('p_arithmetic_exp_p3_1')

def p_arithmetic_exp_p3_not(p):
  """
  arithmetic_exp_p3 : '!' arithmetic_exp_p4
  """
  p[0]= p[2] + 'NOT\n'
  if global_debug:
    print('p_arithmetic_exp_p3_not')

def p_arithmetic_exp_p4(p):
    """
    arithmetic_exp_p4 : ref_value
                      | sconst
                      | prim_func_call
                      | '(' expression ')'
    """
    p[0] = p[1] if len(p) == 2 else p[2]
    if global_debug:
      print('p_arithmetic_exp_p4')

def p_relational_operator(p):
    """
    relational_operator : '='
                        | diferent_operator
                        | '<'
                        | '>'
                        | GEQ_operator
                        | LEQ_operator
    """
    p[0] = p[1]
    if global_debug:
      print('p_relational_operator')

def p_ref_value_array(p):
    """
    ref_value : array_ele_ref
    """
    p[0] = p[1] + 'LOADN\n'
    if global_debug:
      print('p_ref_value_array')

def p_ref_value_id(p):
    """
    ref_value : id_ref
    """
    p[0] = f'PUSHG {p[1]}\n'
    if global_debug:
      print('p_ref_value_id')
# ------------------------------------------------------------ flux control
def p_flux_control(p):
    """
    flux_control : if_command
                 | while_command
    """
    p[0] = p[1]
    if global_debug:
        print('p_flux_control')

def p_if_command(p):
    """
    if_command : if_then
               | if_then_else
    """
    p[0] = p[1]
    if global_debug:
        print('p_if_command')

def p_if_then(p):
    """
    if_then : if expression then commands fi
    """
    endif = global_env.label
    p[0] = p[2] + f'JZ {endif}\n' + p[4] + f'{endif}:\n'
    if global_debug:
        print('p_if_then')

def p_if_then_else(p):
    """
    if_then_else : if expression then commands else commands fi
    """
    elsecond = global_env.label
    endif = global_env.label
    p[0] = p[2] + f'JZ {elsecond}\n' + p[4] + f'JUMP {endif}\n' + p[6] +f'{endif}:\n'
    if global_debug:
        print('p_if_then_else')

def p_while_do(p):
    """
    while_command : while expression do commands od
    """
    startwhile = global_env.label
    endwhile = global_env.label
    p[0] = f'{startwhile}:\n' + p[2] + f'JZ {endwhile}\n' + p[4] + f'JUMP {startwhile}\n' + f'{endwhile}:\n'
    if global_debug:
        print('p_while_do')
# ------------------------------------------------------------ "primitive function call"
def p_prim_func_call(p):
    """
    prim_func_call : primitive_id_const '(' func_args ')'
    """
    p[0] = p[3] + p[1][1:].upper() + '\n'
    if global_debug:
        print('p_prim_func_call')

def p_func_args_1(p):
    """
    func_args : func_arg
    """
    p[0] = p[1]
    if global_debug:
        print('p_func_args_1')

def p_func_args_2(p):
    """
    func_args : func_args ',' func_arg
    """
    p[0] = p[1] + p[3]
    if global_debug:
        print('p_func_args_2')

def p_func_args_empty(p):
    """
    func_args :
    """
    p[0] = ''
    if global_debug:
        print('p_func_args_empty')

def p_func_arg(p):
    """
    func_arg : expression
    """
    p[0] = p[1]
    if global_debug:
        print('p_func_arg')

# ------------------------------------------------------------ "repl"
def p_error(p):
    print("Syntax error", p)
    parser.exito = False
    
parser = yacc.yacc()
if __name__ == "__main__":
    for line in sys.stdin:
        parser.success = True
        result = parser.parse(line)

