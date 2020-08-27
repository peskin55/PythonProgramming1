#!/usr/bin/env python
from bs4 import BeautifulSoup
from re import findall
from urllib.parse import urljoin
from urllib.parse import urlparse
from html.parser import HTMLParser
from urllib.request import urlopen

class Vocab(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attribs in attrs:
                if attribs[0] == "href":
                    absolute = urljoin(self.url, attribs[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def getlinks(self):
        return self.links

def decode_url(url):
    analysis = urlopen(url).read().decode()
    importer = Vocab(url)
    importer.feed(analysis)
    finished = importer.getlinks()
    return finished

has_been_viewed = set()

def parse_dictionary(url):
	vocab = []
	for link in range(len(url)):
		path = urlparse(url[link]).path
		word = path[8:]
		print("Parsing info for " + word + ".")
		vocab.append([word, ""])
	return vocab

def delete_duplicates(url):
    new_list = []
    global has_been_viewed
    unique = decode_url(url)
    unique.sort()
    has_been_viewed.add(url)
    for uniq in unique:
        if uniq not in has_been_viewed:
            try:
                has_been_viewed.add(uniq)
                if findall("http://dictionary.reference.com/browse/+",uniq) != []:
                    new_list.append(uniq)
            except:
                pass
    return new_list

def change_definition(list):
    terms = []
    for n in range(len(list)):
        terms.append(list[n][0])
    update_vocab = input("Would you like to update a definition (Y/N)? ")
    while update_vocab in ["Y", "Yes", "y", "yes"]:
        term = input("Term: ")
        if term in terms:
            index = terms.index(term)
            list.pop(index)
            new_def = input("Definition: ")
            list.insert(index, [term,new_def])
        else:
            print("ERROR! Term not found.")
        return change_definition(list)
    edited_list = list
    return edited_list

story_path = input("What's the short story path? ")
full_url = "http://classicshorts.com/stories/" + story_path + ".html"
try:
    test = urlopen(full_url)
    deflist = delete_duplicates(full_url)
    if len(deflist) > 0:
        vocablist = parse_dictionary(deflist)
        print("Short story found. There are " + str(len(vocablist)) + " unique vocabulary words.")
        updated_list=change_definition(vocablist)
        file_export = input("What would you like to save the file as? ")
        outfile = open(file_export,'w')
        words = []
        for k in range(len(vocablist)):
            words.append(vocablist[k][0])
        cell_size = len(max(words, key = len))
        row_format = "{:<" + str(cell_size) + "} - {}\n"
        for line in range(len(updated_list)):
            outfile.writelines(row_format.format(updated_list[line][0],updated_list[line][1]))
        print("File saved!")
    else:
        print("Short story found. There are no vocabulary words.")
except:
    print("Short story not found.")
