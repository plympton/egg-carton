from bs4 import BeautifulSoup
from os import path
from collections import Counter

#load stuff into bsoup
#take command from the command line, arg-v

#load var
#load var into soup
#run soup commands on var

soup = BeautifulSoup(open("hell-1.xhtml"))

#print(soup.find_all("p"))

wordCount = 0
class_counter = Counter()

for p in soup.find_all("p"):
    words = p.get_text()
    #print words
    words = words.split()
    #type(thing)
    wordCount +=len(words)
    print wordCount
    

p.find_all("p", "s1")

#use soup to find what classes we're dealing with
#find the count of each type of class