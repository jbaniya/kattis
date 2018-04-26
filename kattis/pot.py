input = int(raw_input())

final = 0

for i in range(0, input):
    num1 = int(raw_input())
    mod1 = num1 % 10
    num1 = num1 / 10 
    final = final + (num1 ** mod1) 
print final