from RegEx import stringgenerator
from RegEx import Regular
from SMC import SMC
from PLY import PLY_Check
import os.path

while True:
    print('1. Enter string from keyboard')
    print('2. Generate new file')
    print('3. Check file with RegEx')
    print('4. Check file with SMC')
    print('5. Check file with PLY')
    print('0. Quit')
    print('Make your choice: ')
    c = input()
    if c.isdigit():
        choice = int(c)
        if choice == 1:
            print('Enter string: ')
            _str = input()
            print('Make your choice: ')
            print('1. Check with all methods')
            print('2. Check with RegEx')
            print('3. Check with SMC')
            print('4. Check with PLY')
            k = input()
            _choice = int(k)
            if _choice == 1:
                print('RegEx result:', Regular.consolecheck(_str).rstrip('\n'))
                print(' SMC  result:', SMC.SMCconsolecheck(_str).rstrip('\n'))
                print(' PLY  result:', PLY_Check.PLYconsolecheck(_str))
            elif _choice == 2:
                print('RegEx result:', Regular.consolecheck(_str).rstrip('\n'))
            elif _choice == 3:
                print(' SMC  result:', SMC.SMCconsolecheck(_str).rstrip('\n'))
            elif _choice == 4:
                print(' PLY  result:', PLY_Check.PLYconsolecheck(_str))
            else:
                print('Wrong choice')
        elif choice == 2:
            print('Enter count of string: ')
            while True:
                _buf = input()
                if _buf.isdigit():
                    _num = int(_buf)
                    break
                else:
                    print('Wrong choice!')
            stringgenerator.generator(_num)
        elif choice == 3:
            Regular.CheckFromFile()
        elif choice == 4:
            SMC.SMCfilecheck()
        elif choice == 5:
            PLY_Check.PLYfilecheck()
        elif choice == 0:
            break
        else:
            print('Wrong choice')
    else:
        print('Wrong choice')
print('Bye Bye')