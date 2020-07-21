# Author: Rocky Mazorow
# Date: 12/16/2019

# You're starting to sweat as the ship makes its way toward Mercury. The Elves suggest that you get the air conditioner working by upgrading your ship computer to support the Thermal Environment Supervision Terminal. The Thermal Environment Supervision Terminal (TEST) starts by running a diagnostic program (your puzzle input). The TEST diagnostic program will run on your existing (Day 2) Intcode computer after a few modifications:

# First, you'll need to add two new instructions:
# 		Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
# 		Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.

# Second, you'll need to add support for parameter modes:
# 		Each parameter of an instruction is handled based on its parameter mode. Right now, your ship computer already understands parameter mode 0, position mode, which causes the parameter to be interpreted as a position - if the parameter is 50, its value is the value stored at address 50 in memory. Until now, all parameters have been in position mode.
# 		Now, your ship computer will also need to handle parameters in mode 1, immediate mode. In immediate mode, a parameter is interpreted as a value - if the parameter is 50, its value is simply 50.
# 		Parameter modes are stored in the same value as the instruction's opcode. The opcode is a two-digit number based only on the ones and tens digit of the value, that is, the opcode is the rightmost two digits of the first value in an instruction. Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.

# The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an input instruction - provide it 1, the ID for the ship's air conditioner unit. It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, like parameter modes, function correctly. For each test, it will run an output instruction indicating how far the result of the test was from the expected value, where 0 means the test was successful. Non-zero outputs mean that a function is not working correctly; check the instructions that were run before the output instruction to see which one failed. Finally, the program will output a diagnostic code and immediately halt. This final output isn't an error; an output followed immediately by a halt means the program finished. If all outputs were zero except the diagnostic code, the diagnostic program ran successfully.

# After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program produce?

f = open('Day5.txt', 'r')
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