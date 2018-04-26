import sys
list = [ 1, 1, 2, 2, 2, 8 ]

chessPieces = map(int, raw_input().split())

newList = [0 for i in range(0, 6)]

for i in range(0, 6):
		newList[i] = list[i] - chessPieces[i]
		sys.stdout.write(str(newList[i]) + " ")