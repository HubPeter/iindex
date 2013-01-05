#!/usr/bin/env python
from os import walk

def parse():
	'''
	parse all document and get 
	word-docid
	and save document path and document id into doc.txt
	'''
	lAllDocs = []
	sDocListFileName = 'doc.txt'
	fDocs = open( sDocListFileName, 'w' )
	sWIdDIdFileName = 'wd.txt'
	fWD = open(sWIdDIdFileName, 'w')
	for ( dirpath, dirname, filenames ) in walk('./src/kernel'):
		for filename in filenames:
			sCurDocName = dirpath+'/'+filename
			#put current document into document list
			lAllDocs.append( sCurDocName )
			#get items of word-docid
			nCurDocId = len( lAllDocs )-1#0 based index
			content =  open(sCurDocName ,'r').read()
			lWIDDId = content.split()
			#write lWID_DId into temp_index_file
			for item in lWIDDId:
				print>>fWD, item+" "+str(nCurDocId)
			print>>fDocs, str(nCurDocId)+'	'+sCurDocName
	fDocs.close()
	fWD.close()

if __name__=='__main__':
	parse()
