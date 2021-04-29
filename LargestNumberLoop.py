largest_num_so_far = -1
print("Before", largest_num_so_far)
for the_num in (9, 51, 12, 3, 73, 14):
    if the_num > largest_num_so_far:
        largest_num_so_far = the_num
    print(largest_num_so_far, the_num)
print("after", largest_num_so_far)

