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
	print 'Begin to get all words.......'
	#read all word-docid from wd.txt
	sWDFile = 'wd.txt'
	lWD = []
	fWDFile = open(sWDFile, 'r')
	print 'Load wd.txt....'
	for line in fWDFile.readlines():
		lWD.append([ line.split()[0] ,int(line.split()[1])])
	fWDFile.close()
	#get all words and replace word with wid
	lWords = []
	print 'Get words...'
	process = '#'
	i = 0
	length = len(lWD)
	for item in lWD:
		# hello = 12
		# word = id
		print str(i)+' of '+str(length)+'\r',
		i+=1
		sys.stdout.flush()
		if item[0] not in lWords:
			lWords.append( item[0] )
		item[0] = lWords.index(item[0])

	#write wid-docid back
	fWDFile = open('widdid.txt', 'w')
	print 'Sort....'
	lWD.sort()
	print 'Saving result to wd.txt...'
	for item in lWD:
		print>>fWDFile, str(item[0])+' '+str(item[1])
	fWDFile.close()
	#save words in words.txt
	print 'Saving all words to words.txt...'
	fWords = open('words.txt', 'w')
	for i in range(len(lWords)):
		print>>fWords, str(i)+' '+lWords[i]
	fWords.close()
	print 'Get words finished.'
def invert():
	'''
	read all wid-did and sort
	and generate invert index
	'''
	sWDFile = 'widdid.txt'
	lWD = []
	print 'Begin create invert index....'
	fWDFile = open(sWDFile, 'r')
	print 'Load files.....'
	for line in fWDFile.readlines():
		lWD.append( [ int(i) for i in line.split()] )
	fWDFile.close()
	#sort
	print 'Sort wordid-docid items....'
	lWD.sort( )
	#generate invert index
	print 'Creating invert index.....'
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
	print 'Saving invert index to index.txt...'
	sInvert = 'index.txt'
	fInvert = open(sInvert, 'w')
	for item in lInvert:
		for i in range(len(item)):
			fInvert.write('%s '%item[i])
		fInvert.write('\n')
	fInvert.close()
	print 'All succeed!'


if __name__=='__main__':
	genWords()
	invert()
