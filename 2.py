first = 0
second = 1
x = 0
sum = 0
for i in range(1, 10000000):    
    if x < 4000000 :
        x = first + second
        first = second
        second = x
        i +=1
        if x % 2 == 0 :
            sum += x
    else : 
        break
    
print(sum)