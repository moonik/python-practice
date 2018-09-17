# comment

'''
Multiline
'''

# Data types
# Numbers, Strings, Lists, Tuples, Dictionaries (maps)

# ** - powers. e.g. 2 ** 3 = 8

# // - floor division  5 // 2 = 2

list = ["first", "second", "third"]

print("First item", list[0])

print("From 1 to 3", list[1:3])

list[2:] # from second index
list[:2] # to second index

anotherList = ["five", "six", "seven"]

storage = [list, anotherList]  # [][]

print(storage)

list.insert(0, "zero")
list.append("nine")
list.sort()
list.remove("nine")
list.reverse()

del anotherList[0]  # deletes first element

print(list)
print(anotherList)

list2 = list + anotherList  # two list in one

print(list2)

