#!/usr/bin/python3

import getopt, sys
from random import seed
from random import randint


# option variables
debug = False
startingCash = 100
goal = 500
numberOfExperiments = 1000000
minNumberOfBets = 1
maxNumberOfBets = 21
 
 
 
def main():
    seed()
    GetOptions()
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
                if (debug):
                    print (f"experiments={experiments}, spins={spins}, winings={winings}")
                if(winings >= (goal * 100)):
                    goBigCount += 1
                    break

        # calculate the probablity of going over the goal for this betting style
        probabilityOfGoBig = goBigCount / numberOfExperiments

        # print the results for this experiment
        if(debug):
            print(f"goBigCount={goBigCount}, numberOfExperiments={numberOfExperiments}")
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

# get options for running the program
def GetOptions():
    global debug
    global startingCash
    global goal
    global numberOfExperiments
    global minNumberOfBets
    global maxNumberOfBets
 
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd", ["help", "debug", "cash=", "goal=", "minbets=", "maxbets=", "experiments="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    for o, a in opts:
        if o in ("-d", "--debug"):
            print("got here")
            debug = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o == "--cash":
            startingCash = int(a)
        elif o == "--goal":
            goal = int(a)
        elif o == "--minbets":
            minNumberOfBets = int(a)
        elif o == "--maxbets":
            maxNumberOfBets = int(a)
        elif o == "--experiments":
            numberOfExperiments = int(a)
        else:
            assert False, "unhandled option"
  
# help menu
def usage():
    usageString = """slot machine.py simulates running a slot machine for Amanda's class.
 
This will simulate a large number of experiments and output the percentage of those experiments where the player won more than --goal amount of money.
 
Options:
    -h --help     Print this help file
    -d --debug    Print debug information
    --cash        Starting Cash.  Default 100
    --goal        Amount of Cash at the end of each experiment to be considered sucessful.  Default 500
    --minbets     Min number of Bets to make
    --maxbets     Max number of Bets to make
    --experiments Number of Experiments to run.  Default 1,000,000
"""
    print(usageString)
 
if __name__ == "__main__":
    main()
