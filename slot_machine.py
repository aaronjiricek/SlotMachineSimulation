#!/usr/bin/python3

import getopt, sys
from random import seed
from random import randint


# variables
startingCash = 100
goal = 500
numberOfExperiments = 1000000
minNumberOfBets = 1
maxNumberOfBets = 21
 
 
 
def main():
    seed()
    RunGames()
 
def RunGames():
    print(f"Starting {numberOfExperiments} experiments from {minNumberOfBets} bets to {maxNumberOfBets} bets")

    for numberOfBets in range(minNumberOfBets, maxNumberOfBets):
        # Calculate the bet based on the number of bets and the starting cash.
        # the bet is in pennies, rounded up if there are any fractions of a penny
        bet = ((startingCash*100) + (numberOfBets - 1)) // numberOfBets 
        betInDolars = bet / 100;

        # Initialize the count of how many times you won $500 for this beting style
        goBigCount = 0

        print(f"{numberOfBets}, {betInDolars}, ", end='', flush=True)

        # run a simulation of the betting style "numberOfExperiments" times and count the number of times the betting style wins over the goal
        for experiments in range(numberOfExperiments):
            winings = 0
            for spins in range(numberOfBets):
                winings += spin(bet)
                if(winings >= (goal * 100)):
                    goBigCount += 1
                    break

        # calculate the probablity of going over the goal for this betting style
        probabilityOfGoBig = goBigCount / numberOfExperiments

        # print the results for this experiment
        print(f"{probabilityOfGoBig}", flush=True)


# play one spin of the slot machine and return the amount of money won based on the bet 
def spin(_bet):
    _spin = randint(1,216)
    if(_spin < 121):
        return 0
    elif(_spin < 196):
        return _bet
    elif(_spin < 211):
        return 4*_bet
    elif(_spin < 216):
        return 10*_bet
    else:
        return 30*_bet

 
if __name__ == "__main__":
    main()
