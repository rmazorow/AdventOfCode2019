# Author: Rocky Mazorow
# Date: 12/13/2019

# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

# Given this additional criterion, but still ignoring the range rule, the following are now true:
# 		112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 		123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
#		 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).

# How many different passwords within the range given in your puzzle input meet all of the criteria?

count = 0

for p in range(183564, 657474):
	double = False
	increase = True

	p = str(p)
	i = 0
	for i in range(5):
		if p[i+1] < p[i]:
			increase = False
			break
		if p[i] == p[i+1]:
			find = str(p[i]) + str(p[i])
			if p.find(find) == p.rfind(find):
				double = True

	if double and increase:
		count += 1

print("There are", count, "passwords that meet these criteria")