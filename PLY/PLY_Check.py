import parserR
import time
import os.path

def PLYconsolecheck(_str):
    _parser = parserR.PParser()
    _str += '\n'
    _res = _parser.PLYCheck(_str)
    if _parser.flag:
        return _str.rstrip('\n') + ' --- Correct\n'
    else:
        return _str.rstrip('\n') + ' --- Incorrect\n'

def PLYfilecheck():
    _parser = parserR.PParser()
    StatFile = open('PLYStatistic.txt', 'w')
    inf = open('strings.txt', 'r')
    ouf = open('PLYoutput.txt', 'w')
    _starttime = time.time()
    for line in inf.readlines():
        _res = _parser.PLYCheck(line, _file=True)
        if _parser.flag:
            ouf.write(line.rstrip('\n') + ' --- Correct\n')
        else:
            ouf.write(line.rstrip('\n') + ' --- Incorrect\n')
    _endtime = time.time()
    StatFile.write('Analyzing time:')
    StatFile.write(str(_endtime - _starttime))
    StatFile.write(' seconds\n')
    StatFile.write('\n\n-----List of names-----\n')
    for key in _parser._names.keys():
        StatFile.write(key + ' - ' + str(_parser._names[key]) + '\n')

    StatFile.close()
    inf.close()
    ouf.close()