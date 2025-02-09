def times12(n):
    for i in range(12,n+1,12):
        yield i

for i in times12(44):
    print(i)