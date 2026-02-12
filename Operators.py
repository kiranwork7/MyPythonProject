# arithmatic operators
a = 10
b = 4
print(a+b)      # addition
print(a-b)      # subtraction
print(a*b)      #multiplication
print(a/b)      #division , may give float value
print(a//b)     # round up to the nearest integer value
print(a%b)      # give modulus( baki)
print(a**2)     # like square , cube , depend on second value

# Comparison operators, return boolean value true or false
print(a>b)         # return true if a is greater than b
print(a<b)         # return true if a is less than b
print(a==b)        # return if a is equal to b
print(a!=b)        # return true if a is not equal to b
print(a>=b)        # return true if a is greater than or equal to b
print(a<=b)        # return true if a is less than or equal to b

# Logical Operators
print(a>5 and b<5)             # return true when both conditions match
print(a>5 or b>5)              # return true when at least one conditions match
print(not(a>5 and b<5))        # return reverse result


# Identify operators
print(a is b)                  # return true if value of a is same as b
print(a is not b)              # return true if value of a is different than b

# Membership operators
Months = ["Jan", "Feb", "Mar", "Apr"]

print("Jan" in Months)         #return true if jan is present in Months list
print("Feb" in Months)         #return true if feb is present in Months list
print("June" in Months)        #return true if june is present in Months list
print("May" not in Months)     #return true if may is not present in Months list

