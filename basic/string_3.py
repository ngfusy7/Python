# str = "Hello World!"

# print(str.upper())
# print(str.lower())
# print(str.strip())

# a = "Hello"
# b = "World"
# c = a + b
# print(c)

#Format String
age = 36
str = "I am {} years old"
print(str.format(age))


price = 36
day = 17 
gate = 5
str1 = "Gate number {2} with {0} ticket in day {1}"
print(str1.format(price,day,gate))