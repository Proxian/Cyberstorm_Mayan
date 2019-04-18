##############################################################################
#									     #
#  Team:  Mayans							     #
#  Names: Dawson Markham, Justin Bethelot				     #
#  Date:  5/3/2019							     #
#									     #
#  Description: Program takes user input and can hide a file or extract a    #
# 		 file using either bit or byte steganography.		     #
##############################################################################

# LIBRARIES
import sys

# CONSTANTS
SENTINEL    = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
BIT_METHOD  = False
BYTE_METHOD = True
DEBUG       = False
EXTRACT     = True

# VARIABLES
offset   = 1024
interval = 8
wrapper  = "test_result"
hidden   = "test_hide"

# FUNCTIONS

# Bit Method
def bitMethod():
	
	# Check extraction mode
	if EXTRACT:

		# Open and read file
		wrap_file = open(wrapper, 'r')
		wrap_byte = []

                while True:
                        tmp = wrap_file.read(1)
							        
                        if not tmp:
	                        break
	                wrap_byte.append(tmp)
		
		wrap_file.close()

		# Set counters and buffer
		i = offset
		j = k = m = 0
		out_buffer = [0,0,0,0,0,0]

		# Extract the last bit from every byte as specified by variables
		while (i < len(wrap_byte)):
			tmp = 0x0		# Set counter and tmp variab;e
			k = 0
			for k in range(0,8):
				tmp |= ((ord(wrap_byte[i]) & 0b00000001) << (7-k)) # Add bit to correct location
				i += interval
			
			# Check if enough cycles have been completed to fill the buffer
			if (i > offset + 6*(8*interval)):
				sys.stdout.write(chr(out_buffer[m]))

			# Store in buffer
			out_buffer[m] = tmp

			# DETECT SENTINEL
			if (out_buffer[m] == SENTINEL[j]): # Check if correct sentinel byte has been detected
				j+=1
                                if DEBUG:
					print "here"
                                if (j == 6):		   # Break if sentinel has been found
                                        break
                        else:				   # Else, reset search	
                                if DEBUG:
                                        if (j>0):
	                                       print "reset"
				j=0
			
			# Update buffer variables
			m += 1
			m %= 6

	# Hide file
	else:
		# Open wrap and hidden files and stroe in list
		wrap_file = open(wrapper, 'r')
		wrap_byte = []

		hide_file = open(hidden, 'r')
		hide_byte = []

		while True:
			tmp = wrap_file.read(1)
			
			if not tmp:
				break

			wrap_byte.append(tmp)

		while True:
			tmp = hide_file.read(1)
				
			if not tmp:
				break
			
			hide_byte.append(ord(tmp))
		
		wrap_file.close()
		hide_file.close()


		# Add sentinel to end of hidden file list
		i = 0
		for i in range(0, len(SENTINEL)):
			hide_byte.append(SENTINEL[i])
		
		# Set counters
		i = offset
		j = 0
		for j in range(0, len(hide_byte)):
			# Get each bit of hidden byte and store in the ends of bytes in the wrapper
			k = 0
			for k in range(0, 8):
				tmp = ord(wrap_byte[i]) & 11111110			
				wrap_byte[i] = chr(tmp | ((hide_byte[j] & 10000000) >> 7))
				hide_byte[j] <<= 1
				i += interval
		
		# Output edited file
		i = 0
		for i in range(0, len(wrap_byte)):
			sys.stdout.write(wrap_byte[i])

# Byte Method
def byteMethod():
	
	# Check extraction mode
	if EXTRACT:
		# Open file and store contents
		wrap_file = open(wrapper, 'r')
		wrap_byte = []

		while True:
			tmp = wrap_file.read(1)
			
			if not tmp:
				break

			wrap_byte.append(tmp)
		
		wrap_file.close()

		# Set counters and buffer
		i = j = m = 0
		out_buffer = [0,0,0,0,0,0]

		# Find and output the hidden bytes as specified by variables
		for i in range(offset,len(wrap_byte), i + interval):
			if (i >= offset + 6*interval):		# Check if buffer has been filled
				sys.stdout.write(out_buffer[m])
			
			out_buffer[m] = wrap_byte[i] 	# Buffer to prevent sending sentinel bytes

			# SENTINEL DETECTION
			if (ord(out_buffer[m]) == SENTINEL[j]): # Check if next sentinel byte has been sent
				j+=1
				if DEBUG:
					print "here"
				if (j == 6):		# Break if entire sentinel has been sent
					break
			else:				# Else, reseet search
				if DEBUG:
					if (j>0):
						print "reset"
				j=0

			# Update buffer variables
			m += 1
			m %=6

	# Else, hide file
	else:
		# Open and stroe wrapper and hidden files
		wrap_file = open(wrapper, 'r')
		hide_file = open(hidden, 'r')

		wrap_byte = []
		hide_byte = []

		while True:
			tmp = wrap_file.read(1)

			if not tmp:
				break

			wrap_byte.append(tmp)

		while True:
			tmp = hide_file.read(1)

			if not tmp:
				break

			hide_byte.append(tmp)

		wrap_file.close()
		hide_file.close()

		# Store the bytes of hidden file within wrapper
		i = 0
		o = offset
		for i in range(0, len(hide_byte)):
			wrap_byte[o] = hide_byte[i]
			o += interval

		# Store sentinel after hidden file
		i = 0
		for i in range(0, len(SENTINEL)):
			wrap_byte[o] = chr(SENTINEL[i])
			o += interval
		
		# Output new file
		i = 0
		for i in range(0, len(wrap_byte)):
			sys.stdout.write(wrap_byte[i])

# Check the method requested
if BIT_METHOD:
	bitMethod()

elif BYTE_METHOD:
	byteMethod()

else:
	print "Mode not recognized"
