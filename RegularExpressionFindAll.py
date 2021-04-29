import re
book=open("bible.txt")
sean = re.findall("tion", book)
print(sean)