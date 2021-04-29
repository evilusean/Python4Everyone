import urllib
import urllib.request,urllib.parse,urllib.error
counts=dict()
fhand =urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
