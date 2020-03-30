import Regular
import stringgenerator

while True:
    print('1. Generate new file')
    print('2. Check file')
    print('3. Enter string from keyboard')
    print('0. Quit')
    print('Make your choice: ')
    c = input()
    if c.isdigit():
        choice = int(c)
        if choice == 1:
            stringgenerator.generator()
        elif choice == 2:
            Regular.CheckFromFile()
        elif choice == 3:
            print('Enter the string: ')
            str = input()
            print('RegEx result:', Regular.check(str).rstrip('\n'))
        elif choice == 0:
            break
        else:
            print('Wrong choice, try again!')
    else:
        print('Wrong choice, try again!')
print('Bye Bye')