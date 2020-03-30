import PLY_Check
import os.path

while True:
    print('4. Check file with PLY')
    print('0. Quit')
    print('Make your choice: ')
    c = input()
    if c.isdigit():
        choice = int(c)
        if choice == 4:
            PLY_Check.PLYfilecheck()
        elif choice == 0:
            break
        else:
            print('Wrong choice, try again!')
    else:
        print('Wrong choice, try again!')
print('The end!')