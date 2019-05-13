import os, time
from copy import deepcopy

#The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells,
# each of which is in one of two possible states, alive or dead. Every cell interacts with its
# eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
# At each step in time, the following transitions occur:

# - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# - Any live cell with two or three live neighbours lives on to the next generation.
# - Any live cell with more than three live neighbours dies, as if by overcrowding.
# - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#The initial pattern constitutes the seed of the system. The first generation is created by
# applying the above rules simultaneously to every cell in the seed—births and deaths occur
# simultaneously, and the discrete moment at which this happens is sometimes called a tick (in
# other words, each generation is a pure function of the preceding one)


seed = """
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
------------------------------------x-------------------------------------
-----------------------------------x-x------------------------------------
----------------------------------x---x-----------------------------------
---------------------------------x--x--x----------------------------------
--------------------------------x--xxx--x---------------------------------
---------------------------------x--x--x----------------------------------
----------------------------------x---x-----------------------------------
-----------------------------------x-x------------------------------------
------------------------------------x-------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
"""

# --------x-x----------
seedSmall = """---------------------
--------x-x----------
---------x-----------
---------------------"""

#print(seed)

# storage structures: list of lists, dict, object
# for each line in seed, assign each character to a list
# split on characters, split on line breaks

__alive__ = "x"
__dead__ = "-"
world = []
# line = []
# linenumber = 1
# cellnumber = 1

def main():
	# global cell
	# global line
	# global linenumber
	# global cellnumber

	seedTheWorld()
	print("\nworld dimensions: {} x {}".format(len(world), len(world[0])))
	# print(world)
	alive = 1
	while alive > 0:
		alive = runTheWorld()
		time.sleep(1)
		os.system("clear")


	# TODO: store the coordinates of every living cell

# we could store coordinates for every single cell, or we could only store coordinates for cells that are alive.
# if we just keep a list of live cells, we could check current cell coordinates against the cells in the list

# current cell coordinates: current position (line number, column number)
# coordinate list = mapOfTheLiving={7:[14,15],8:[13]}
	# current cell = line 7, cell 14
	# are any alive in line 6 or 8?

	# TODO: loop through the world until every cell is dead
	# TODO: clear the screen and print each iteration of the world
	# TODO: count every iteration
	# TODO: count how many are alive in each iteration

	# for cell in seedSmall:
	# 	# evaluateCell(linenumber, cellnumber)
	# 	status = evaluateCell(cell)
	# 	print(cell, end='')
	# 	if cell == '\n':
	# 		world.append(line)
	# 		line = []
	# 		linenumber += 1
	# 		cellnumber = 1
	# 	else:
	# 		line.append({cellnumber:status})
	# 		cellnumber += 1

def runTheWorld():
	newWorld = deepcopy(world)
	totalLiving = 0
	for linenumber, line in enumerate(world):
		for cellnumber, cellstatus in enumerate(line):
			if cellstatus == __alive__:
				totalLiving += 1
			newStatus = evaluateCell(linenumber, cellnumber, cellstatus)
			# write results to newWorld
			newWorld[linenumber][cellnumber] = newStatus
			print(newStatus, end='')
		print()

	# world = deepcopy(newWorld)
	return totalLiving

# def evaluateCell(line, cell):
def evaluateCell(linenumber, cellnumber, cellstatus):
	surroundingCount = countSurroundingCells(linenumber, cellnumber)
	# print("surrounding cell count: {}".format(surroundingCount))
	# print("line#:{0}, cell#:{1}, status:{2}, surroundingCount: {3}".format(linenumber, cellnumber, cellstatus, surroundingCount))
	# print("cellstatus: {}, __alive__: {}, __dead__: {}, cell is alive: {}".format(cellstatus, __alive__, __dead__, cellstatus == __alive__))
	if cellstatus == __alive__:
		# - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
		if surroundingCount < 2:
			return __dead__
		# - Any live cell with two or three live neighbours lives on to the next generation.
		elif surroundingCount == 2 or surroundingCount == 3:
			return __alive__
		# - Any live cell with more than three live neighbours dies, as if by overcrowding.
		elif surroundingCount > 3:
			return __dead__

	else:
		# - Any dead cell with exactly three live neighbours becomes a live cell
		# count surrounding cells
		# if count == 3, cell becomes alive
		if surroundingCount == 3:
			return __alive__
		else:
			return __dead__

def countSurroundingCells(linenumber, cellnumber):
	# count living cells around this cell, in other words, how many are True?
	# first we need to test line and cell size
	# if line is 0, there is no need to check above
	# if line is at len(world), there is not need to check below
	# if cell is at 0, there is no need to check left
	# if cell is at len(line), there is no need to check right

	numberOfLivingCells = 0
	if linenumber > 0 and cellnumber > 0 and world[linenumber-1][cellnumber-1] == "x":
		numberOfLivingCells += 1

	if linenumber > 0 and world[linenumber-1][cellnumber] == "x":
		numberOfLivingCells += 1

	if linenumber > 0 and cellnumber < len(world[linenumber])-1 and world[linenumber-1][cellnumber+1] == "x":
		numberOfLivingCells += 1

	if cellnumber > 0 and world[linenumber][cellnumber-1] == "x":
		numberOfLivingCells += 1

	if cellnumber < len(world[linenumber])-1 and world[linenumber][cellnumber+1] == "x":
		numberOfLivingCells += 1

	if linenumber < len(world)-1 and cellnumber > 0 and world[linenumber+1][cellnumber-1] == "x":
		numberOfLivingCells += 1

	if linenumber < len(world)-1 and world[linenumber+1][cellnumber] == "x":
		numberOfLivingCells += 1

	if linenumber < len(world)-1 and cellnumber < len(world[linenumber])-1 and world[linenumber+1][cellnumber+1] == "x":
		numberOfLivingCells += 1

	# topleft = linenumber-1, cellnumber-1
	# topmiddle = linenumber-1, cellnumber
	# topright = linenumber-1, cellnumber+1
	# left = cellnumber-1
	# right = cellnumber+1
	# bottomleft = linenumber+1, cellnumber-1
	# bottommiddle = linenumber+1, cellnumber
	# bottomright = linenumber+1, cellnumber+1
	# print("{}:{} = world[{}][{}]".format(linenumber, cellnumber, linenumber, cellnumber-1))
	return numberOfLivingCells


def seedTheWorld():
	line = []
	print("seedsize:", len(seedSmall))
	for index, cell in enumerate(seedSmall):
		print(cell, end='')
		if cell == '\n':
			world.append(line)
			line = []
		else:
			line.append(cell)
	world.append(line) # get the last line


if __name__ == '__main__':
	main()

