input = open('day2_input.txt', 'r')
lines = input.readlines()

hor_pos = 0
depth = 0
aim = 0

for line in lines:
	instructions = line.split()
	if (instructions[0] == "forward"):
		hor_pos = hor_pos + int(instructions[1])
		depth = depth + (aim * int(instructions[1]))
	if (instructions[0] == "up"):
		aim = aim - int(instructions[1])
	if (instructions[0] == "down"):
		aim = aim + int(instructions[1])

print("Horizontal position: " + str(hor_pos))
print("Depth: " + str(depth))
print("Aim: " + str(aim))

result = hor_pos * depth
print("Result: " + str(result))