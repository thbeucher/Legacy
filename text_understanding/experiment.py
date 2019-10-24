# -*- coding: utf-8 -*-
import json
import re
import ast
import numpy as np

# get all alphabetic letters
letters = [l.strip('\n') for l in open('letters.txt')]

# find all words in the file
words = re.findall(r'\w+', open('big.txt').read().lower())
print(len(words), words[:5])

# delete doublon
words = list(set(words))
print(len(words), words[:5])

# remove non-alphabet chars
regex = re.compile('[^a-zA-Z]')
words = [regex.sub('', w) for w in words]
print(words[:5])



# convert string representation of a list into a numpy array
# np.asarray(ast.literal_eval(x)) where x = '[[1,2,3], [4,5,6]]
