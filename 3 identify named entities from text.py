# To identify the named entities and store them in a text file

import nltk

# defining a function to extract named entities whose label is NE from a sentence

def extractname(taggedwords):
	entityname = []

	if hasattr(taggedwords, 'label') and taggedwords.label:
		if taggedwords.label() == 'NE':
			entityname.append(' '.join([child[0] for child in taggedwords]))
		else:
			for child in taggedwords:
				entityname.extend(extractname(child))

	return entityname

# opening the files necessary

txt = open("Texts.txt", "r")
txtw = open("TextsExtracted.txt", "w")

'''
For each line in txt file, we are word wise tokenizing it and then speech tagging it.
further, we chunk it and then search for the named entities necessary and store them back 
in txtw. 
'''

for line in txt:
	tokens = nltk.word_tokenize(line)
	tagged = nltk.pos_tag(tokens)
	entities = nltk.chunk.ne_chunk(tagged, binary=True)
	extracted = extractname(entities)
	for word in extracted:
		print(word)
		txtw.write(word)
		txtw.write("\n")
	print("\n")
