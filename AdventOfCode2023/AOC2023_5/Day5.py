# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:04:03 2023

@author: leo
"""
from collections import defaultdict
class seed2:
    def __init__(self,seednum):
        self.seednum = seednum
    def advance(self,inlist):
        DestinationStart = int(inlist[0])
        SourceStart = int(inlist[1])
        Length = int(inlist[2])
        if self.seednum >= SourceStart and self.seednum <= SourceStart+Length-1:
            self.seednum = (self.seednum-SourceStart)+(DestinationStart)
            return True
        else:
            return False
    def returnlocationnum(self):
        return self.seednum
class seed:
    def __init__(self,num):
        self.seednum = num
        self.soilnum = -1
        self.fertilizernum = -1
        self.waternum = -1
        self.lightnum = -1
        self.tempnum = -1
        self.humiditynum = -1
        self.locationnum = -1
        
    # print seed num
    def printseednum(self):
        print(self.seednum)
    
    # Calculate Soil Num
    def findsoilnum(self,inlist):
        DestinationStart = int(inlist[0])
        SourceStart = int(inlist[1])
        Length = int(inlist[2])
        if self.seednum >= SourceStart and self.seednum <= SourceStart+Length-1:
            self.soilnum = (self.seednum-SourceStart)+(DestinationStart)
        elif self.soilnum == -1:
            self.soilnum = self.seednum
    
    # print soil number
    def printsoilnum(self):
        print(self.soilnum)
        
    
    # Calculate fertilizer number
    def findfertilizernum(self,inlist):
        DestinationStart = int(inlist[0])
        SourceStart = int(inlist[1])
        Length = int(inlist[2])
        if self.soilnum >= SourceStart and self.soilnum <= SourceStart+Length-1:
            self.fertilizernum = (self.soilnum-SourceStart)+(DestinationStart)
        elif self.fertilizernum == -1:
            self.fertilizernum = self.soilnum
    
    # print fertilizer number
    def printfertilizernum(self):
        print(self.fertilizernum)
        
    # Calculate water number
    def findwaternum(self,inlist):
        DestinationStart = int(inlist[0])
        SourceStart = int(inlist[1])
        Length = int(inlist[2])
        if self.fertilizernum >= SourceStart and self.fertilizernum <= SourceStart+Length-1:
            self.waternum = (self.fertilizernum-SourceStart)+(DestinationStart)
        elif self.waternum == -1:
            self.waternum = self.fertilizernum
    
    # print water number
    def printwaternum(self):
        print(self.waternum)
        
    # Calculate light number
    def findlightnum(self,inlist):
        DestinationStart = int(inlist[0])
        SourceStart = int(inlist[1])
        Length = int(inlist[2])
        if self.waternum >= SourceStart and self.waternum <= SourceStart+Length-1:
            self.lightnum = (self.lightnum-SourceStart)+(DestinationStart)
        elif self.lightnum == -1:
            self.lightnum = self.waternum
    
    # print water number
    def printlightnum(self):
        print(self.lightnum)    
    
    # Calculate temperature number
    def findtempnum(self,inlist):
        DestinationStart = int(inlist[0])
        SourceStart = int(inlist[1])
        Length = int(inlist[2])
        if self.lightnum >= SourceStart and self.lightnum <= SourceStart+Length-1:
            self.tempnum = (self.lightnum-SourceStart)+(DestinationStart)
        elif self.tempnum == -1:
            self.tempnum = self.lightnum
    
    # print temp number
    def printtempnum(self):
        print(self.tempnum)
        
    # Calculate humidity number
    def findhumiditynum(self,inlist):
        DestinationStart = int(inlist[0])
        SourceStart = int(inlist[1])
        Length = int(inlist[2])
        if self.tempnum >= SourceStart and self.tempnum <= SourceStart+Length-1:
            self.humiditynum = (self.tempnum-SourceStart)+(DestinationStart)
        elif self.humiditynum == -1:
            self.humiditynum = self.tempnum
    
    # print water number
    def printhumiditynum(self):
        print(self.humiditynum)
    
    # Calculate location number
    def findlocationnum(self,inlist):
        DestinationStart = int(inlist[0])
        SourceStart = int(inlist[1])
        Length = int(inlist[2])
        if self.humiditynum >= SourceStart and self.humiditynum <= SourceStart+Length-1:
            self.locationnum = (self.humiditynum-SourceStart)+(DestinationStart)
        elif self.locationnum == -1:
            self.locationnum = self.humiditynum
    
    # print location number
    def printlocationnum(self):
        print(self.locationnum)
    
    # return locationnumber
    def returnlocationnum(self):
        return self.locationnum
    
# generate list of seeds
def makelist(pair):
    retlist = []
    for i in range(pair[1]):
        retlist.append(int(pair[0])+i)
    return retlist
            
def main():
    with open("data2.txt") as f:
        lines = f.readlines()
    # Get Rid of All  Empty Lines and End of lines
    lines = list(filter(None,[x.replace("\n","") for x in lines]))
    # Get Rid of map:
    lines = [x.replace("map:","").split(" ") for x in lines]
    # Get Rid of blank spaces left by map
    for i in range(len(lines)):
        lines[i] = list(filter(None,lines[i]))
    
    # set which problem to answer
    prob = 2
    
    if prob == 1:
        #generate listof seeds
        listofseeds = [seed(int(x)) for x in lines[0][1::]]
    elif prob == 2:
        ranges = [int(x) for x in lines[0][1::]]
        ranges = [ranges[i:i+2] for i in range(0,len(ranges),2)]
        

    # Find Where Conversion Lists Start And End
    SeedToSoilIndex = lines.index(['seed-to-soil'])
    SoilToFertilizerIndex = lines.index(['soil-to-fertilizer'])
    FertilizerToWaterIndex = lines.index(['fertilizer-to-water'])
    WaterToLightIndex = lines.index(['water-to-light'])
    LightToTempIndex = lines.index(['light-to-temperature'])
    TempToHumidityIndex = lines.index(['temperature-to-humidity'])
    HumidityToLocationIndex = lines.index(['humidity-to-location'])
    if prob == 1:
        for x in lines[SeedToSoilIndex+1:SoilToFertilizerIndex]:
            for y in listofseeds:
                y.findsoilnum(x)
        for x in lines[SoilToFertilizerIndex+1:FertilizerToWaterIndex]:
            for y in listofseeds:
                y.findfertilizernum(x)
        for x in lines[FertilizerToWaterIndex+1:WaterToLightIndex]:
            for y in listofseeds:
                y.findwaternum(x)
        for x in lines[WaterToLightIndex+1:LightToTempIndex]:
            for y in listofseeds:
                y.findlightnum(x)
        for x in lines[LightToTempIndex+1:TempToHumidityIndex]:
            for y in listofseeds:
                y.findtempnum(x)
        for x in lines[TempToHumidityIndex+1:HumidityToLocationIndex]:
            for y in listofseeds:
                y.findhumiditynum(x)
        for x in lines[HumidityToLocationIndex+1::]:
            for y in listofseeds:
                y.findlocationnum(x)
    
        retlist = []
        for y in listofseeds:
            retlist.append(y.returnlocationnum())

        print(min(retlist))
    elif prob == 2:
        
        # Try intervalmap???
        SeedToSoilDict = defaultdict(lambda: 0)
        for x in lines[SeedToSoilIndex+1:SoilToFertilizerIndex]:
            Source = int(x[1])
            Destination = int(x[0])
            Length = int(x[2])
            num2add = Destination-Source
            for i in range(Source,Source+Length,1):
                SeedToSoilDict.update({i:num2add})
        SoilToFertilizerDict = defaultdict(lambda: 0)
        for x in lines[SoilToFertilizerIndex+1:FertilizerToWaterIndex]:
            Source = int(x[1])
            Destination = int(x[0])
            Length = int(x[2])
            num2add = Destination-Source
            for i in range(Source,Source+Length,1):
                SoilToFertilizerDict.update({i:num2add})
        FertilizerToWaterDict = defaultdict(lambda: 0)
        for x in lines[FertilizerToWaterIndex+1:WaterToLightIndex]:
            Source = int(x[1])
            Destination = int(x[0])
            Length = int(x[2])
            num2add = Destination-Source
            for i in range(Source,Source+Length,1):
                FertilizerToWaterDict.update({i:num2add})
        WaterToLightDict = defaultdict(lambda: 0)
        for x in lines[WaterToLightIndex+1:LightToTempIndex]:
            Source = int(x[1])
            Destination = int(x[0])
            Length = int(x[2])
            num2add = Destination-Source
            for i in range(Source,Source+Length,1):
                WaterToLightDict.update({i:num2add})
        LightToTempDict = defaultdict(lambda: 0)
        for x in lines[LightToTempIndex+1:TempToHumidityIndex]:
            Source = int(x[1])
            Destination = int(x[0])
            Length = int(x[2])
            num2add = Destination-Source
            for i in range(Source,Source+Length,1):
                LightToTempDict.update({i:num2add})
        TempToHumidityDict = defaultdict(lambda: 0)
        for x in lines[TempToHumidityIndex+1:HumidityToLocationIndex]:
            Source = int(x[1])
            Destination = int(x[0])
            Length = int(x[2])
            num2add = Destination-Source
            for i in range(Source,Source+Length,1):
                TempToHumidityDict.update({i:num2add})
        HumidityToLocationDict = defaultdict(lambda: 0)
        for x in lines[HumidityToLocationIndex+1::]:
            Source = int(x[1])
            Destination = int(x[0])
            Length = int(x[2])
            num2add = Destination-Source
            for i in range(Source,Source+Length,1):
                HumidityToLocationDict.update({i:num2add})
        total=0
        runnin = 99999999999
        for y in ranges:
            for x in range(y[0],y[0]+y[1],1):
                x+=SeedToSoilDict[x]
                x+=SoilToFertilizerDict[x]
                x+=FertilizerToWaterDict[x]
                x+=WaterToLightDict[x]
                x+=LightToTempDict[x]
                x+=TempToHumidityDict[x]
                x+=HumidityToLocationDict[x]
                if x < runnin:
                    runnin = x
                    print(runnin)
                    total+=1
                    print(total,"completed")
        print(runnin)
main()