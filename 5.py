n = 0
f = 0
x = 1
for m in range(1, 21):
    for n in range(1, m+1):
        if m % n == 0:
            f += 1
    if f == 2:
        x *= m
        #print(m)
    f = 0
#print(x)

for i in range(0, 999999999, x):
    #print(i)
    n = 0
    for j in range(1, 21):
        if i % j  == 0:
            n += 1
            #print(n)
    if n == 20 :
        print(i)