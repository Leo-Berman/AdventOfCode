# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:14:01 2023

@author: leo
"""

def main():
    with open("data2.txt") as f:
        lines = f.readlines()
    # Get Rid of All  Empty Lines and End of lines
    lines = list(filter(None,[x.replace("\n","").replace("Time:","").replace("Distance:","").strip(" ").split(" ") for x in lines]))
    for i in range(len(lines)):
        lines[i] = list(filter(lambda y: len(y)>0,lines[i]))
        print(lines[i])
        lines[i] = int(lines[i][0]+lines[i][1]+lines[i][2]+lines[i][3])
    
    runsum = 0
    for i in range(lines[0]):
        distance = (lines[0]-i)*i
        if distance > (lines[1]):
            runsum+=1
    print(runsum)
main()
    