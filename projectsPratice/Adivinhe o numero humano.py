import random

def  guess(x):
    numero_aleatorio = random.randint(1, x)
    guess = 0
    while guess != numero_aleatorio :
        guess = int(input(f'Tente adivinhar um numero entre 1 a {x}'))
        if guess < numero_aleatorio:
            print('desculpe, tente novamente. Numero muito baixo')
        elif guess > numero_aleatorio:
            print('Desculpe, tente novamente, Numero muito alto')

    print('Ei, Parabens. Voce adivinhou o numero {numero_aleatorio} certo')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high, too low(L), or correct(C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('Yay! the computer guessed your number, {guess}, correctly!')



computer_guess(690)      