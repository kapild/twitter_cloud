'''
Created on Aug 31, 2014

@author: kdalwani
'''
from string import lower
import re
def countWords(lines):
    word_dict = {}
    for line in lines:
        words = line.split()
        add_to_dict(words, word_dict)

    print word_dict 
    return word_dict

replace_to_space_regex = "[\\.|\\!|\\(|\\)|\\#\\,\\:\\/\\-\\;\\?\\\"\\\\\@\\$\\*\\']"
igonore_words_list =["i",       
"the",     
"is",      
"to",      
"you",     
"a",       
"in",      
"with",
"https",
"an",
"with",
"what",
"from",
"of",      
"for",    
"co",
"http",
"can",
"by",
"if",
"via",
"all",
"its",
"was",
"rt",
"and",     
"on",      
"so", "am", "be","or",
"how", "why", "that",
"has", "should",
"than",
"at",      
"it",      
"this",    
"are"]     
ignore_words = set(igonore_words_list)
def add_to_dict(words, word_dict, ):
    for word in words:
        word = lower(word)
        if word.startswith("@"):
            continue
        word = re.sub(replace_to_space_regex, " ", word)
        word = word.strip()
        word_agains = word.split()
        for word_2 in word_agains:
            if word_2 in ignore_words or len(word_2) == 1 or len(word_2) == 2:
                continue
            count = 0
            if word_2 in word_dict:
                count = word_dict[word_2]
            word_dict[word_2] = count + 1

def test_word_count():
    lines = []
    lines.append("hdaoop in hadoop world")
    lines.append("hdaoop in java world")
    lines.append("java in hive world")
    lines.append("Hdaoop in java world")
    lines.append("Hdaoop In Java world")

    countWords(lines)


if __name__ == '__main__':
    test_word_count()