def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    prime_count = 1
    num = 1
    while prime_count < n:
        num += 2
        if is_prime(num):
            prime_count += 1
    return num

nth_prime = 10001
result = find_nth_prime(nth_prime)
print("The", nth_prime, "st prime number is:", result)
