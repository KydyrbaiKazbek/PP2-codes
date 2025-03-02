from functools import reduce
from operator import mul
l = [1,2,4,4,5,6]

ans = reduce(mul, l)
print(ans)