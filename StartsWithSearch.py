fname = input("Enter File Name: ")
try:
    fhand = open(fname)
except:
    print("File can not be opened.", fname)
    quit()

count = 0
for line in fhand:
    if line.startswith("Jesus"):
        count = count + 1
print("There were", count, "subject lines in", fname)
#if count == 0:
#    print("Ya'll need Jesus.")




#look = open("bible.txt")
#for line in look:
#    line = line.rstrip()
#    if line.startswith("Jesus"):
#        print(line)

#above is old version, less refined
#use rstrip to take away extra lines