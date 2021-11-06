def print_triangular_numbers(n):
    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        print(i,'       ',sum)
        i += 1
