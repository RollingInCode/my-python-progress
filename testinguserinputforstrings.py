def hardware(i):
    i = i + 1
    return i
    
count = 0
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
    while (count != 8):
        count += hardware(count) ## Function is called and needs to return an int
        print(counter) ## Used as a counter variable

        

    
