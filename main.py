#!/usr/bin/env python3

import argparse
import random

CODES = [
	"Alfa",   "Bravo",     "Charlie", "Delta",
	"Echo",   "Foxtrot",   "Golf",    "Hotel",
	"India",  "Juliett",   "Kilo",    "Lima",
	"Mike",    "November", "Oscar",   "Papa",
	"Quebec",  "Romeo",    "Sierra",  "Tango",
	"Uniform", "Victor",   "Whiskey", "Xray",
	"Yankee",  "Zulu"
]

def check_codes(codes):
	correct = 0

	for code in codes:
		word = input("Code for letter {}: ".format(code[0]))
		if word.lower() != code.lower():
			while word.lower() != code.lower():
				word = input("Wrong! The correct answer is {}. Please type correct answer: ".format(code))

		else:
			correct += 1
			print("That was correct!")

	if correct == len(codes):
		print("You got all correct! Congrats!")
	else:
		print("You got {} out of {} correct!".format(correct, len(codes)))


if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		prog="NATO Phonetic Alphabet Learning Tool",
		description="Just a little tool written in Python to lean the NATO alphabet codes."
	)
	parser.add_argument("-r", "--random", action="store_true", help="randomizes order of codes")
	args = parser.parse_args()

	print("NATO Phonetic Alphabet Learning Tool")
	codes = CODES.copy()
	if args.random:
		random.shuffle(codes)
	check_codes(codes)

