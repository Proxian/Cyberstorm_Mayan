#!/bin/bash

# Delete old folder if it exists and create new one
rm -rf steg2
mkdir steg2

# $i represents the interval
for i in {1..4}
do
	# $j represents the offset
	for j in {1..10}
	do
		Interval=$(($i*2))
		# Set up the file name
		FileName="./steg2/Bit$Interval"
		offset=$((2**$j+1))
		Temp="_o$offset"
		FileName="$FileName$Temp"
		# echo so that we know the status
		echo $filename
		# Run the program
		python steg.py -b -r -o$offset -i$Interval -w$1 > $FileName
	done
done
