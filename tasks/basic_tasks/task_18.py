def first_last_same(items):
    first_num = items[0]
    last_num = items[-1]
    #check 
    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("The answer is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("The answer is", first_last_same(numbers_y))
