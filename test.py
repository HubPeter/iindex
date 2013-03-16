#!/usr/bin/env python

from parse import getwords
	
if __name__=="__main__":
	content = open('parse.py', 'r')
	words = getwords(content)
	for word in words:
		print word
	
