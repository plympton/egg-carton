from bs4 import BeautifulSoup, Tag
from os import path
import codecs
#from collections import Counter

def makeSoup(file_name):
	return BeautifulSoup(open(file_name))

def replaceTag(soup, old_tag, new_tag):
	for a in soup.findAll("p", old_tag): #loop through all of the results from the search for 'old_tag', even if its a class and not a plain tag
		a.unwrap() 
		print(a)
		a.wrap(soup.new_tag(new_tag))


def saveSoup(soup, file_name):
 	html_string = soup.prettify()
 	# wb means open the file_name with write binary permissions
 	codecs.open(file_name, "wb", encoding='utf-8').write(html_string)

def replaceTagWithContents(old_tag, new_tag_name):
	#get the contents of the old tag
	contents = old_tag.contents
	#create an empty new tag based on new_tag_name
	new_tag = soup.new_tag(new_tag_name)
	#fill up the new tag with the contents of the old tag
	new_tag.append(contents[0])
	# replaces this back in the soup, don't need to return
	old_tag.replaceWith(new_tag)

def replace_all_tags(soup, old_tag_name, new_tag_name, old_tag_class=None):
	""" takes, a soup object, the old tag name (str), new_tag_name (str)
		and an optional old_tag_class (str)
		finds the old tags in the soup, and runs a replacement with new_tag_name
	"""
	if old_tag_class:
		old_tags = soup.find_all(old_tag_name, class_=old_tag_class)
	else:
		old_tags = soup.find_all(old_tag_name)

	for old_tag in old_tags:
		replaceTagWithContents(old_tag, new_tag_name)


# p.TX > p
# p.BOLD > strong
# p.CCT__1 > p

if __name__ == "__main__":
	soup = makeSoup("DeepDownDark.xhtml")
	#print(soup)
	#replaceTag(soup, 'TX', 'p')
	# changes is a list, where every element has an OLD_Tag, old_tag class and a new_tag
	changes = [
		['p', 'TX', 'p'], # all below use standard <p></p>
		['p', 'EP', 'p'],
		['p', 'CRT__L1', 'p'],
		['p', 'CRT__L2', 'p'],
		['p', 'CRT__L', 'p'],
		['p', 'EXN', 'p'],
		['p', 'EXV', 'p'],
		['p', 'CPT', 'p'],
		['p', 'CCT__1', 'p'],
		['p', 'CCT', 'p'],
		['p', 'sp', 'p'],
		['p', 'ntx', 'p'],
		['p', 'CFMH', 'p'],
		['p', 'TNI-2', 'p'],
		['p', 'STXS', 'p'],
		['p', 'STNI', 'p'],
		['p', 'STX', 'p'],
		['p', 'TXS', 'p'],
		['p', 'SB2', 'p'],
		['p', 'SB2-NOSPACE', 'p'],
		['p', 'CO', 'p'],
		['p', 'EXVSB', 'p'],
		['p', 'BMTNI', 'p'],
		['p', 'BMTX', 'p'],
		['p', 'CAP', 'p'],
		['p', 'TNI', 'p'],
		['p', 'ATATNI', 'p'],
		['p', 'CBMH', 'p'],
		['p', 'HEAD', 'H2'], # all below use <h2></h2>
		['p', 'HEAD-1', 'H2'],
		['p', 'ABMH', 'H2'],
		['p', 'ACH', 'H2'],
		['p', 'FMH', 'H2'],
		['p', 'ePub-I', 'em'] # all below use <em></em>phasis for italics
		['p', 'ePub-B', 'strong'], # same for bold
		['p', 'ePub-SC-B', 'strong'],
		['p', 'ePub-SC', 'small'], #and small
		# ['p', 'TIT', 'center'] #and center 

	] 

	for change in changes:
		replace_all_tags(soup, change[0], change[2], old_tag_class=change[1])
	saveSoup(soup, "prettyFile.html")



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