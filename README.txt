Local file search program. Create invert index with your lcoal files.
And search files with key words quickly.

data files:
	note:
		these files are nothing about using, it is for programmers
	doc.txt: 
		document id  -- document  path 
	wd.txt:  
		word  --  document id
	words.txt: 
		word id -- word
	index.txt:  
		word id -- set of document id
	widdid.txt:  
		word id -- document id
	path.txt: 
		path to be indexed
	key.txt:
		hash_value  -- word -- wordid
	
	Hint: this if for you to know this code easily, if you don't want 
	to see the detail, just see <0 <1 <2 directly.

code moudles:

	parse.py:
		get word-docid list to the wd.txt
		write doc-docid to the doc.txt

	build.py:
		build invert index and words
	key.py:
		get hash value from words
	
	
0. Config your local search.
	Edit path.txt.
	e.g. if you want 
		/usr/local/include
	to be indexed, just add the path.


1. How to use?
	>build invert index:
		python llsearch.py build
	
	>Use your search engine
		python llearch.py search
	
	>For help
		python llsearch.py help
	
	Ctrl-c to exit local search engine.

2. How to remove?
	>Delete files occured in <data files> and <code moudles>
		Hint: there is nothing with your own file.

$. Welcome to email me with or without problem:
	tecnodechina@gmail.com	
