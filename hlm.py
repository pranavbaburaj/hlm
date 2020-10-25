#!/usr/bin/env python3

from urllib.request import URLopener
from sys import argv
from os import mkdir, listdir
from os.path import isdir

if __name__ == "__main__":
	if not isdir('modules'):
		mkdir('modules')
	if argv[1] == 'install':
		for lib in argv[2:]:
			try:
				URLopener().retrieve(f'https://raw.githubusercontent.com/hascal/hlm/main/libraries/{lib}.h', f'modules/{lib}.h')
			except:
				print(f"library {lib} not found")
	elif argv[1] == 'upgrade':
		for lib in map(lambda s: s[:-2], listdir('modules')):
			try:
				URLopener().retrieve(f'https://raw.githubusercontent.com/hascal/hlm/main/libraries/{lib}.h', f'modules/{lib}.h')
			except:
				print(f"library {lib} not found")
