fhand = open("bible.txt")
counts = dict()
for lines in fhand:
    line = lines.rstrip()
    word = line.split()
    for words in word:
        counts = counts.get(word, 0) + 1

lst = list()
for key,val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst =sorted(lst, reverse=True)

for val, key in lst[:10]:
        print(key, val)
