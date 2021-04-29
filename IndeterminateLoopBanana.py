fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#use 'for' loop when you can instead of while
#less code is better
#fruit = 'banana'
for letter in fruit:
    print(letter)

#letter count 'a'
word = "banana"
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)