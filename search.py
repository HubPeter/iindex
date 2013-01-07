#!/usr/bin/env python
import sys

def load():
	'''
	load index, words and docs
	'''
	sIndex = 'index.txt'
	sWord = 'words.txt'
	sDoc = 'doc.txt'
	lIndex = []
	#load index
	fIndex = open(sIndex, 'r')
	for line in fIndex.readlines():
		lIndex.append( [int(i) for i in line.split()] )
	fIndex.close()
	#load words
	lWord = []
	fWord = open(sWord, 'r')
	for line in fWord.readlines():
		lWord.append([ int(line.split()[0]), line.split()[1] ])
	fWord.close()
	#load docs
	lDoc = []
	fDoc = open(sDoc, 'r')
	for line in fDoc.readlines():
		lDoc.append([ int(line.split()[0]), line.split()[1] ])
	fDoc.close()
	return (lIndex, lWord, lDoc)

if __name__=='__main__':

	#load index
	print 'Loading index...'
	lIndex, lWord, lDoc = load()
	print 'I am ready.'
	while True:
		key = raw_input('Key word:')
		print 'Your key word is : '+key
		print 'Documents matched is :'
		#get word id
		wid = -1
		for i in range(len(lWord)):
			if key==lWord[i][1]:
				wid = lWord[i][0]
		#find document id
		docs = []
		if wid==-1:
			print 'No matched'
			#sys.exit()
			continue
		for i in range(len(lIndex)):
			if lIndex[i][0]==wid:
				docs = lIndex[i][1:]
		if len(docs)==0:
			print 'No match.'
			#sys.exit()
			continue
		#find document path
		for item in docs:
			for i in range(len(lDoc)):
				if lDoc[i][0]==item:
					print lDoc[i][1]
		print '------------OK-------------------'
		#show path
