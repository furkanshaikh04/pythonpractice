print('Welcome to Code-Decode!')
x = int(input('Enter 1. for Code and 2. for Decode\n'))


def code(input):
    if len(input) < 3 or len(input) == 3:
        print(input[1::] + input[0])
    else:
        print(input[::-1])


def decode(input):
        if len(input) < 3 or len(input) == 3:
            print(input[-1] + input[:-1])
        else:
             print(input[::-1])

if x == 1:
     code(input('Enter the word you want to encode - \n'))
elif x == 2:
     decode(input('Enter the word you want to decode - \n'))
else:
     print('Wrong statement! Choose either 1 or 2!')