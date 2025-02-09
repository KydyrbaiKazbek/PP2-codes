def decrease(n):
    for i in range(n,-1,-1):
        yield i

for i in decrease(5):
    print(i)