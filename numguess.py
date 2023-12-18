import random

def compareNum(guess, answer):
    diff = abs(guess - answer)
    if diff < 25 and diff > 1:
        print('Almost there.')
    elif diff > 75:
        print('Far off.')
    else:
        print('Close-ish?')
    

answer = random.randint(0,100)
guess = 0

while guess != answer:
    guess = int(input('Pick a number between 1 - 100: '))
    compareNum(guess, answer)
    print(guess, answer)

print('Congrats :)')