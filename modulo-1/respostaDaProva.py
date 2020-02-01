a = 1
b = 3
c = 5

while b < a or b > a and c < 20:
    if a > c:
        c = c - 2
    else:
        c = c + 2
        if (a + b) < c:
            a = b - a
            b = b + 2
print('Os números são:', a, b, c)
