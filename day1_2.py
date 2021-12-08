input = open('day1_input.txt', 'r')
lines = input.readlines()

sumA = 0
sumB = 0
sumC = 0
sumD = 0
line_num = 0
increases = 0

def comparisons( lhs, rhs, l):
	if (l < 4):
		return
	if (lhs > rhs):
		global increases
		increases += 1

for line in lines:
	line_num += 1
	# 1 -> 2 -> 3 -> 0
	if (line_num % 4 == 1):
		comparisons(sumB, sumA, line_num)
		# print("B: " + str(sumB) + "  A: " + str(sumA))

		sumA = int(line)
		sumC += int(line)
		sumD += int(line)
	if (line_num % 4 == 2):
		comparisons(sumC, sumB, line_num)
		# print("C: " + str(sumC) + "  B: " + str(sumB))

		sumA += int(line)
		sumB = int(line)
		sumD += int(line)
	if (line_num % 4 == 3):
		comparisons(sumD, sumC, line_num)
		# print("D: " + str(sumD) + "  C: " + str(sumC))

		sumA += int(line)
		sumB += int(line)
		sumC = int(line)
	if (line_num % 4 == 0):
		comparisons(sumA, sumD, line_num)
		# print("A: " + str(sumA) + "  D: " + str(sumD))

		sumB += int(line)
		sumC += int(line)
		sumD =  int(line)



print(increases)
	
