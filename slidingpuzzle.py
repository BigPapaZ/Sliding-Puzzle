import random

class SlidingPuzzle:

    #constuctor
    def __init__(self, nrow, ncol):
        self.y=nrow
        self.x=ncol
        self.EmptyList1=[]
        self.EmptyList2=[]

        #Generating the list of lists
        for i in range(self.x*self.y):  # x*y
            self.EmptyList1 += [i]    #A list with all the integers in the range in it
        self.acc1 = 0
        self.EmptyList2 = []
        #Dividing the given list of integers into lists representing lists
        while True:
            if self.acc1 >= len(self.EmptyList1): break
            self.EmptyList2+=[self.EmptyList1[self.acc1:self.acc1 + self.x]]
            self.acc1 += self.x

        #Establishing some extra templates of the list of lists
        self.EmptyList3=self.EmptyList2
        self.EmptyList4=self.EmptyList2



    def displayPuzzle(self):
        '''
        Prints a given list of lists into a table
        Input: Self
        Return: None
        '''

        self.acc2 = 0             #An accumulator to help determine the index of the list within the bigger list
        self.EmptyList3 = self.EmptyList2
        for i in self.EmptyList3:
            self.acc3 = 0 #An accumulator to help determine the index of an integer within the secondary list

            #converting the integer elements of a list into a string
            for x in i:
                if len(str(x)) == 1:     #adding 2 whitespaces if the integer is only one digit long
                    self.EmptyList3[self.acc2][self.acc3] = "  " + str(x)
                elif len(str(x))==2:     #adding 1 whitespaces if the integer is two digits long
                    self.EmptyList3[self.acc2][self.acc3] = " " + str(x)
                self.acc3 += 1           #incrementing an accumulator
            self.acc2 += 1               #incrementing an accumulator
        for i in self.EmptyList3: #Concatenating the secondary list into a single list
            print(''.join(i))
        self.EmptyList3=self.EmptyList2



    def method(self, rowIndex, colIndex):
        '''
        Interchanges the position of 0 with the a digit's given coordinates at a given point
        Input: Self, x-coordinate, y-coordinate
        return: The modified string
        '''
        self.rowIndex=rowIndex
        self.colIndex=colIndex

        #scanning for 0's coordinates
        self.acc3=0
        for i in self.EmptyList2:
            self.acc4=0
            for x in i:
                x=int(x)        #Had to be done. without it x would be a string with whitespaces in front of it

                #Storing the coordinates of 0
                if x==0:
                    self.List_Index=self.acc3
                    self.Individual_Index=self.acc4

                self.acc4+=1
            self.acc3+=1



        self.Value_To_be_Modified=self.EmptyList2[self.rowIndex][self.colIndex]    #Storing the integer at 0's to be new
                                                                                   #position into a variable

        self.EmptyList2[self.List_Index][self.Individual_Index] = self.Value_To_be_Modified #Assinging the integer to be
                                                                                            #moved 0's place

        self.EmptyList2[self.rowIndex][self.colIndex]=0  #putting 0 at its new position

        self.EmptyList3, self.EmptyList4=self.EmptyList2, self.EmptyList2




    def legalMoves(self):
        '''
        Determines the possible moves for a 0 at a given position
        Input: self
        return: A list of tuples representing the possible moves
        '''

        # Determining the position of 0
        self.acc3 = 0
        for i in self.EmptyList3:
            self.acc4 = 0
            for x in i:
                x=int(x)
                if x == 0:
                    self.List_Index = self.acc3
                    self.Individual_Index = self.acc4
                self.acc4 += 1
            self.acc3 += 1

        # Checking to see which category of positions do the coordinates of 0 fall into and then generating the relevant
        # movable legal coordinates
        if self.List_Index == 0 and self.Individual_Index == 0:
            self.LegalMoves = [(self.List_Index + 1, self.Individual_Index), (self.List_Index, self.Individual_Index + 1)]
        elif self.List_Index == 0 and self.Individual_Index != (self.x-1):  # x
            self.LegalMoves = [(self.List_Index + 1, self.Individual_Index), (self.List_Index, self.Individual_Index + 1),
                          (self.List_Index, self.Individual_Index - 1)]
        elif self.List_Index != (self.y-1) and self.Individual_Index == 0:  # y
            self.LegalMoves = [(self.List_Index + 1, self.Individual_Index), (self.List_Index - 1, self.Individual_Index),
                          (self.List_Index, self.Individual_Index + 1)]
        elif self.List_Index == 0 and self.Individual_Index == (self.x-1):  # x
            self.LegalMoves = [(self.List_Index + 1, self.Individual_Index), (self.List_Index, self.Individual_Index - 1)]
        elif self.List_Index == (self.y-1) and self.Individual_Index == 0:  # y
            self.LegalMoves = [(self.List_Index - 1, self.Individual_Index), (self.List_Index, self.Individual_Index + 1)]
        elif self.List_Index == (self.y-1) and self.Individual_Index == (self.x-1):
            self.LegalMoves = [(self.List_Index - 1, self.Individual_Index), (self.List_Index, self.Individual_Index - 1)]
        elif self.List_Index == (self.y-1) and self.Individual_Index != (self.x-1):
            self.LegalMoves = [(self.List_Index - 1, self.Individual_Index), (self.List_Index, self.Individual_Index - 1),
                          (self.List_Index, self.Individual_Index + 1)]
        elif self.List_Index != (self.y-1) and self.Individual_Index == (self.x-1):
            self.LegalMoves = [(self.List_Index - 1, self.Individual_Index), (self.List_Index + 1, self.Individual_Index),
                          (self.List_Index, self.Individual_Index - 1)]
        else:
            self.LegalMoves = [(self.List_Index + 1, self.Individual_Index), (self.List_Index - 1, self.Individual_Index),
                          (self.List_Index, self.Individual_Index + 1), (self.List_Index, self.Individual_Index - 1)]



        return self.LegalMoves



    def scramble(self, NumberOfMoves):
        '''
        It scrambles an ordered table for a given number og moves
        Input: Self, Number of moves
        return: None
        '''
        self.NOM=NumberOfMoves


        for i in range(self.NOM):
            self.list_of_moves=self.legalMoves()
            self.len_of_list=len(self.list_of_moves)
            self.random_integer=random.randint(1,self.len_of_list)-1
            self.method(self.list_of_moves[self.random_integer][0],self.list_of_moves[self.random_integer][1])




    def isSolved(self):
        '''
        Method for determining whether the table is in the right order
        Input: Self
        Output: A boolean value
        '''
        self.acc5=0
        for list in self.EmptyList3:
            for i in list:
                i=int(i)
                if self.acc5==0:
                    self.acc5=1
                    self.previous_integer=i
                else:
                    if i<=self.previous_integer:
                        return False
                        break
                    else:return True; break