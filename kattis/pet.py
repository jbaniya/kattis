
winner_sum = 0
player = 0
for i in range(0,5):
	sum = 0
	input = map(int, raw_input().split())
	for j in range(0,4):
		sum += input[j]
	if (sum > winner_sum):
		winner_sum = sum
		player = i + 1
print player, winner_sum