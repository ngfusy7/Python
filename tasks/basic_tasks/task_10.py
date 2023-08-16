n = int(input("Enter N: "))
temp = str(n)


t1 = temp + temp
t2 = temp + temp + temp

comp = n + int(t1) + int(t2)
print(f"The value is {comp}")
