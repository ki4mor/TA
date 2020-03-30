
from SMC import AutomataAnalyzer
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
    outf = open('SMCoutput.txt', 'w')
    _anlstime = time.time()

    while True:
        _string = inf.readline()
        if not _string:
            break

        match = statemachine.Check(_string)

        if match:
            if statemachine.GetType() == 'C':
                if statemachine.GetNameRes() in names and statemachine.GetName() in names[statemachine.GetNameRes()]:
                    outf.write(_string.rstrip('\n') + '  --- Incorrect\n')
                else:
                    outf.write(_string.rstrip('\n') + '  --- Correct\n')
                    if statemachine.GetName() not in names:
                        names[statemachine.GetName()] = []
                        names[statemachine.GetName()].append(statemachine.GetNameRes())
                    else:
                        if statemachine.GetNameRes() not in names[statemachine.GetName()]:
                            names[statemachine.GetName()].append(statemachine.GetNameRes())
            else:
                outf.write(_string.rstrip('\n') + '  --- Correct\n')
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