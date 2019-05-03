#!/bin/bash


# Remove old folder and create new folder for output files
rm -rf steg2
mkdir steg2

# Use $i for interval
for i in {0..10}
do
	# interval
	Interval=$((2**$i))
	# Filename
	FileName="./steg2/Byte$Interval"
	Temp="_o2"
	FileName="$FileName$Temp"
	# echo so we know status
	echo $FileName
	# Run the Steg Program
	python steg.py -B -r -o256 -i$Interval -w$1 > $FileName
done

# Use $i for interval
for i in {0..10}
do
	# interval
	Interval=$((2**$i))
	# Filename
	FileName="./steg2/Byte$Interval"
	Temp="_o2048"
	FileName="$FileName$Temp"
	# echo so we know status
	echo $FileName
	# Run the Steg Program
	python steg.py -B -r -o2048 -i$Interval -w$1 > $FileName
done
