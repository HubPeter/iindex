#!/usr/bin/env python
import sys

def getDocMap():
	'''
	get all document and document id key-value item from doc.txt
	'''
	sDocListFile = 'doc.txt'
	fDocList = open(sDocListFile, 'r')
	dDocId = {}
	for line in fDocList.readlines():
		nDocId = line.split()[1]
		sDocPath = line.split()[0]
		dDocId[nDocId] = sDocPath
	fDocList.close()
	return dDocId

#get all words and replace word with wid in wd.txt
def genWords():
	'''
	get all words from wd.txt
	replace word with wid and write them back to wd.txt
	'''
	#read all word-docid from wd.txt
	sWDFile = 'wd.txt'
	lWD = []
	fWDFile = open(sWDFile, 'r')
	for line in fWDFile.readlines():
		lWD.append([ line.split()[0] ,int(line.split()[1])])
	fWDFile.close()
	#get all words and replace word with wid
	lWords = []
	for item in lWD:
		# hello = 12
		# word = id
		if item[0] not in lWords:
			lWords.append( item[0] )
		item[0] = lWords.index(item[0])

	#write wid-docid back
	fWDFile = open('widdid.txt', 'w')
	lWD.sort()
	for item in lWD:
		print>>fWDFile, str(item[0])+' '+str(item[1])
	fWDFile.close()
	#save words in words.txt
	fWords = open('words.txt', 'w')
	for i in range(len(lWords)):
		print>>fWords, str(i)+' '+lWords[i]
	fWords.close()
	
def invert():
	'''
	read all wid-did and sort
	and generate invert index
	'''
	sWDFile = 'widdid.txt'
	lWD = []
	fWDFile = open(sWDFile, 'r')
	for line in fWDFile.readlines():
		lWD.append( [ int(i) for i in line.split()] )
	fWDFile.close()
	#sort
	lWD.sort( )
	#generate invert index
	nBegin = 0
	lInvert = []
	i = 0
	while i < len(lWD):	
		lDocs = []#set fo current word's document id
		nWid = lWD[nBegin][0]#wid of current word
		lDocs.append(nWid)#put wid
		#deal with current word and its document id set
		while i<len(lWD) and lWD[i][0]==lWD[nBegin][0]:
			if lWD[i][1] not in lDocs[1:]:
				lDocs.append( lWD[i][1] )
			i += 1
		#goto next word
		lInvert.append( lDocs )
		nBegin = i

	#write 
	sInvert = 'index.txt'
	fInvert = open(sInvert, 'w')
	for item in lInvert:
		for i in range(len(item)):
			fInvert.write('%s '%item[i])
		fInvert.write('\n')
	fInvert.close()

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
	#genWords()
	#invert()
	
	#load inde
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
		

	


	#load word
	#load docs



