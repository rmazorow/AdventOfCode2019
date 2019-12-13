# Author: Rocky Mazorow
# Date: 12/12/2019

# The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

# Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

# The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

# What is the Manhattan distance from the central port to the closest intersection?

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
	
	for p1 in wire1:
		for p2 in wire2:
			if (p1 in p2):
				cross.append(int(calcDist(p1)))
	return cross

def calcDist(path):
	path = path.replace('(', ' ')
	path = path.replace(')', ' ')
	path = path.replace(',', ' ')
	path = path.split()
	
	return (abs(int(path[0])) + abs(int(path[1])))
	
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

print("The Manhattan distance from the central port to the closest intersection is: ", min(cross))