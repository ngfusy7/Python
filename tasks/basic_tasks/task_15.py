#Print the sum of the current number and the previous number

previous_number = 0
for i in range(1,11):
    sum = previous_number + i
    print("Current Number ", i, "Previous Number ", previous_number, "Sum ", sum)
    previous_number = i 