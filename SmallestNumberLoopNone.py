smallest = None
print("Before")
for the_num in (9, 51, 12, 3, 73, 14):
    if smallest is None:
        smallest = the_num
    elif the_num < smallest:
        smallest = the_num
    print(smallest, the_num)
print("after", smallest)