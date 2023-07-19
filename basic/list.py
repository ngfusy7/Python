# mylist = ["apple", "cherry", "pinapple"]

# print(mylist)

# print(type(mylist)) 

#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry"))
print(thislist[-1])  

#-1 refers to the last item, -2 refers to the second last item etc. ~ index

# thislist[1] = "orange"
# print(thislist)

#Insert Items in list

# thislist.insert(2, "watermelon")


#To add an item to the end of the list, use the append() method:

# thislist.append("chicken")


# The remove() method removes the specified item.
# thislist.remove("banana")


#The pop() method removes the specified index.
thislist.pop(1)

print(thislist)
