#!/bin/bash


# Remove old folder and create new folder for output files
rm -rf stegtest
mkdir stegtest

# Use $i for interval
for i in {0..8}
do
	# interval
	Interval=$((2**$i))
	# Filename
	FileName="./stegtest/Byte$Interval"
	Temp="_o$2"
	FileName="$FileName$Temp"
	# echo so we know status
	echo $FileName
	# Run the Steg Program
	python steg.py -B -r -o$j -i$Interval -w$1 > $FileName
done

# Use $i for interval
for i in {0..8}
do
	# interval
	Interval=$((2**$i))
	# Filename
	FileName="./stegtest/Byte$Interval"
	Temp="_o$2048"
	FileName="$FileName$Temp"
	# echo so we know status
	echo $FileName
	# Run the Steg Program
	python steg.py -B -r -o$j -i$Interval -w$1 > $FileName
done
