str = input("Enter string: ")

size = len(str)

for i in range(0, size-1, 2):
    print("index[", i, "]", str[i])
    