def prob1(instring):
    return firstnlast(instring)
def prob2(instring,indict):
    print(instring)
    workstr=""
    workstrcpy=""
    done = False
    for x in instring:
        if x.isdigit():
            break
        workstr+=str(x)
        for y in indict:
            if y in workstr:
                workstrcpy = workstr.replace(y,indict.get(y))
                done = True
                break
        if done == True:
            break
    done = False
    if workstrcpy!="":
        instring = instring.replace(workstr,workstrcpy)
    #print(instring)
    workstr = ""
    workstrcpy = ""
    for i,x in enumerate(reversed(instring)):
        if x.isdigit():
            break
        workstr = x+workstr
        for y in indict:
            if y in workstr:
                #print(workstr)
                workstrcpy = workstr.replace(y,indict.get(y))
                editlist = list(instring)
                editlist[len(instring)-i-1::]=list(workstrcpy)
                #print(editlist)
                instring = "".join(editlist)
                #print(workstrcpy)
                done = True
                break
        if done == True:
            break
    print(instring)
    return firstnlast(instring)
def firstnlast(instring):
    sum = ""
    for x in instring:
        if x.isdigit():
            sum+=str(x)
            break
    for x in reversed(instring):
        if x.isdigit():
            sum+=str(x)
            break
    return int(sum)
            

def main():
    with open("data.txt") as f:
        lines = f.readlines()
    sum = 0
    mydict = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    for x in lines:
        sum+=prob2(x,mydict)
    print(sum)
        
main()