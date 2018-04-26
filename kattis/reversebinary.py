input = int( raw_input() ) 
bin_string = "{0:b}".format(input)
reverse = bin_string[::-1]
print int(reverse, 2)
		