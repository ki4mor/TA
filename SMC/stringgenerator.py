import random
import string
import time

def makerndstr(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(size))
def makernddigitstr(size):
    return ''.join(random.choice(string.digits) for i in range(size))
def generator(_num=10000):
    StatFile = open('SMCStatistic.txt', 'w')
    _gnrttime = time.time()
    _types = ['A', 'C']
    with open('strings.txt', 'w') as ouf:
        for i in range(_num):
            bufstr = ''
            bufstr += makerndstr(random.randint(0, 32))
            bufstr += ' '
            _type = random.choice(_types)
            _tp = _type
            bufstr += _type
            bufstr += ' '
            if _tp == "A":
                for j in range(4):
                    bufstr += str(random.randint(0, 255))
                    if j < 3:
                        bufstr += '.'
            else:
                bufstr += makerndstr(random.randint(0, 32))

            ouf.write(bufstr + '\n')
    print('Generation time:', time.time() - _gnrttime, 'seconds')
    StatFile.write('-----List of Timing-----\n')
    StatFile.write('Generation time:')
    StatFile.write(str(time.time() - _gnrttime))
    StatFile.write(' seconds\n')
    StatFile.close()