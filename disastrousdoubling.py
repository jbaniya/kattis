# your code goes here

n = int(raw_input())
arr = map(int, raw_input().split())

v = 1
for i in range(n):
	v = v + v - arr[i]
	if v < 0:
		print "error"
		exit()

print v % 1000000007