
## python3

mylist = {"foo":"bar", "foobo":"foobar"}

width_col1 = max([len(x) for x in mylist.keys()])
width_col2 = max([len(x) for x in mylist.values()])

def f(ind):
    return mylist[ind]

for i in mylist:
    print("|{0:<{col1}}|{1:<{col2}}|".format(i,f(i),col1=width_col1,
                                            col2=width_col2))
                                            
 
