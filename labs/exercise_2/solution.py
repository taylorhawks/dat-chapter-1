def even_fibonacci(number):
    a, b = 0, 1
    while a < number:
        if a % 2 == 0:         
            yield a
        c = b
        b = b + a
        a = c
print sum(even_fibonacci(4000000))
