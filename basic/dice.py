import random

MAX_DICE = 6
MIN_DICE = 1

def main():
    # Create y to start the dice game
    again = 'y'
    while again == 'y' or again == 'Y':
        print("Rolling the dice ")
        print("Their values are: ")
        print(random.randint(MIN_DICE, MAX_DICE))
        print(random.randint(MIN_DICE, MAX_DICE))
        
        again = input("Play again --> Enter y or Y: ")

main()