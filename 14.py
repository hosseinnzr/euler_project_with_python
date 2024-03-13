def collatz_length(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    elif n % 2 == 0:
        length = 1 + collatz_length(n // 2, memo)
    else:
        length = 1 + collatz_length(3 * n + 1, memo)
    memo[n] = length
    return length

def longest_collatz_chain(limit):
    max_length = 0
    starting_number = 0
    memo = {}
    for i in range(1, limit):
        length = collatz_length(i, memo)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number, max_length

limit = 1000000
start, length = longest_collatz_chain(limit)

print(start)
