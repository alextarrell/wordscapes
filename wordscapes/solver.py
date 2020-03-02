from importlib import resources
from . import data
import itertools
import re

def find_words(letters, mask=None, length=None):
	words = match_letters(letters, length)

	if mask is not None:
		words = filter_regex(words, mask)

	return words

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
	with resources.open_text(data, 'word_list.txt') as f:
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
