x = "Hello World"               # method 1 for string declaration
print(x)
y = str("how are you? ")        # method 2 for declration
print(y)

print(type(x))                  # data type identification
print(type(y))                  # data type identification


a = "FooBoo"
#Get the characters from the start to position 4
print(a[4])                     # this will print 4th letter from start
print(a[2:5])                   # this will print from 2nd position to 5th position

#  case methods upper() and lower()
print(a.upper())
print(a.lower())
print(a.index("B"))             # return index of B


# replace() method , replacing Boo by Zoo
print(a.replace("Boo", "Zoo"))

#concatenate string
b = "Foo"
c = "Boo"
print(b + c)                     #print FooBoo



