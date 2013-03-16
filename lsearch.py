#!/usr/bin/env python

import sys

from build import build
from parse import parse
from search import search

if __name__=='__main__':
	if len(sys.argv)!=2:
		print 'usage: ./lsearch <command>'
		print '	command: build | search | help'
		sys.exit()
	#work
	if sys.argv[1]=='help':
		#help
		print 'All you need is in README.txt'
		sys.exit()
	if sys.argv[1]=='build':
		build()
		sys.exit()
	if sys.argv[1]=='search':
		search()
		sys.exit()
	print 'Bad command.'
	
		
