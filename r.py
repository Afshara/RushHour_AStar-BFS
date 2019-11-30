#!/bin/python3
import sys
import copy
import random
#-----------------------------------------------------------------------------------------------------

#class Path represents a sequences of board states
class Path:
	def __init__(self, inputString=[]):
		#assuming inputString is an array of boards
		self.inputPath = []
		self.inputPath.append(inputString)


	#to add a board to the depth
	#goal : [[],[],[]...add []]
	def add(self, newBoard):
		inputPath = self.inputPath
		inputPath.append(newBoard)
	
	def getPath(self):
		return(self.inputPath)

	#to clone(copy) the path for branching
	def clone(self):
		cloneBoard = copy.deepcopy(self)
		return(cloneBoard)
	
	#to return the last board
	def last(self):
		inputPath = self.inputPath
		lastBoard = inputPath[len(inputPath)-1]
		return(lastBoard)
	
	#print maximun of 6 boards in a line and then continues to print the rest of the boards in 2nd line
	def pathPrintFunction(self, finalArray=[]):
		#a = 0
		#x = range(len(self.inputPath))
		for i in self.inputPath:
			#print(i)
			row=0
			while (row <= 7):
				print(i[row])
				row += 1

		#	for row in range(len(eachBoard)):
		#		for col in range(len(eachBoard[row])):
		#			print(eachBoard[row][col])
		#			if i < (x - 1):
		#				print(finalArray[i][a], end="")
		#			elif i == (x - 1):
		#				print(finalArray[i][a])


class PathAStar:
	def __init__(self):
		# assuming inputString is an array of boards
		self.inputPath = []

	# to add a board to the depth
	# goal : [[],[],[]...add []]
	def add(self, newBoard):
		inputPath = self.inputPath
		inputPath.append(newBoard)

	def getPath(self):
		return (self.inputPath)

	# to clone(copy) the path for branching
	def clone(self):
		cloneBoard = copy.deepcopy(self)
		return (cloneBoard)

	# to return the last board
	def last(self):
		inputPath = self.inputPath
		lastBoard = inputPath[len(inputPath) - 1]
		return (lastBoard)

	# print maximun of 6 boards in a line and then continues to print the rest of the boards in 2nd line
	def pathPrintFunction(self, finalArray=[]):
		# a = 0
		# x = range(len(self.inputPath))
		for i in self.inputPath:
			#print(i)
			row=0
			while (row <= 7):
				print(i[row])
				row += 1
	# eachBoard = i

#	for row in range(len(eachBoard)):
#		for col in range(len(eachBoard[row])):
#			print(eachBoard[row][col])
#			if i < (x - 1):
#				print(finalArray[i][a], end="")
#			elif i == (x - 1):
#				print(finalArray[i][a])


#-------------------------------------------------------------------------------------------------------
#Create a representation of the board
#create a board class that takes a sequence of strings, stores it in an arrray
#seperate the rows by "|"
#create eight rows and 8 columns, where row 1 and row 8 is "------" and row 2 - 7 has column 1 and 8 "|" except for row 3.
#create a function that prints the list of boards horizontally
#create a print function that allows printing from the commandline
#if no board isn't provided use the default board  " ooo |ppp q |xx qa|rrr qa|b c dd|b c ee"

class BOARD:
	def __init__(self, inputString = "  o aa|  o   |xxo   |ppp  q|     q|     q"):
		#"  o aa|  o   |xxo   |ppp  q|     q|     q"
		if type(inputString)==list:
			self.inputString= inputString
		else:
			t = inputString.split('|')
			sArray = []
			row = 0
			while (row <=7):
				if row == 0 or row == 7:
					sArray.insert(row,' ------ ')
				else:
					#row 1 - 6
					if row is not 3:
						sArray.insert(row,"|" + t[row-1] + "|")
					elif row == 3:
						sArray.insert(row, "|" + t[row-1] + " ")
				row += 1
			self.inputString = sArray


#-------------------------------------------------------------------------------------------------------
	#print the given/default board

	def printfunction(self, finalArray=[]):
		a = 0
		x = len(finalArray)

		if x == 0:
			row = 0
			finalArray=self.inputString
			#print(sArray)
			while (row<= 7):
				print(finalArray[row])
				row+=1

		while a<8:
			for i in range(len(finalArray)):
				if i < (x-1):
					print(finalArray[i][a], end= "")
				elif i == (x-1) :
					print(finalArray[i][a])
			a +=1 
	
	




	#a function that checks if row ==3 then if position column 5,6 is 'x'  and 7th position column is " "
	#return true if condition applies else false

	def donefunction(self, sArray = []):
		if len(sArray) == 0:
			sArray = self.inputString

		if sArray[3][5] == 'x' and sArray[3][6]=='x':
			return True
		return False
	

#-----------------------------------------------------------------------------------------------------------------------------------------------

#THE BOARD INFORMATION: 8*8 dimension.
#" ------- " [0][0]-[0][7] && all till  [7][0]-[7][7]
#Board Data = [1][1]-[1][6] && all till [6][1]-[6][6]
#To win - xx needs to be at [3][5] & [3][6]

#------------------------------------------------------------


#returns a list of unique cars in the board

	def eachCar(self):
		sArray = self.inputString
		carArray = []
		for i in range(len(sArray)):
			for car in range(len(sArray[i])):
				if (sArray[i][car] is not '|') and (sArray[i][car] is not '-') and (sArray[i][car] is not ' ') and (sArray[i][car] not in carArray):
					carArray.append(sArray[i][car])
		return carArray


#Create all the possible board for all the posible cars one after another, stores the boards in an array and returns

	def bBoard(self,car,carMovement):
		cloneBoard = copy.deepcopy(self.inputString)
		eachBoard= []
		
		if carMovement[0] == 'Horizontal':
			constantRow = carMovement[1]
			rowArray = []
			for i in range(len(cloneBoard[constantRow])):
				rowArray.append(cloneBoard[constantRow][i])
			iColumnS = carMovement[2]
			iColumnE = carMovement[3]
			fColumnS = carMovement[4]
			fColumnE = carMovement[5]
			column = iColumnS

			while column <= iColumnE:
				if column>= iColumnS and column<=iColumnE:
					rowArray[column]= " "

				column+=1
			
			column = fColumnS
			while column<= fColumnE:
				if column >= fColumnS and column <= fColumnE:
					rowArray[column]= car
				column +=1

			rowArray=''.join(rowArray)
			cloneBoard[constantRow]=rowArray


			row = 0
			eachBoard.append(cloneBoard)
		
		if carMovement[0] == 'Verticle':
			rowArray = []
			columnArray = []
			constantColumn = carMovement[1]
			iRowS = carMovement[2]
			iRowE = carMovement[3]
			fRowS = carMovement[4]
			fRowE = carMovement[5]

			tryArray= []

			for i in range(len(cloneBoard)):
				rowArray.append(cloneBoard[i])
			
			for i in range(len(rowArray)):
				columnArray.append(rowArray[i][constantColumn])
			

			row = iRowS
			while row <= iRowE:
				if row>= iRowS and row <=iRowE:
					columnArray[row]=" "

				row+=1
			
			row = fRowS
			while row<= fRowE:
				if row  >= fRowS and row <= fRowE:
					columnArray[row]= car
				row +=1

			compositeArray = []
			for i in range(len(cloneBoard)):
				compositeArray.append(list(cloneBoard[i]))


			for i in range(len(compositeArray)):
				compositeArray[i][constantColumn]=columnArray[i]

			finalArray = [None] * len(compositeArray)
			for i in range(len(compositeArray)):
				finalArray[i] = "".join(compositeArray[i])
			eachBoard.append(finalArray)
		return eachBoard


	#create all position next boards for ALL posible cars in the board.
	def next(self):
		#the list of cars are stored in carArray
		carArray = self.eachCar()
		finalArray = []
		for car in range(len(carArray)):
			carMovement = self.next_for_car(carArray[car])
			for x in range(len(carMovement)):
				returnBoard = self.bBoard(carArray[car],carMovement[x])
				finalArray.append(returnBoard)
		finalArray = self.stripify(finalArray)
		return(finalArray)
	
	
	def stripify(self, finalArray):
		cc= []
		for i in range(len(finalArray)):
			cc.append(finalArray[i][0])
		return(cc)

	

	def next_for_car(self,car):
		
		carInformation = self.carInformation(car)
		#([startIndex, endIndex, finalrow/col, lastrow/column ,firstrow/column, dimension])
		startIndex = carInformation[0]
		endIndex = carInformation[1]
		dimension = carInformation[5]

		carArray= self.eachCar()


		if dimension == 'Horizontal':
			constantrow = carInformation[2]
			defaultlastcolumn = carInformation[3]
			firstcolumn = carInformation[4]
		else:
			lastrow = carInformation[2]
			constantcolumn = carInformation[3]
			defaultfirstrow = carInformation[4]

		
		sArray = self.inputString
	
		carMovement = []
		if dimension == 'Horizontal':
			rlastcolumn = defaultlastcolumn
			#move right
			ii  = 0
			while (rlastcolumn <= 5) and (sArray[constantrow][rlastcolumn+1] not in carArray):
			
				ii += 1
				finalColumnS = firstcolumn + ii
				finalColumnE = rlastcolumn+1
				carMovement.append([dimension, constantrow, firstcolumn,defaultlastcolumn,finalColumnS,finalColumnE])
				rlastcolumn +=1
				
			

			#Move left
			iii = 0
			llastcolumn = defaultlastcolumn
			while (firstcolumn >= 2) and (sArray[constantrow][firstcolumn-1] not in carArray):
				
				iii = iii - 1
				
				finalColumnS= firstcolumn -1
				finalColumnE = llastcolumn + iii
				carMovement.append([dimension, constantrow, firstcolumn,defaultlastcolumn,finalColumnS,finalColumnE])
				firstcolumn -= 1

		elif dimension == 'Verticle':
			ufirstrow = defaultfirstrow
			#move up
			
			ii  = 0
			while (ufirstrow >= 2) and (sArray[ufirstrow-1][constantcolumn] not in carArray):
				
				ii -= 1
				
				finalRowS = ufirstrow-1
				finalRowE = lastrow + ii
				carMovement.append([dimension, constantcolumn,defaultfirstrow,lastrow,finalRowS,finalRowE])
				ufirstrow -= 1

			#move down
			dfirstrow = defaultfirstrow
			iii  = 0
			while (lastrow <= 5) and (sArray[lastrow+1][constantcolumn] not in carArray):
			
				iii += 1
				finalRowS = dfirstrow+iii
				finalRowE = lastrow + 1
				carMovement.append([dimension, constantcolumn,defaultfirstrow,lastrow,finalRowS,finalRowE])
				lastrow += 1


		return (carMovement)
				



#create a function carInformation(start index, end index, row, column, Horizontal/Verticle)
#loop through each row, column in inputString board
	#if inputString[row,column] == car and inputString[row, column+1= == car,
		#start_index = [row][column]
		#while inputString[row,column] == car:
			#endindex = [row][column]
			#column+=1
			#return(startindex,end index, row, column, horizontal)

	#if inputString[row,column] == car and inputString[row+1, column= == car,
		#start_index = [row][column]
		#while inputString[row,column] == car:
			#endindex = [row][column]
			#row+=1
			#return(startindex,end index, row, column, verticle)


	def carInformation(self, car):
		#return (start index, end index, row(start), column(start), dimension(H/V))
		sArray = self.inputString
		for row in range(len(sArray)):
			for column in range(len(sArray[row])):
				
				
				if (sArray[row][column] == car) and (sArray[row][column+1] == car):
					dimension = 'Horizontal'
					startIndex = "[" + str(row) +"]" + "[" +  str(column) + "]"
					finalrow = row
					firstcolumn = column
					while sArray[row][column]== car:
						endIndex = "[" + str(row)+ "]" + "[" +str(column) + "]"
						column +=1
					return ([startIndex, endIndex, finalrow, (column-1),firstcolumn, dimension])
				
				
				
				elif (sArray[row][column] == car) and (sArray[row+1][column] == car):
					dimension = 'Verticle'
					startIndex = "[" + str(row) +"]" + "[" +  str(column) + "]"
					finalcolumn = column
					firstrow = row
					while sArray[row][column] == car:
						endIndex = "[" + str(row) +"]" + "[" +  str(column) + "]"
						row +=1
					return ([startIndex, endIndex, (row-1), finalcolumn, firstrow,  dimension])
#------------------------------------------------------------------------------------------------------------------------------------------------------

	def random(self):
		n = 0
		randomList = []
		while n <10 and (self.donefunction() == False):
			nextArray = self.next()
			lenNextArray = len(nextArray)
			randomIndex = random.randint(0,lenNextArray-1)
			self.inputString = nextArray[randomIndex]
			randomList.append(self.inputString)
			n +=1

		return(randomList)
		#self.printfunction(randomList)
	
	#do a bfs from a given board and returns the first path found that returns donefunction == True
	#the output should print the path examined at each step and then prints the solution path together 6 one line, rest the next line format(path print)


	#change nodes to PATH
	def bfs(self, problemB =[]):
		if len(problemB) == 0:
			problemB = self.inputString
		
		#the state is each board, node is a list of boards(we can consider our node as anything we want)
		path = Path(problemB)
		node = path.getPath()
		countB = 1
	
		#nodelast = node[len(node)-1]
		nodelast = path.last()
		if self.donefunction(nodelast) == True:
			return(node)
	
		#a FIFO queue with node as the only element
		#frontier is a list of list
		frontier = []
		frontier.insert(0, path)
		#visited nodes(list of list)
		explored = []
		i = 0
		while len(frontier) != 0:
			currentPath = frontier.pop(0)
			lastCPB = currentPath.last()

			currentPath.pathPrintFunction()
			if self.donefunction(lastCPB) == True:
				print(countB)
				break

			self.inputString = lastCPB
			actions = self.next()
			
			for action in range(len(actions)):
				child = actions[action]
				if child not in explored:
					x = path.clone()
					x.add(child)
					frontier.append(x)
					explored.append(child)
			countB += 1

	def heuristic(self, findBoardHeuristic):
		#if sArray[3][5] == 'x' and sArray[3][6] == 'x':
		for row in range(len(findBoardHeuristic)):
			for col in range(len(findBoardHeuristic)):
				if findBoardHeuristic[row][col]=="x":
					heuristic = 5 - col
					return(heuristic)

	def aStar(self, problemB=[]):
		if len(problemB) == 0:
			problemB = self.inputString

		frontier = []
		explored = []

		path = PathAStar()
		nodeBoard = Node(problemB)
		nodeBoard.h = self.heuristic(problemB)
		nodeBoard.g = 0
		nodeBoard.f = nodeBoard.h + nodeBoard.g

		path.add(nodeBoard)
		frontier.append(path)
		countB = 1

		while len(frontier) != 0:
			currentNode = frontier[0].last()
			boardIndex = self.getLowestF(frontier, currentNode)
			n = frontier.pop(boardIndex)
			n = n.last()
			#print(n.board)

			for i in n.board:
				 print(i)


			tryboard = n.board


			if self.donefunction(n.board) == True:
				print(countB)
				break

			explored.append(n.board)
			self.inputString = n.board
			for m in self.next():
				newBoard = BOARD(m)
				if m not in explored:
					newNode = Node(m)
					newNode.h = self.heuristic(newBoard.inputString)
					newNode.g = newNode.getG() + 1
					newNode.f = newNode.h + newNode.g
					x = path.clone()
					x.add(newNode)
					frontier.append(x)
					explored.append(newBoard.inputString)
			countB += 1



	def getLowestF(self, frontier, currentNode):
		current = currentNode
		lowestIndex = 0
		for i in frontier:
			nodeF = i.last()
			if nodeF.f < current.f:
				current = nodeF
				lowestIndex += 1
		return lowestIndex



	def sortfinalqueueH(self, finalqueueH):
		return(sorted(finalqueueH, key=lambda finalqueueH: finalqueueH[1]))



class Node:
	def __init__(self, board= []):
		self.board = board;
		self.h = 0;
		self.g = 0
		self.f = 0
	def getG(self):
		return self.g
	def heuristicCalculation(self, findBoardHeuristic):
		#if sArray[3][5] == 'x' and sArray[3][6] == 'x':
		for row in range(len(findBoardHeuristic)):
			for col in range(len(findBoardHeuristic)):
				if findBoardHeuristic[row][col]=="x":
					heuristic = 5 - col
					print(heuristic)
					return(heuristic)

					

#-------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	##check if arg 2 is given if given, initiate the board class by passing that value
	##the script passes 3 arguments, thus check if len(argument) ==3,to initiate the class with the value passed in the argument 2 as index of argument is len(argument)-1
	#bfs = x.bfs()
	#aStar = x.aStar(i)
	#path = Path()
	if len(sys.argv) == 3:
		x  = BOARD(sys.argv[2])
	else:
		x = BOARD()

	if sys.argv[1] == 'print':
		x.printfunction()

	if sys.argv[1] == 'done':
		print(x.donefunction())

	if sys.argv[1] == 'next':
		finalArray = x.next()
		x.printfunction(finalArray)
	
	if sys.argv[1] == 'random':
		r = x.random()
		x.printfunction(r)

	if sys.argv[1] == 'bfs':
		x.bfs()

	if sys.argv[1] == 'astar':
		x.aStar()
