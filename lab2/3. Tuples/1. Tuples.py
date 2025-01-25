#1 
mytuple = ("apple", "banana", "cherry")

#2 
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#3 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#4 
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#5
thistuple = ("apple",)
print(type(thistuple))

    #NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#6
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#
tuple1 = ("abc", 34, True, 40, "male")

#
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)