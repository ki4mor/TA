import re
import ply.lex as lex


class Lexer:
    tokens = (
        'NAME', 'NL', 'TYPE_A', 'TYPE_C', 'RESNAME', 'IP', 'UNKNOWN'
    )
   # t_NAME = r'([a-zA-Z]{1}[a-zA-Z0-9]{0,31})(\s)+'
   # t_TYPE = r'([AC]{1})(\s)'
   # t_RESNAME = r'([a-zA-Z]{1}[a-zA-Z0-9]{0,31})'
   # t_IP = r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'

    states = (
        ('name', 'exclusive'),
        ('type', 'exclusive'),
        ('resname', 'exclusive'),
        ('ip', 'exclusive')
    )

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input (self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()


    def t_NAME(self, t):
        r'\s*([a-zA-Z]{1}[a-zA-Z0-9]{0,31})(\s+)'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('type')
        else:
            t.lexer.begin('INITIAL')
        return t

    def t_type_TYPE_C(self, t):
        r'([C]{1})(\s+)'
        t.lexer.begin('resname')
        return t

    def t_type_TYPE_A(self, t):
        r'([A]{1})(\s+)'
        t.lexer.begin('ip')
        return t
    def t_resname_RESNAME(self, t):
        r'([a-zA-Z]{1}[a-zA-Z0-9]{0,31})'
        return t

    def t_ip_IP(self, t):
        r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})'
        return t

    def t_ANY_NL(self, t):
        r'\s*(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_ANY_UNKNOWN(self, t):
        r'(.)+'
        t.lexer.begin('INITIAL')
        return t

    def t_ANY_error(self, t):
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')
        return t


# data = '''           abc    C             dsfdsfsd
# xer A 229.321.312.111
# '''
# l = Lexer()
# l.input(data)
# while True:
#     tok = l.token()
#     if not tok:
#         break
#     print(tok)



