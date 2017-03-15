# csv to html

import sys

words = []
nums = []
def parsing():
    file = open("data/sample.csv").read().replace('"','').replace('\n',',').split(',')
    for i in file:
        if i.isdecimal():
            
            nums.append(i)
        else:
            words.append(i)
    words.pop(4)
    words.pop(5)

def making_html():
    code = "<table><tr>"
    parsing()
    numbers=[]
    for i in(0,5,10,15,20):
        numbers.append(nums[i:i+5])
    td = 5
    tr = 5
    for k in range(0,tr):
        for i in range(0,td):
            if i == 0:
                code += "<td>{0}</td>".format(words[i])
                words.pop(i)
            code += "<td>{0}</td>".format(numbers[k][i])
        
        code += "</tr>"
    code += "</table>"
    return code

def main():
    code = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Result</title></head><body>"""
    code += making_html()
    code += "</body></html>"
    html = open("data/index.html",'w')
    html.write(code)
    html.close()

main()