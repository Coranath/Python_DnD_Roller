import os
from random import randint

os.system('clear')

while True:

    data = input('> ')

    if data == 'q':
        break

    if data[-1].isdigit():

        data = data.split('d')

        data = [int(i) for i in data]

        rolls = []

        for dice in range(data[0]):
            rolls.append(randint(1, data[1]))

        print(f'You rolled:', end='')

        output = ''

        for roll in rolls:

            output += f'{roll}+'

        print(output[:-1], '=', sum(rolls))

