runtotal=0
sumtotal=0
print("Before", runtotal)
for number in (9, 42, 12, 3, 74, 15):
    runtotal = runtotal + 1
    sumtotal = sumtotal + number
    print(runtotal, sumtotal, number)
print ("RunTimes/Sum/Average", runtotal, sumtotal, sumtotal/runtotal)
#count how many times a loop gets executed runtotal
#calculate average by dividing sumtotal by runtotal