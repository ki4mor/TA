
import AutomataAnalyzer
import time
import os.path


def SMCconsolecheck(str):
    statemachine = AutomataAnalyzer.AutomataAnalyzer()
    match = statemachine.Check(str)
    if match:
        return str.rstrip('\n') + ' --- Correct\n'
    else:
        return str.rstrip('\n') + ' --- Incorrect\n'


def SMCfilecheck():
    StatFile = open('SMCStatistic.txt', 'w')
    statemachine = AutomataAnalyzer.AutomataAnalyzer()
    names = {}
    inf = open('strings.txt', 'r')
    ouf = open('SMCoutput.txt', 'w')
    _anlstime = time.time()
    for line in inf.readlines():
        match = statemachine.Check(line)
        if match:
            if statemachine.GetType() == 'C':
                if names.get(statemachine.GetName()) is None:
                    names[statemachine.GetName()] = 1
                else:
                    num = names.get(statemachine.GetName())
                    names[statemachine.GetName()] = num + 1
            ouf.write(line.rstrip('\n') + ' --- Correct\n')
        else:
            ouf.write(line.rstrip('\n') + ' --- Incorrect\n')
    print('Analyzing time:', time.time() - _anlstime, 'seconds')
    StatFile.write('Analyzing time:')
    StatFile.write(str(time.time() - _anlstime))
    StatFile.write(' seconds\n')
    StatFile.write('\n\n-----List of names-----\n')
    for key in names.keys():
        StatFile.write(key + ' - ' + str(names[key]) + '\n')

    StatFile.close()
    inf.close()
    ouf.close()