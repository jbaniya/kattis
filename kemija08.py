import sys
input = raw_input()
vowels = [ 'a', 'e', 'i', 'o', 'u']

i = 0
while(i < len(input)):
	k = 0
	sys.stdout.write(str(input[i]))
	for k in range(0,5):
		if input[i] == vowels[k]:
			i = i + 2
	i = i + 1
	