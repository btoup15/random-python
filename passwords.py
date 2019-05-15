import math
import os
from random import choice, randint

os.system('cls')
length = int(input('Enter the length of your password: '))
pw = []
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ]
symb = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=']


for x in range(length):
    r = randint(1, 6)
    if r >= 4:
        pw.append(choice(let))
    elif r == 5:
        pw.append(choice(num))
    else:
        pw.append(choice(symb))


print('Your password is: ', ''.join(pw))
