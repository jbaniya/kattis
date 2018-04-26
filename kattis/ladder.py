import math

input = map( int, raw_input().split())
ladder = input[0] / math.sin( input[1] /180.0 * math.pi )
print int(ladder + 0.999999)	
