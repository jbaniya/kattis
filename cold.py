num = int(raw_input())
list = map(int, raw_input().split())
count = 0
for i in range(0, num):
	if list[i] < 0:
		count += 1
print count