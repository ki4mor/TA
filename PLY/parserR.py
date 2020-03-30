import lexer
import ply.yacc as yacc


class PParser:
    tokens = lexer.Lexer.tokens

    def __init__(self):
        self._lexer = lexer.Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._names = {}
        self.flag = False

    def p_stroka(self, p):
        """stroka : NAME TYPE_A IP NL
        | NAME TYPE_C RESNAME NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]
        if p[2].strip() == 'A':
            _ip = p[3].split('.')
            for line in _ip:
                if 0 <= int(line) <= 255:
                    self.flag = True
                else:
                    self.flag = False
                    break
        if p[2].strip() == 'C':
            self.flag = True
            if self._names.get(p[1]) is None:
                self._names[p[1]] = 1
            else:
                num = self._names.get(p[1])
                self._names[p[1]] = num + 1

    def p_stroka_zero_error(self, p):
        """stroka : err NL"""
        p[0] = p[1] + p[2]

    def p_stroka_first_error(self, p):
        """stroka : NAME err NL"""
        p[0] = p[1] + p[2] + p[3]

    def p_stroka_second_error(self, p):
        """stroka : NAME TYPE_A err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_stroka_third_error(self, p):
        """stroka : NAME TYPE_C err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_err(self, p):
        """err : UNKNOWN"""
        p[0] = p[1]

    def p_error(self, p):
        pass

    def PLYCheck(self, _str, _file=False):
        if _file == False:
            self._names.clear()
        self.flag = False
        _res = self._parser.parse(_str)
        return _str

data = '''xer A 229.21.32.111
'''
y = PParser()
y.PLYCheck(data)
print(y.flag)