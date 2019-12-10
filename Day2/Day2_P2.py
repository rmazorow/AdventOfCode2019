# Author: Rocky Mazorow
# Date: 12/10/2019

# To complete the gravity assist, you need to determine what pair of inputs produces the output 19690720."

#The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before. In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

#Once the program has halted, its output is available at address 0, also just like before. Each time you try a pair of inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

#Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)

def start(opCodes, seek):
	for noun in range(100):
		for verb in range(100):
			copy = opCodes.copy()
			copy[1] = noun
			copy[2] = verb
			if (find(copy) == "19690720"):
				print("The pair of inputs that produce " + seek + " is:")
				print("\tNoun: ", noun)
				print("\tVerb: ", verb)
				return (100 * noun + verb)

def find(copy):
	for op in range(0, len(copy), 4):
		if copy[op] == '99':
			break
		else:
			result = int(copy[op + 3])
			math1  = int(copy[op + 1])
			math2  = int(copy[op + 2])
			
			if copy[op] == '1':
				copy[result] = str(int(copy[math1]) + int(copy[math2]))
			elif copy[op] == '2':
				copy[result] = str(int(copy[math1]) * int(copy[math2]))
			else:
				print("ERROR: Not valid opcode [" + copy[op] + "]")
	return copy[0]
	
f = open('Day2.txt', 'r')
instruct = f.read()

opCodes  = instruct.split(",")
		
print("100 * noun + verb = ", start(opCodes, "19690720"))