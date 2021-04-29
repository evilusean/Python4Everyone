d = {"a": 10, "b":1, "c":22}
d.items()
sorted(d.items())
#sorts items out of ([('a', 10), ('b', 1), ('c', 22)]) line to line by line
for k, v in sorted(d.items()):
    print(k,v)

#switches locations of key and value
tmp=list()
tmp.append((v,k))
#print(tmp)
tmp=sorted(tmp, reverse=True)
print(tmp)