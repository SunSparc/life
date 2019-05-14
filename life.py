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


seedDefault = """--------------------------------------------------------------------------
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
--------------------------------------------------------------------------"""

# --------x-x----------
seedSmall = """---------------------
--------x-x----------
---------x-----------
---------------------"""


__alive__ = "x"
__dead__ = "-"
world = []

def main():
	seed = acquireSeed()
	seedTheWorld(seed)
	print("\nseedsize:", len(seed))	
	print("world dimensions: {} x {}".format(len(world), len(world[0])))
	# TODO: refresh only the world map, not the whole screen, if possible
	os.system("clear")
	lifeCycle = 1
	alive = 1
	while alive > 0:
		# TODO: watch for lack of change, if nothing changes for a couple of cycles, end the program
		print("Current life cycle: {}, number of living: {}".format(lifeCycle, alive))
		alive = runTheWorld()
		time.sleep(1)
		os.system("clear")
		lifeCycle += 1

def runTheWorld():
	global world
	newWorld = deepcopy(world)
	totalLiving = 0
	for linenumber, line in enumerate(world):
		for cellnumber, cellstatus in enumerate(line):
			if cellstatus == __alive__:
				totalLiving += 1
			newStatus = evaluateCell(linenumber, cellnumber, cellstatus)
			newWorld[linenumber][cellnumber] = newStatus
			print(newStatus, end='')
		print()

	world = deepcopy(newWorld)
	return totalLiving

def evaluateCell(linenumber, cellnumber, cellstatus):
	surroundingCount = countSurroundingCells(linenumber, cellnumber)
	if cellstatus == __alive__:
		if surroundingCount < 2:
			return __dead__
		elif surroundingCount == 2 or surroundingCount == 3:
			return __alive__
		elif surroundingCount > 3:
			return __dead__

	else:
		if surroundingCount == 3:
			return __alive__
		else:
			return __dead__

def countSurroundingCells(linenumber, cellnumber):
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
	return numberOfLivingCells


def seedTheWorld(seed):
	line = []
	for index, cell in enumerate(seed):
		print(cell, end='')
		if cell == '\n':
			world.append(line)
			line = []
		else:
			line.append(cell)
	world.append(line) # get the last line


def acquireSeed():
# TODO: read the seed from a file, if no file offered, use a default seed
	return seedDefault


if __name__ == '__main__':
	try:
		main()
	except (KeyboardInterrupt, SystemExit):
		print("The End")
		exit()


