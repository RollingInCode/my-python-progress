def collatz(number):
    if number % 2 == 0:      
        return number // 2        
    elif number % 1 == 0:
        return 3 * number + 1
        
for funLoop in range (1,10):
    taco = int(input())
    collatz(taco)
    print(taco)
