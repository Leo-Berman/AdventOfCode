# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:14:01 2023

@author: leo
"""
def main():
    with open("data2.txt") as f:
        lines = f.readlines()

    # Get Rid of All  Empty Lines and End of lines
    lines = list(filter(None,[x.replace("\n","").replace("=","").replace("(","").replace(")","").replace(",","").split(" ") for x in lines]))
    pattern = str(lines[0][0])
    patternlength=len(pattern)
    mydict = {}
    for i in range(len(lines)-2):
        mydict[lines[i+2][0]]=lines[i+2][2:4]
    i = 0
    found = False
    workval = 'AAA'
    steps = 0
    while found == False:

        if workval == 'ZZZ':
            found = True
        if i == patternlength:
            i = 0
        if pattern[i] == 'R':
            workval = mydict[workval][1]
            i+=1
        else:
            workval = mydict[workval][0]
            i+=1
        steps+=1
        893
    print(steps-1)
main()
    