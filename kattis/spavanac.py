array = map(int, raw_input().split())
hour = array[0]
minutes = array[1]
new_minutes = minutes - 45
if(new_minutes < 0):
    hour = hour - 1
    if (hour < 0):
        hour = hour + 24
    new_minutes = new_minutes + 60
    
print hour , new_minutes