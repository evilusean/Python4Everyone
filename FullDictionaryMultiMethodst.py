fname = input("enter file: ")
if len(fname) < 1 : fname = "bible.txt"
hand=open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print lin
    wds=lin.split()
    #print(wds)
    for w in wds:
        #print('**',w,di.get(w,-99))                Here
        #if w in di:
            #di[w] = di[w] + 1
            #print("**Existing**")
        #else:
            #di[w] = 1
            #print("**New**")
        #print(w,di[w])                           to here old method below new method
        #if the key is not there the count is 0
        #oldcount= di.get(w,0)
        #print(w, oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount

        #if w in di :
            #di[w] = di[w] + 1
        #else:di[w] = 1

        #new new method idiom=retrieve/create/update counter
        di[w] = di.get(w,0) +1
        #print(w, di[w])

largest=-1
theword= None
for k,v in di.items():
    #print(k,v)
    if v > largest :
        largest = v
        theword = k

print(theword, largest)