input = raw_input()

list = [1, 0, 0]

for letter in input:
	if letter == 'A':
		list[0], list[1] = list[1], list[0]
	elif letter == 'B':
		list[1], list[2] = list[2], list[1]
	else:
		list[2], list[0] = list[0], list[2]
		
for i in range(0,3):
	if list[i] == 1:
		print i + 1	