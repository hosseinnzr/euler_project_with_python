sum = 0 
m = 0
i=1
    while i < 1000000000:
        m = 0
        sum += i
        #print(sum)
        sum=76576500
        for j in range(1, sum+1):
            if sum%j == 0:
                m += 1
            if m == 500 :
                print("==========", sum)
                break
        i += 1