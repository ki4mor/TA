from SMC import AutomataAnalyzer_sm

class AutomataAnalyzer:
    def __init__(self):
        self._fsm = AutomataAnalyzer_sm.AutomataAnalyzer_sm(self)
        self._isAcceptable = False
        self._fsm.enterStartState()
        self._bufstr = ''
        self._name = ''
        self._nameRes = ''
        self._length = 0
        self._count = 0
        self._type = ''

    def GetNameRes(self):
        return self._nameRes
    def GetName(self):
        return self._name
    def GetType(self):
        return self._type
    def Acceptable(self):
        self._isAcceptable = True
    def Unacceptable(self):
        self._isAcceptable = False
    def Check(self, string):
        self._fsm.Start()
        for c in string:
            if not self._isAcceptable:
                break
            if c.isalpha():
                self._fsm.Letter(c)
            elif c.isdigit():
                self._fsm.Digit(c)
            elif c == ' ':
                self._fsm.SpaceS()
            elif c == '.':
                self._fsm.DotS()
            elif c == '\n':
                self._fsm.EOS()
                break
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        return self._isAcceptable
    def InsToBuf(self, string):
        self._bufstr += string
    def IncLength(self):
        self._length += 1
    def ClearLength(self):
        self._length = 0
    def InsType(self):
        self._type = self._bufstr
    def InsName(self):
        self._name = self._bufstr
    def InsNameOfRes(self):
        self._nameRes = self._bufstr
    def ClearBuf(self):
        self._bufstr = ''
    def InsCount(self):
        self._count += 1
    def LessThan32(self):
        return self._length <= 32
    def CheckCount(self):
        k = int(self._bufstr)
        if 255 >= k >= 0 and self._count == 4:
            return True
        else:
            return False
    def CheckNumber(self):
        k = int(self._bufstr)
        if self._count < 4 and 255 >= k >= 0:
            return True
        else:
            return False
    def CheckTypeA(self):
        a = False
        if self._bufstr == 'A':
            a = True
        return a
    def CheckTypeC(self):
        a = False
        if self._bufstr == 'C':
            a = True
        return a
    def ClearSMC(self):
        self._isAcceptable = True
        self._bufstr = ''
        self._name = ''
        self._nameRes = ''
        self._length = 0
        self._count = 0
        self._type = ''