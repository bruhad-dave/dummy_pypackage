__version__ = "0.0.1"

import sys
from .other_logic import other_greeting

def main():
	if sys.argv[1]:
		print("hello, " + sys.argv[1])
	else:
		print("hello, world!")
	other_greeting()
	
	return
