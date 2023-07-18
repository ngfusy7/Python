#single text
strA = "Hello"
print(strA)

#mutiple text 
strB = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(strB)

strC = "Canada"
print(strC[0]) 

#loop in string
for x in "banana":
    print(x)

#string length
print(len(strC))

#check string
text = "Hello everybody today i feel so good haha"
print("today" in text)

if "today" in text:
    print("Yes" )

#Slicing Strings
print(strC[2:5])

#Get the characters from the start to position 5
print(strC[:5])

#Get the characters from position 2, and all the way to the end
print(strC[2:])