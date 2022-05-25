import random
import time
import sys

def slowPrint(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

num = random.randint(0,100)
slowPrint('Guess a number between 1 and 100')
print('')
def guess():
    ans = int(input(''))
    if ans == num:
        print("Good Job!")
    elif ans < num:
        print("Nope, too low!")
        guess()
    elif ans > num:
        print('Nope, too high!')
        guess()
guess()