import stringgenerator
import SMC

import os.path

while True:
    print('1. Generate new file')
    print('2. Check file with SMC')
    print('3. Enter string from keyboard')
    print('0. Quit')
    print('Make your choice: ')
    c = input()
    if c.isdigit():
        choice = int(c)
        if choice == 1:
            print('How many strings do you want to have in a new file?: ')
            while True:
                numstr = input()
                if numstr.isdigit():
                    num = int(numstr)
                    break
                else:
                    print('Wrong choice, try again!')
            stringgenerator.generator(num)
        elif choice == 2:
            SMC.SMCfilecheck()
        elif choice == 3:
            print('Enter the string: ')
            str = input()
            print(' SMC  result:', SMC.SMCconsolecheck(str).rstrip('\n'))
        elif choice == 0:
            break
        else:
            print('Wrong choice, try again!')
    else:
        print('Wrong choice, try again!')
print('The end!')