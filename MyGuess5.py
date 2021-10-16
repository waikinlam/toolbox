# -*- coding: utf-8 -*-

# Description:
#
# This is the final version guess number game demo program
# The entry point of program starts with main() and being verified
# by __name__.
# The computer generated number is from 1 to x where x is passed
# from guess(x) and x is set to 10 in this listing.
#
# Author: Lam Wai Kin
# Date: 16 Oct. 2021

import random   # import the random number package

def main():
    guess(10)
    
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    y = 0
    while guess != random_number:
        guess = int(input("Enter your guess number, please: "))
        y = guess
      
        while y < random_number:
            print('Sorry, guess again. Too low.')
            y = random_number
        while y > random_number:
            print('Sorry, guess again. Too high')
            y= random_number
            
    print("You have guessed the number", random_number, "correctly!!")
    
if __name__ == '__main__':
    main()