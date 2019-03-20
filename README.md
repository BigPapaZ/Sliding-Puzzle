# Sliding-Puzzle
python3
slidingpuzzle.py
This program consists of a class named slidingPuzzle which consists of a constructor function
and the following method functions: displayPuzzle(), method(), legalMoves(), scramble(), and
isSolved(). All of these functions take self as an input parameter. Additionally, the constructor takes in
the number of rows and columns; method() takes in row index and column index; and scramble() takes
in the number of moves as input parameters as well. The purpose of this program is to help with making
objects needed to play a sliding puzzle game with numeric as the slides.

The constructor uses the input number of rows and columns to construct a list which has all the
integers in the range of number of rows and columns product. Then it divides the list into a list of
smaller list, where each of these secondary lists represent a row.

displayPuzzle() is responsible for displaying this whole data set like a normal pretty table. It
iterates through the main list for secondary lists. Then it iterates through each integer element of the
secondary list. If converts them into a string. If the integer is a single digit, then it adds two whitespaces
in front of it; else, it only adds one. Then it concatenates all the elements of these secondary lists and
prints the product.

method() is responsible for interchanging the position of 0 with a digit at some given
coordinates. Basically at first scans for the coordinates of 0 in the dateset. Then it stores the digits at 0’s
new coordinates in a variable. Then it puts up this value into 0’s old coordinates and moves 0 to its new
position.

legalMoves() is responsible for determining the possible legal moves for 0-plz note that the 0
slide can only move a unit perpendicularly. So basically at first, this function scans for 0’s position. Then
it determines which category of positions it lies on. Then calculates the relevant positions as a list of
tuples with each tuple as a set of coordinates. This list is then returned.
scramble() purpose is to scramble the puzzle by moving legally moving 0 for a given number of
times. So basically for each move it calls the legalmoves() function and stores it in a variable. Then it
randomly chooses one of these moves and moves 0 to a new place.

isSolved() basically tests whether the puzzle is solved or not. This is done by iterating through
the list, followed by iteration of each secondary list’s integers. It basically tests that whether these
elements are arithmetically in an ascending order. If they are, then it returns a True Value, otherwise a
False.


game.py
This program is not object orientated and therefore has no defined functions. It just imports
slidingpuzzle and keeps calling object from it. There is also user interface related string printing. The
object calls and string prints are organized in way that makes it convenient for a user to play with it.
