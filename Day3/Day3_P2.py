# Author: Rocky Mazorow
# Date: 12/12/2019

# It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

# To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

# The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

# What is the fewest combined steps the wires must take to reach an intersection?

def readWire(path):
	path = path.split(',')
	wire = ""
	x = 0
	y = 0
	
	for p in path:
		if p[0] == 'R':
			for n in range(int(p[1:])):
				x += 1
				wire += "(" + str(x) + "," + str(y) + ") "
		elif p[0] == 'L':
			for n in range(int(p[1:])):
				x -= 1
				wire += "(" + str(x) + "," + str(y) + ") "
		elif p[0] == 'U':
			for n in range(int(p[1:])):
				y += 1
				wire += "(" + str(x) + "," + str(y) + ") "
		elif p[0] == 'D':
			for n in range(int(p[1:])):
				y -= 1
				wire += "(" + str(x) + "," + str(y) + ") "
		
	return wire
	
def compare(wire1, wire2):
	cross = []
	
	wire1 = str(wire1).split()
	wire2 = str(wire2).split()
	
	for p1 in range(len(wire1)):
		for p2 in range(len(wire2)):
			if (wire1[p1] in wire2[p2]):
				steps = p1 + p2 + 2
				cross.append(steps)
	return cross
	
def min(cross):
	min = cross[0]
	
	for r in cross:
		if r < min:
			min = r
	return min
	
f = open('Day3.txt', 'r')
path = f.readline()
wire1 = readWire(path)
path = f.readline()
wire2 = readWire(path)

cross = compare(wire1, wire2)

print("The sum of the shortest number of steps to an intersection is: ", min(cross))