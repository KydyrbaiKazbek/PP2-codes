from math import tan, radians
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area = n/4*l*l/tan(radians(180/n))
print(f"The area of the polygon is: {area}")