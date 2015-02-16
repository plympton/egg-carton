from bs4 import BeautifulSoup
from os import path

#load stuff into bsoup
#take command from the command line, arg-v

#load var
#load var into soup
#run soup commands on var

soup = BeautifulSoup(open("hell-1.xhtml"))

#print(soup.find_all("p"))

wordCount = 0

for p in soup.find_all("p"):
    words = p.get_text()
    #print words
    words = words.split()
    #type(thing)
    wordCount +=len(words)
    print wordCount

p.find_all()