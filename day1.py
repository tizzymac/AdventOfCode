input = open('day1_input.txt', 'r')
lines = input.readlines()

prev_line = 0
larger_count = 0

for line in lines:
    curr_line = int(line)
    if (curr_line > prev_line):
        larger_count = larger_count + 1
    prev_line = curr_line

print(larger_count - 1)