# Author: Rocky Mazorow
# Date: 12/10/2019

# On the way to your gravity assist around the Moon, your ship computer beeps angrily about a "1202 program alarm". On the radio, an Elf is already explaining how to handle the situation: "Don't worry, that's perfectly norma--" The ship computer bursts into flames.

# You notify the Elves that the computer's magic smoke seems to have escaped. "That computer ran Intcode programs like the gravity assist program it was working on; surely there are enough spare parts up there to build a new Intcode computer!"

# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

# Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

# Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

# Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

f = open('Day2.txt', 'r')
instruct = f.read()

opCodes = instruct.split(",")
op = 0
opCodes[1] = 12
opCodes[2] = 2

for op in range(0, len(opCodes), 4):
	if opCodes[op] == '99':
		break
	else:
		result = int(opCodes[op + 3])
		math1  = int(opCodes[op + 1])
		math2  = int(opCodes[op + 2])
		
		if opCodes[op] == '1':
			opCodes[result] = str(int(opCodes[math1]) + int(opCodes[math2]))
		elif opCodes[op] == '2':
			opCodes[result] = str(int(opCodes[math1]) * int(opCodes[math2]))
		else:
			print("ERROR: Not valid opcode")
	
print("The value in the 0 position is " + opCodes[0])