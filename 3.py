def avall(m):
    j=0
    for i in range(1, m+1):
        if m % i == 0 :
            j += 1
    if j == 2 :
        return True
    else:
        return False  

def prime_factors(n):
    for i in range(1, n+1):
        if n % i == 0 and avall(i):
            print (i)


prime_factors (600851475143)