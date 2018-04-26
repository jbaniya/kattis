fortyTwo = [0 for k in range(0,42)]
for i in range(0, 10):
    num = int(raw_input())
    i = num % 42
    fortyTwo[i] += 10
    
count = 0

for j in range (0, 42):
    if(fortyTwo[j] != 0):
        count += 1
print count