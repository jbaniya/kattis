input = map(int, raw_input().split())
people = input[0]
problems = input[1]

names = [ 0 for k in range(0, people)]
for i in range(0, people):
	names[i] = raw_input()
	
print problems