input = raw_input()
t = 0
g = 0
c = 0
for letter in input:
	if(letter == 'T'):
		t += 1
	elif(letter == 'G'):
		g += 1
	elif(letter == 'C'):
		c += 1
extra_points = min(t,g,c)
total = (t ** 2) + (g ** 2) + (c ** 2) + (7 * extra_points)
print total