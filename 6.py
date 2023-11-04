a = 1
b = 100
sum = 0
for i in range(a, b+1):
    sum = sum + i
sum = sum * sum
x = 0
sum_2 = 0 
for i in range(a, b+1):
    x = i * i
    sum_2 = sum_2 + x
print(sum - sum_2)