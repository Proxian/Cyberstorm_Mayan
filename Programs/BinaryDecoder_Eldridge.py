#run with python 3, won't accept input greater than 85 characters otherwise

#Returns a human readable decoded String
def decode(binary, size):
	Done = False
	DCStr = ""
	i = 0
	ascii = 0
	
	for t in range(0, len(binary)-1):
		
		#read bits and add decimal values
		ascii += [0,1][binary[t] == '1'] * pow(2, (size-1) - (t%(size)))
		
		if (t % size == (size-1)):
			#convert from ascii to character and add it to the output string
			if (ascii == 8):
				DCStr = DCStr[0:len(DCStr)-1]
			else:
				DCStr += chr(ascii)
			ascii = 0
	return DCStr


#input from StandardIn
inStr = str(input())

if ( inStr == "exit" or inStr == "EXIT"):
	exit()
x = list(inStr)

#assumes input is strictly 7 or 8 bit-lengths
sevenBit = [False,True][(len(x) % 7) == 0]
eightBit = [False,True][(len(x) % 8) == 0]

if (sevenBit and eightBit):
	y = decode(x, 7)
	z = decode(x, 8)
	print(str(y) + " or " + str(z))
elif (sevenBit):
	z = decode(x, 7)
	print(str(z))
elif(eightBit):
	z = decode(x, 8)
	print(str(z))
else:
	#incase of some funny business 
	h = "0" * (7-(len(x)%7)) + str(x)
	i = decode(x, 7)
	j = "0" * (8-(len(x)%8)) + str(x)
	k = decode(x, 8)
	print (str(i) + " or " + str(k))


