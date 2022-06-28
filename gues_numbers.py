import random

def guess (x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f'Guss a number 1 and {x}:'))
        if guess<random_number:
            print(('sorry , guess again Too low\n'))
        elif guess>random_number:
            print("sorry , guess again Too high\n")
    print(f'yay, concrats. you have gussed the number {random_number}')
guess(10)

def computer_guss(x):
    low=1
    high= x
    feedback=''
    while feedback !='c':
        if low != high:
            guess=random.randint(low ,high)
        else :
            guess= low
        feedback=input(f'Is {guess} too high (H),  too low (L),or correct (C)??').lower()
        if feedback=='h':
            high = guess-1
        elif feedback =='l':
            low=guess+1

    print(f'yay! the computer gussed your number, {guess},correctly!')

computer_guss(1000)
