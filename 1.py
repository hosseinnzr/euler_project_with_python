three = 0
five = 0
x = 0
for i in range(1, 1000):
    if i % 3 == 0 :
        three += i
    if i % 5 == 0 :
        five += i
    if i % 15 == 0 : 
        x += i
sum = three + five - x
print(sum)
