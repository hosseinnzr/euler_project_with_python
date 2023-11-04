a = 0
b = 0 
c = 0
s = 1000
found = False
for a in range(1, 1000):
    a +=1
    if a < s / 2 :
        for b in range(a, 1000):
            #print(a,b)
            if b < s / 2:
                b +=1
                c = s - a - b
                if (a * a + b * b == c * c):
                    found = True
                    break   
    if (found):
        print(a*b*c)
        break