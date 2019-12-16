# Author: Rocky Mazorow
# Date: 12/13/2019

# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

# However, they do remember a few key facts about the password:
#		It is a six-digit number.
#		The value is within the range given in your puzzle input.
#		Two adjacent digits are the same (like 22 in 122345).
#		Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# Other than the range rule, the following are true:
#		111111 meets these criteria (double 11, never decreases).
#		223450 does not meet these criteria (decreasing pair of digits 50).
#		123789 does not meet these criteria (no double).

# How many different passwords within the range 183564-657474 meet these criteria?

count = 0

for p in range(183564, 657474):
	double = False
	increase = True
	
	p = str(p)
	for i in range(0, 5):
		if p[i+1] < p[i]:
			increase = False
			break 
			
		if p[i] == p[i+1]:
			double = True
	
	if double and increase:
		count +=1

print("There are", count, "passwords that meet these criteria")