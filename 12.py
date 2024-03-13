def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2
    return count

def find_triangle_number_with_over_n_divisors(n):
    triangle_number = 1
    natural_number = 2
    while True:
        if count_divisors(triangle_number) > n:
            return triangle_number
        triangle_number += natural_number
        natural_number += 1

# Finding the first triangle number with over 500 divisors
first_triangle_number = find_triangle_number_with_over_n_divisors(500)
print("The first triangle number with over 500 divisors is:", first_triangle_number)
