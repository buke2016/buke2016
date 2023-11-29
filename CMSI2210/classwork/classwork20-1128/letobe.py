# Function to swap a value from
# big Endian to little Endian and
# vice versa.
def swap_Endians(value):

	# Get the rightmost 8 bits of the number
	# by anding it 0x000000FF. since the last
	# 8 bits are all ones, the result will be the 
	# rightmost 8 bits of the number. this will
	# be converted into the leftmost 8 bits for the
	# output (swapping)

	leftmost_byte = (value & eval('0x000000FF')) >> 0

	# Similarly, get the right middle and left 
	# middle 8 bits which will become
	# the left_middle bits in the output

	left_middle_byle = (value & eval('0x0000FF00')) >> 8

	right_middle_byte = (value & eval('0x00FF0000'))>> 16

	# Get the leftmost 8 bits which will be the 
	# rightmost 8 bits of the output

	rightmost_byte = (value & eval('0xFF000000'))>> 24

	# Left shift the 8 bits by 24
	# so that it is shifted to the 
	# leftmost end

	leftmost_byte <<= 24

	# Similarly, left shift by 16
	# so that it is in the left_middle
	# position. i.e, it starts at the
	# 9th bit from the left and ends at the
	# 16th bit from the left

	left_middle_byle <<= 16

	right_middle_byte <<= 8

	# The rightmost bit stays as it is
	# as it is in the correct position

	rightmost_byte <<= 0

	# Result is the concatenation of all these values

	result = (leftmost_byte | left_middle_byle 
				| right_middle_byte | rightmost_byte)


	return result



# main function
if __name__ == '__main__':

	# Consider a hexadecimal value
	# given below. we are gonna convert
	# this from big Endian to little Endian
	# and vice versa.
	big_Endian = eval('0x12345678')
	little_Endian = eval('0x78563412')
	
	result1 = swap_Endians(big_Endian)

	result2 = swap_Endians(little_Endian)

	print("big Endian to little: % s\nlittle Endian to big: % s" %(hex(result1), hex(result2)))
