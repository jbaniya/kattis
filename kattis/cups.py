input = int(raw_input())
radiusList = []
colors = []

for i in range(0, input):
    robot = raw_input();
    color = ""
    radius = ""
    if(ord(robot[0]) >= 97 and ord(robot[0]) <=122):
        for letter in  robot:
            if ord(letter) >= 48 and ord(letter) <= 57:
                radius = radius + letter
            else:
                if(ord(letter) != 32):
                    color = color + letter
        
        radiusNum = int(radius)
        radiusList.append(radiusNum)
        colors.append(color)
    else:
        for letter in  robot:
            if ord(letter) >= 48 and ord(letter) <= 57:
                radius += letter
            else:
                if(ord(letter) != 32):
                    color = color + letter
        
        radiusNum = int(radius)/2
        radiusList.append(radiusNum)
        colors.append(color)
            
def sortList(radiusList, colorList, total):
    i = 0
    for i in range(0,total-1):
        j = 0
        for j in range (0, total - 1):
            if(radiusList[j] > radiusList[j+1]):
                radiusList[j],radiusList[j+1] = radiusList[j+1], radiusList[j] 
                colors[j], colors[j+1] = colors[j+1],colors[j]
                            
sortList(radiusList, colors, input)

for i in range(0, input):
    print colors[i]