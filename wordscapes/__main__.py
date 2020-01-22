import argparse

from .solver import find_words

def parse_args(args):
	parser = argparse.ArgumentParser()

	parser.add_argument('--length', '-l', type=int)
	parser.add_argument('--mask', '-m')
	parser.add_argument('letters')

	return parser.parse_args(args)

def main(args=None):
	args = parse_args(args)

	words = find_words(args.letters, args.mask, args.length)

	for w in sorted(sorted(words), key=len):
		print(w)

if __name__ == '__main__':
	main()
