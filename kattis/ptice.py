input = int(raw_input()) # 5
string = raw_input()

countA = 0
countB = 0
countG = 0

adrian = [ 'A', 'B', 'C' ]
bruno = [ 'B', 'A', 'B', 'C' ]
goran = [ 'C','C','A','A', 'B', 'B' ]

i = 0
for letter in string:
	if(letter == adrian[i % 3]):
		countA += 1
	if(letter == bruno[i % 4]):
		countB += 1
	if(letter == goran[i % 6]):
		countG += 1
	i += 1
		
winner = max(countA, countB, countG)
print winner

if(winner == countA):
	print 'Adrian'
	
if(winner == countB):
	print 'Bruno'
	
if(winner == countG):
	print 'Goran'