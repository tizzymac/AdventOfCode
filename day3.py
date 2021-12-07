input = open('day3_input.txt', 'r')
lines = input.readlines()

l = len(lines[0]) - 1

totals = [0] * l

for line in lines:
	for i in range(0, l):
		totals[i] = totals[i] + int(line[i])

gamma_bin = ""
epsilon_bin = ""
for i in range(0, l):
	if (int(totals[i]) >= len(lines) / 2):
		gamma_bin = gamma_bin + "1"
		epsilon_bin = epsilon_bin + "0"
	else:
		gamma_bin = gamma_bin + "0"
		epsilon_bin = epsilon_bin + "1"

gamma = int(gamma_bin, 2)
epsilon = int(epsilon_bin, 2)

print("Gamma rate in binary: " + gamma_bin)
print("Gamma rate in decimal: " + str(gamma))
print("Epsilon rate in binary: " + epsilon_bin)
print("Epsilon rate in decimal: " + str(epsilon))
print("Power consumption: " + str(gamma * epsilon))
