import ply.lex as lex
import sys

tokens = ["id_const","float_const", "int_const", "str_const",'int','str','float','assignment_operator','diferent_operator', 'GEQ_operator','LEQ_operator','if','then','else','do','od','while','fi','primitive_id_const','comment']
literals = ['(',')','[',']','=','+','-','*','/','%','<','>',':','!',';','≔',',']

# declaração das Palavras-Reservadas e dos Simbolos de Classe (variáveis)

def t_if(t):
    r'\bif\b'
    return t

def t_fi(t):
    r'\bfi\b'
    return t

def t_then(t):
    r'\bthen\b'
    return t

def t_else(t):
    r'\belse\b'
    return t

def t_do(t):
    r'\bdo\b'
    return t

def t_od(t):
    r'\bod\b'
    return t

def t_while(t):
    r'\bwhile\b'
    return t

def t_diferent_operator(t):
    r'/='
    return t

def t_GEQ_operator(t):
    r'>='
    return t

def t_LEQ_operator(t):
    r'<='
    return t

def t_assignment_operator(t):
    r':='
    return t

def t_int(t):
    r'\bint\b'
    return t

def t_float(t):
    r'\bfloat\b'
    return t

def t_str(t):
    r'\bstr\b'
    return t

def t_comment(t):
    r'`[^`]*`'
    pass

def t_primitive_id_const(t):
    r'_[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_id_const(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    return t

def t_float_const(t):
    r"[0-9]*\.[0-9]+"
    t.value = float(t.value)
    return t

def t_int_const(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t

def t_str_const(t):
    r'"[^"]*"'
    # t.value = t.value[1:-1]
    return t

# declaração dos Carateres que podem aparecer no texto de entrada e que devem ser ignorados
t_ignore = " \n\t"

# declaração da ação a fazer relativa aos Carateres que NÃO podem aparecer no texto de entrada
def t_error(t):
    print("Carater ilegal: ", t.value)


lexer = lex.lex()

if __name__ == "__main__":
    for line in sys.stdin:
        lexer.input(line)
        tok = lexer.token()
        while tok:
            print(tok)
            tok = lexer.token()