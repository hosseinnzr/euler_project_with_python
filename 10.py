def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print (sumPrimes(2000000))

#142913828922

#تان هاش

#برنامه دوم
def prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        #print(i)
        if not num % i:
            return False
    return True

result = 2

for i in range(3, 2000000,2):
    if prime(i):
        result += i
        
print(result)



#sum = 0
#ar = [2]
#for i in range(1 , 2000000):
#   # print(sum)
#    test= True
#    for j in range(0, i+1):
#        #print(ar[j])
#        print(j)
#        if i % ar[j] == 0 :
#            test = False
#    if test :
#        ar.append(i)
#        sum += i
#