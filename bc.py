#!/usr/bin/python3
import sys

bases_ = { 'x': 16, 'o': 8, 'd': 10, 'b': 2 }

def comma(intG):
	intG = str(intG)
	offset = len(intG) % 3
	string = ''
	backup = ''
	i = 0
	string += intG[ :offset ] 
	while offset <= len(intG):
		ope = string
		string += intG[ offset - 3:offset ] + ','
		offset += 3
	return string.strip(',')

def conv( value, from_, to_):
    answer = int( value, bases_[from_])

    if to_ == 'x':
    	print('hex: ', end='')
    	return hex(answer)
    elif to_ == 'b':
    	print(f'bin, {len(bin(answer)) - 2} bits: ', end='')
    	return bin(answer)
    elif to_ == 'o':
    	print('octal: ', end='')
    	return oct(answer)
    return '{:,}'.format(answer) 

if sys.argv[1] == 'bit':
	no = sys.argv[2]	
	b_ = '1' * int(no)
	b_to = sys.argv[3]
	b_from = 'b'
elif len(sys.argv) < 2:
    print("You didn't put enough arguments")
    sys.exit()
elif len(sys.argv) > 3:
    b_from = sys.argv[1]
    b_to  = sys.argv[2]
    b_ = sys.argv[3]
elif len(sys.argv) == 2:
	b_from = 'x'
	b_to = 'd'
	b_ = sys.argv[-1]
else:
    b_from = sys.argv[1]
    b_to  = 'd'
    b_ = sys.argv[2]

print(conv(b_, b_from, b_to))

# print(comma(1234567834542524))