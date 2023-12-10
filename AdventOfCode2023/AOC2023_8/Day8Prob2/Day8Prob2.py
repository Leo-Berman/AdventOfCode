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
    vals = []
    for i in range(len(lines)-2):
        mydict[lines[i+2][0]]=lines[i+2][2:4]
        if lines[i+2][0][2] == "A":
            vals.append(lines[i+2][0])
    #print(vals)
    i = 0
    found = False
    steps = 0
    test = len(vals)
    runtests = 0
    while found == False:
        #print(vals)
        for j in range(len(vals)):
            if vals[j][2]=='Z':
                runtests+=1
                if runtests == test:
                    print(steps)
                    #print(vals)
                    return
            else:
                runtests = 0
                break
        if i == patternlength:
            i = 0
        if pattern[i] == 'R':
            for j in range(len(vals)):
                vals[j] = mydict[vals[j]][1]
            i+=1
        else:
            for j in range(len(vals)):
                vals[j] = mydict[vals[j]][0]
            i+=1
        steps+=1
main()
    