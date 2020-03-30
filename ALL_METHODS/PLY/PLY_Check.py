from PLY import Parser
import time
import os.path

def PLYconsolecheck(_str):
    _parser = Parser.Parser()
    _str += '\n'
    _res = _parser.PLYCheck(_str)
    if _parser.flag:
        return _str.rstrip('\n') + ' --- Correct\n'
    else:
        return _str.rstrip('\n') + ' --- Incorrect\n'

def PLYfilecheck():
    _parser = Parser.Parser()
    StatFile = open('PLYStatistic.txt', 'w')
    inf = open('strings.txt', 'r')
    ouf = open('PLYoutput.txt', 'w')
    _starttime = time.time()

    while True:
        _string = inf.readline()
        if not _string:
            break

        _res = _parser.PLYCheck(_string, _flag=True)
        if _parser.flag:
            ouf.write(_string.rstrip('\n') + ' --- Correct\n')
        else:
            ouf.write(_string.rstrip('\n') + ' --- Incorrect\n')

    _endtime = time.time()
    StatFile.write('Analyzing time:')
    StatFile.write(str(_endtime - _starttime))
    print('Analyzing time:', str(_endtime - _starttime))
    StatFile.write(' seconds\n')
    StatFile.write('\n\n-----List of names-----\n')
    for key in _parser._names.keys():
        StatFile.write(key + ' - ' + str(len(_parser._names[key])) + '\n')

    StatFile.close()
    inf.close()
    ouf.close()