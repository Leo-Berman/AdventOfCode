# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:39:30 2023

@author: leo
"""

def main():
    with open("data2.txt") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        x=lines[i].find(":")
        y= lines[i].find("|")
        lines[i]=[lines[i][x+2:y-1].replace("  "," ").strip().split(" "),lines[i][y+2:-1].replace("  "," ").strip().split(" ")]
    part = 2
    # Day 1
    if part == 1:
        totalsum = 0
        for i in range(len(lines)):
            sum = 0
            for x in lines[i][0]:
                if x in lines[i][1]:
                    print(x)
                    sum+=1
                if sum == 0:
                    counter = 0
                else:
                    counter = 1
                    for x in range(sum-1):
                        counter*=2
            totalsum+=counter
        print(totalsum)
    
    # Day 2
    mydict = {}
    if part == 2:
        for i in range(len(lines)):
            mydict.update({i:1})
            
        i = 0
        while i < len(lines):
            sum = 0
            for x in lines[i][0]:
                if x in lines[i][1]:
                    sum+=1
            for j in range(sum):
                mydict[i+j+1]+=mydict[i]
            i+=1
        totalsum = 0
        print(mydict)
        for i in range(len(lines)):
            totalsum+=mydict[i]
        print(totalsum)
            
                
        
    

main()