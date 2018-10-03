import random
import sys


class funcionario():

    def __init__(self, nome, sobre):
        self.nome = nome
        self.sobre = sobre

    @property
    def junta(self):
        return f'{self.nome} {self.sobre}'


print("I'm thinking in a number between 1 and 20.")
secretNumber = random.randint(1, 20)
guessesTaken = 0
while guessesTaken < 6:
    print('Type in a guess and press enter.')
    guess = int(input())
    guessesTaken = guessesTaken + 1
    if guess < secretNumber:
        print('Too low!')
    if guess > secretNumber:
        print('Too high!')
    if guess == secretNumber:
        print('You have guessed my number in ' +
              str(guessesTaken) + ' guesses!')
        sys.exit()
print('Nope! My number was ' + str(secretNumber))
