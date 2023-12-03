# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:15:25 2023

@author: leo
"""

def main():
    with open("data2.txt") as f:
        lines = f.readlines()
    i = 0
    for x in lines:
        lines[i] = x.strip("\n")
        i+=1
    
    # add dots to the end
    insertlist=""
    for x in range(len(lines[0])):
        insertlist+="."
    lines.insert(0,insertlist)
    lines.insert(len(lines),insertlist)

    
    i = 0
    for x in lines:
        lines[i]+="."
        lines[i]="."+lines[i]
        i+=1
        
    mydict = {}

    for j in range(len(lines)):
        i = 1
        while i < (len(lines[j])-2):
            if lines[j][i].isdigit():
                num=""
                adj = []
                while lines[j][i].isdigit():
                    adj.append((j-1,i-1))
                    adj.append((j-1,i))
                    adj.append((j-1,i+1))
                    adj.append((j,i-1))
                    adj.append((j,i+1))
                    adj.append((j+1,i-1))
                    adj.append((j+1,i))
                    adj.append((j+1,i+1))
                    num+=lines[j][i]
                    i+=1
                adj = list(set(adj))
                for x in adj:
                    if x not in mydict:
                        mydict.update({x:[int(num)]})
                    else:
                        mydict[x].append(int(num))
            i+=1
    mysum = 0
    part = 2
    for i in range(len(lines)):
        for j in range(len(lines)):
            if part == 1:
                # part 1
                if lines[i][j].isdigit()==False and lines[i][j] != ".":
                    if (i,j) in mydict:
                        for x in mydict[(i,j)]:
                            #print(x)
                            mysum+=x
            else:
                # part 2
                if lines[i][j] =="*":
                    if (i,j) in mydict:
                        runsum = 1
                        if len(mydict[(i,j)]) == 2:
                            for x in mydict[(i,j)]:
                                runsum*=x
                            mysum+=1*runsum
    print(mysum)
main()