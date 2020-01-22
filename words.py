import argparse
import itertools
import re

def parse_args(args):
	parser = argparse.ArgumentParser()

	parser.add_argument('--length', '-l', type=int)
	parser.add_argument('--match', '-m')
	parser.add_argument('letters')

	return parser.parse_args(args)

def main(args=None):
	args = parse_args(args)

	words = match_letters(args.letters, args.length)

	if args.match is not None:
		words = filter_regex(words, args.match)

	for w in sorted(sorted(words), key=len):
		print(w)

def match_letters(letters, length=None):
	if not letters:
		return []

	if length is not None and (length < 3 or length > len(letters)):
		raise ValueError('Invalid Length')
	elif length is None:
		length = len(letters)

	letters = letters.lower()
	pattern = re.compile(f'^[{letters}]*$')

	potentials = set()
	with open("word_list.txt") as f:
		for word in f:
			match = pattern.match(word)
			if match:
				potentials.add(match.group(0))

	words = set()
	for l in range(3, length + 1):
		for p in itertools.permutations(letters, l):
			p_word = ''.join(p)
			if p_word in potentials:
				words.add(p_word)

	return words

def filter_regex(words, pattern):
	pattern = re.compile(f'^{pattern}$')
	return [w for w in words if pattern.match(w)]

if __name__ == '__main__':
	main()
