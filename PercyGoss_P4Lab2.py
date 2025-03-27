menu = 'yes'
while (menu.lower() == 'yes'): 
    print()
    num = int(input('Enter an integer: '))
    print()
    if num < 0:
        print('This program does not handle negative numbers\n')
        menu = input('Would you like to run the program again? ')
    else:
        for mult in range (1, 13):
            print(num, '*', mult, '=', num*mult)
        print()
        menu = input('Would you like to run the program again? ')
