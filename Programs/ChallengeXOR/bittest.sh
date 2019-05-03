#!/bin/bash

# Delete old folder if it exists and create new one
rm -rf stegtest
mkdir stegtest

# $i represents the interval
for i in {1..4}
do
	# $j represents the offset
	for j in {0..10}
	do
		Interval=$i
		# Set up the file name
		FileName="./stegtest/Bit$Interval"
		offset=$((2**$j+1))
		Temp="_o$offset"
		FileName="$FileName$Temp"
		# echo so that we know the status
		echo $filename
		# Run the program
		python steg.py -b -r -o$offset -i$Interval -w$1 > $FileName
	done
done
