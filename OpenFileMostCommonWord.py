name = raw_input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    bigword=word
    bigcount=count

print(bigword, bigcount)
##opens file and finds most common word and amount