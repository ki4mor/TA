import re
import time



def CheckFromFile():
    StatFile = open('RegExStatistic.txt', 'w')
    _gnrttime = time.time()
    names = {}
    inf = open('strings.txt', 'r')
    outf = open('RegExoutput.txt', 'w')
    _anlstime = time.time()
    while True:
        _string = inf.readline()
        if not _string:
            break

        _regular = r'^([a-zA-Z]{1}[a-zA-Z0-9]{0,31})(\s+)((([C]{1})(\s)([a-zA-Z]{1}'
        _regular += r'[a-zA-Z0-9]{0,31}))|(([A]{1})(\s+)(([0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\.)'
        _regular += r'{3}([0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])))$'
        _string = _string.strip('\n')
        _string = _string.strip(' ')
        _result = re.match(_regular, _string)

        if _result is not None:
            if _result.group(9) == 'A':
                outf.write(_string.rstrip('\n') + ' --- Correct\n')
            if _result.group(5) == 'C':
                if _result.group(7) in names and _result.group(1) in names[_result.group(7)]:
                    outf.write(_string.rstrip('\n') + ' --- Incorrect\n')
                else:
                    outf.write(_string.rstrip('\n') + ' --- Correct\n')
                    if _result.group(1) not in names:
                        names[_result.group(1)] = []
                        names[_result.group(1)].append(_result.group(7))
                    else:
                        if _result.group(7) not in names[_result.group(1)]:
                            names[_result.group(1)].append(_result.group(7))
        else:
            outf.write(_string.rstrip('\n') + ' --- Incorrect\n')






    print('Analyzing time:', time.time() - _anlstime, 'seconds')
    StatFile.write('Analyzing time:')
    StatFile.write(str(time.time() - _anlstime))
    StatFile.write(' seconds\n')
    StatFile.write('\n\n-----List of names-----\n')
    for key in names.keys():
        StatFile.write(key + ' - ' + str(len(names[key])) + '\n')

    StatFile.close()
    inf.close()
    outf.close()



def consolecheck(_str):
    _str = _str.strip(' ')
    _reg = r'^([a-zA-Z]{1}[a-zA-Z0-9]{0,31})(\s+)((([C]{1})(\s)([a-zA-Z]{1}'
    _reg += r'[a-zA-Z0-9]{0,31}))|(([A]{1})(\s+)(([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3}))))$'
    _res = re.match(_reg, _str)

    if _res is not None:
        if _res.group(9) == 'A':
            if int(_res.group(12)) <= 255 and int(_res.group(13)) <= 255 and int(
                    _res.group(14)) <= 255 and int(_res.group(15)) <= 255:
                return _str.rstrip('\n') + '  --- Correct\n'
            else:
                return _str.rstrip('\n') + '  --- Incorrect\n'
        else:
            return _str.rstrip('\n') + '  --- Correct\n'
    else:
        return _str.rstrip('\n') + '  --- Incorrect\n'
