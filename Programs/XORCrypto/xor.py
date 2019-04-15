
import sys


data = sys.stdin.read()
# data2 = open('plaintext', 'rb').read()
key = open('key2', 'rb').read()
# bdata2 = ' '.join(format(ord(x), 'b') for x in data2)
# bkey = ' '.join(format(ord(x), 'b') for x in key)
# print bdata2
# print bkey
# encoded = format(data2, "b") ^ format(key, "b")
# print key
# print data
# print "Next is encoded"
# data = open(data, 'rb').read()
def sxor(s1,s2):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

encoded = sxor(key,data)
print encoded