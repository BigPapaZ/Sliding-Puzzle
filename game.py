import sys
from slidingpuzzle import *

print("Welcome to Sliding Puzzle game")


#Getting the dimensions and the difficulty level as inputs
width=int(input("--Enter the width of the puzzle:",))
height=int(input("--Enter the height of the puzzle:",))
difficulty=int(input("--Enter the difficulty level\n>>>> 1, 2, or 3 (1 easiest, 2 medium, 3 hardest) :",))

#making sre that the difficulty level is a avlid integer
while difficulty not in [1,2,3]:
    print("Not a valid difficulty level! Please enter 1, 2, or 3.")
    difficulty = int(input("--Enter the difficulty level\n>>>> 1, 2, or 3 (1 easiest, 2 medium, 3 hardest) :", ))


#Making the puzzle object
Puzzle=SlidingPuzzle(height, width)


#Shuffling for a given level of difficulty
if difficulty==1:
    Puzzle.scramble(3)

if difficulty==2:
    Puzzle.scramble(11)

if difficulty==3:
    Puzzle.scramble(19)


#The game starts
while True:
    Puzzle.displayPuzzle()

    #user Input
    row=int(input("Pick a row:"))
    col=int(input("Pick a column:"))

    #Processing the input
    x=(row,col)
    a=Puzzle.legalMoves()
    if x not in a:
        print("Illegal Move!")
        continue
    if x in a:
        Puzzle.method(row,col)

    #Determining whether the new format of the string is ordered properly.
    if Puzzle.isSolved()==True:
        print("You Win!!")
        sys.exit()