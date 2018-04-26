finish = 0
finish = int(raw_input()) 
while(finish != -1):
	
	total = 0
	prev = 0
	for i in range(0,finish):
		array = (map(int, raw_input().split()))
		speed = array[0]
		time = array[1] - prev
		prev = array[1]
		total += speed * time
	print total , 'miles'
	
	finish = int(raw_input())