from bs4 import BeautifulSoup, Tag
from os import path
#from collections import Counter

"""soup = BeautifulSoup(open("DeepDownDark.xhtml")) this is a test case
#make this a function
#fnct that takes a soup, 
for a in soup.findAll('a'): #loop through all of the results from the search for 'a'
    print(a) #
    p = Tag(soup, 'p') #create a P element
    a.replaceWith(p)   #Put it where the A element is



soup = BeautifulSoup("<b>Argh!</b>")



1) create soup  - take a file, return a soup
2) take a soup, a tag to find, and a tag to replace it with - return a soup
3) write a soup to a file

make three defs for functions
write out their 3 arguments - soup, from, to
"""

def makeSoup(file_name):
	return BeautifulSoup(open(file_name))

def replaceTag(soup, old_tag, new_tag):
	for a in soup.findAll("p", old_tag): #loop through all of the results from the search for 'old_tag', even if its a class and not a plain tag
		a.unwrap() 
		print(a)
		a.wrap(soup.new_tag(new_tag))


def saveSoup(soup, file_name):
 	html_string = soup.prettify()
 	open(file_name, "wb").write(html_string)

def replaceTagWithContents(old_tag, new_tag_name):
	#get the contents of the old tag
	contents = old_tag.contents
	#create an empty new tag based on new_tag_name
	new_tag = soup.new_tag(new_tag_name)
	#fill up the new tag with the contents of the old tag
	new_tag.append(contents[0])
	#
	old_tag.replaceWith(new_tag)

if __name__ == "__main__":
	soup = makeSoup("txtest.xhtml")
	#print(soup)
	#replaceTag(soup, 'TX', 'p')
	for old_tag in soup.findAll('p'):
		replaceTagWithContents(old_tag, "b")
	saveSoup(soup, "prettyFile")



"""
the beginnings of how to find the wordcount and process books based on that is below. incomplete.
print(soup.find_all("p"))

wordCount = 0
class_counter = Counter()

for p in soup.find_all("p"):
    words = p.get_text()
    print words
    words = words.split()
    type(thing)
    wordCount +=len(words)
    print wordCount
    

p.find_all("p", "s1")

#use soup to find what classes we're dealing with
find the count of each type of class


"""