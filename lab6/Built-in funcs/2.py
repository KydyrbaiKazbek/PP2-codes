inp = "HeloajfoijfIJHijfksnNJn"
def checkUpper(s): return s.isupper()
def checkLower(s): return s.islower()    
print("Upper-case letters are ", sum(map(checkUpper, inp)))
print("Lower-case letters are ", sum(map(checkLower, inp)))