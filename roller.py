import os
from random import randint

os.system('clear')

def info():
    
    print("""?: display this menu
q: quit
xdx: rolls any number of dice with any number of sides 2d4 rolls two, four sided dice and 100d2 rolls 100, two sided dice
dx: rolls one die of the number after the d, d6 rolls one six sided die""")
    
def roll(xdx):

    index = xdx.find('d')

    if xdx[index-1].isdigit() and index > 0:

        xdx = xdx.split('d')
        
        xdx = [int(i) for i in xdx]

        rolls = []

        for dice in range(xdx[0]):
            rolls.append(randint(1, xdx[1]))

        print(f'You rolled:', end='')

        output = ''

        for roll in rolls:

            output += f'{roll}+'

        output = output[:-1] # Remove trailing +

        print(output, '=', sum(rolls))

    else:

        xdx = xdx.split('d')

        roll = randint(1, int(xdx[1]))

        print(f'You rolled: {roll}')

        output = str(roll)
    
    return output


print('D&D user tool')
info()


while True:

    data = input('> ')

    index = data.find('d')

    if data == 'q':
        break

    elif data == '?':
        info()

    elif data[index+1].isdigit(): # All dice rolling logic

        if data.find('+') != -1:
            
            data = data.split('+')

            total = 0

            for dice in data:
                #TODO maybe add roll indicators before each sum and show all calculations i.e. (2d6) 3+5 + (3d8) 2+7+4 = 21 

                output = roll(dice)
                
                total += eval(output)

            print(f'You rolled: {total}')

        else:
            roll(data)

    elif data.__contains__('+') or data.__contains__('-') or data.__contains__('*') or data.__contains__('/'):
        print(f'{data} = {eval(data)}')

    else:
        print(f'That input was not valid, enter q to quit or ? for help')