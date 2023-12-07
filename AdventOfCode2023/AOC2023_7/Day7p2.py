# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:14:01 2023

@author: leo
"""
from statistics import multimode
from collections import Counter
def main():
    # Swap function
    def swapPositions(list, pos1, pos2): 
        swaprank(list[pos1],list[pos2])
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list
    def swaprank(first,second):
        firstrank = first.retrank()
        secondrank = second.retrank()
        second.changerank(firstrank)
        first.changerank(secondrank)
    class camelhand():
        def __init__(self,hand,score):
            self.hand = list(hand)
            self.sethand()
            self.score = int(score)
            self.sethandmode()
        def sethand(self):
            replace = lambda x: "9.1" if x == "T" else x
            self.hand = list(map(replace, self.hand))
            replace = lambda x: "1" if x == "J" else x
            self.hand = list(map(replace, self.hand))
            replace = lambda x: "9.3" if x == "Q" else x
            self.hand = list(map(replace, self.hand))
            replace = lambda x: "9.4" if x == "K" else x
            self.hand = list(map(replace, self.hand))
            replace = lambda x: "9.5" if x == "A" else x
            self.hand = list(map(replace, self.hand))
        def retscore(self):
            return self.score
        def sethandmode(self):
            modes = Counter(self.hand)
            print(self.hand)
            if modes.most_common()[0][0] == '1':
                if modes.most_common()[0][1] == 5:
                    currmode = 5
                else:
                    currmode=modes.most_common()[1][1]+modes['1']
            else:
                currmode = modes.most_common()[0][1]+modes['1']
            if currmode == 5:
                self.handmode = 7
            elif currmode == 4:
                self.handmode = 6
            elif currmode == 3:
                if modes.most_common()[1][1] == 2:
                    self.handmode = 5
                else:
                    self.handmode = 4
            elif currmode == 2:
                if modes.most_common()[1][1]==2:
                    self.handmode = 3
                else:
                    self.handmode = 2
            else:
                self.handmode = 1
            #print(self.handmode)
        def printself(self):
            print(self.hand,self.handmode,self.score)
        def rethandmode(self):
            return self.handmode
    with open("data2.txt") as f:
        lines = f.readlines()

    # Get Rid of All  Empty Lines and End of lines
    lines = list(filter(None,[x.replace("\n","").split(" ") for x in lines]))
    highcards = []
    onepairs = []
    twopairs= []
    threekind = []
    fullhouse = []
    fourkind = []
    fivekind = []
    for x in lines:
        temp = camelhand(x[0],x[1])
        handmode = temp.rethandmode()
        if handmode == 1:
            highcards.append(temp)
        elif handmode == 2:
            onepairs.append(temp)
        elif handmode == 3:
            twopairs.append(temp)
        elif handmode == 4:
            threekind.append(temp)
        elif handmode == 5:
            fullhouse.append(temp)
        elif handmode == 6:
            fourkind.append(temp)
        else:
            fivekind.append(temp)
            
            
    
    highcards.sort(key = lambda x: x.hand,reverse = False)
    onepairs.sort(key = lambda x: x.hand,reverse = False)
    twopairs.sort(key = lambda x: x.hand,reverse = False)
    threekind.sort(key = lambda x: x.hand,reverse = False)
    fullhouse.sort(key = lambda x: x.hand,reverse = False)
    fourkind.sort(key = lambda x: x.hand,reverse = False)
    fivekind.sort(key = lambda x: x.hand,reverse = False)
    
    totallist = highcards+onepairs+twopairs+threekind+fullhouse+fourkind+fivekind
    #Rememberto find mode to determine hand type
    i = 1
    total = 0
    for x in totallist:
        x.printself()
        total+=i*x.retscore()
        i+=1
    print(total)
main()
    