'''
Created on Aug 31, 2014

@author: kdalwani
'''
import re
import operator
from wordCount import add_to_dict
from math import log, sqrt
def get_twitter_count(read_file, write_file):
    
    print 'Openning CSV file'
    f_read = open(read_file, "r")

    twitter_dict = {}
    
    lines = f_read.readlines()
    for line in lines:
        words = parse_twitter_data(line)
        add_to_dict(words, twitter_dict)

    print 'writing to file'    
    f_write = open(write_file, "w")
    max_value = max(twitter_dict.values())
    sorted_tuple = sorted(twitter_dict.items(), key=lambda x:-x[1])
#     sorted_x = sorted(twitter_dict.iteritems(), key=operator.itemgetter(1))
    for counts_key, sorted_value in sorted_tuple:
#         f_write.write("[\'" + counts_key + "\',"  + str(((float(sorted_value))/max_value * 20)) + "],\n")
        f_write.write("[\'" + counts_key + "\',"  + str(((sorted_value/float(max_value)))) + "],\n")
        f_write.flush()

    f_write.close()


def parse_twitter_data(line):
    words = re.split("\\s", line)
    return words[5:]
    
if __name__ == '__main__':
    
    twitter_file  = "kapildalwani"
    twitter_newsyc50  =  "newsyc50"
    get_twitter_count(twitter_file, twitter_file + ".counts")