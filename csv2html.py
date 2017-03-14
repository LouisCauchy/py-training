# csv to html

import sys

file = open("data/sample.csv").read().replace('"','').replace('\n',',').split(',')
words = []
nums = []
for i in file:
    if i.isdecimal():
        nums.append(i)
    else:
        words.append(i)
words.pop(4)
words.pop(5)

   
            
