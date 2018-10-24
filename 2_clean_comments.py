import glob
import json
import re
import enchant
import string
from string import digits
import sys

# http://stackoverflow.com/a/13752628/6762004
RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

def strip_emoji(text):
    return RE_EMOJI.sub(r'', text)


def remove_non_english(my_string):
    d = enchant.Dict("en.US")
    english_words = []
    for word in my_string.split():
        if d.check(word):
            english_words.append(word)
            
    return " ".join(english_words)


#filename = 'testfile.json'
filename = sys.argv[1]

with open(filename + '.txt', 'w') as fw:
    with open(filename, 'r') as f:
        cnt = 1
        line = f.readline()
        while line:
            line =json.loads(line)
            textfield = line.get("text")
            remove_digits = str.maketrans('', '', digits)
            outstring = remove_non_english (strip_emoji(textfield).translate(string.punctuation).translate(remove_digits))
            if len(outstring)!=0:
                #print (outstring)
                fw.write(outstring + '\n')
            line = f.readline()
            cnt += 1

