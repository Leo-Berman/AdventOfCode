def cubeneeds(input):
    ret = [0,0,0]
    for x in input: 
        if x[1] == 'red' or x[1] =='red,':
            ret[0]+=int(x[0])
        elif x[1] == 'green' or x[1] == 'green,':
            ret[1]+=int(x[0])
        elif x[1] == 'blue' or x[1] == 'blue,':
            ret[2]+=int(x[0])
    return ret
def isvalid(test):
    if test[0] <= 12 and test[1] <= 13 and test[2] <= 14:
        return True
    else:
        return False
        

def main():
    with open("data2.txt") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if i < 10:
            lines[i] = lines[i][7::]
        elif i == 99:
            lines[i] = lines[i][9::]
        else:
            lines[i] = lines[i][8::]
    #print(lines)
    mydict = {}
    for i in range(len(lines)):
        work = lines[i].split(";")
        work = [str(x).strip() for x in work]
        mydict.update({i+1:work})
    sum = 0 
    check = False
    
    # pick problem
    prob = 1
    # Prob 1
    if prob == 1:
        for i in range(len(lines)):
            work = mydict.get(i+1)
            #print(work)
            for x in work:
                #print(x)
                x = x.split(",")
                x = [y.strip() for y in x]
                x = [y.split(" ") for y in x]
                #print(x)
                if(isvalid(cubeneeds(x)))==False:
                    #print(x)
                    check=True
                    #print(i)
                    #print(i+1,x)
                    #sum+=i+1
                    #break
            if check:
                check = False
            else:
                sum+=i+1
    elif prob ==2:
        for i in range(len(lines)):
            work = mydict.get(i+1)
            #print(work)
            set = [0,0,0]
            for x in work:
                #print(x)
                x = x.split(",")
                x = [y.strip() for y in x]
                x = [y.split(" ") for y in x]
                #print(x)
                comp = cubeneeds(x)
                if comp[0] > set[0]:
                    set[0] = comp[0]
                if comp[1] > set[1]:
                    set[1] = comp[1]
                if comp[2] > set[2]:
                    set[2] = comp[2]
            add = set[0]*set[1]*set[2]
            sum+=add
        
    print(sum)

    #lines = [x.split(";") for x in lines]
    #print(lines)
    #lines = [x.split(",") for x in lines]
    #for i in range(len(lines)):
    #    for j in range(len(lines[i])):
    #        lines[i][j] = lines[i][j].strip().split(" ")
            
main()