def test(num):
    temp = num
    a = [1,2,3,4,5,6]
    a[0] = int(temp % 10)
    a[1] = int((temp/10) %10)
    a[2] = int((temp/100) %10)
    a[3] = int((temp/1000) %10)
    a[4] = int((temp/10000) %10)
    a[5] = int((temp/100000) %10)
    #print(a[0] ,a[1] ,a[2] ,a[3] ,a[4] ,a[5])
    if(temp/100000 == 0):
        a[0] = 0
        if(a[1] == a[5] and a[2] == a[4]):
            return 1
    else:
        #a[0] = (temp/100000) %10
        if(a[0] == a[5] and a[1] == a[4] and a[2] == a[3]):
            return 1
        else:
            return 0

max = 0

for i in range(100 , 1000):
    for j in range(100, 1000):
        result = i * j
        if (result > max):
            n = test(result)
            #print(result)
            if (n == 1):
                print (result)
                max = result
