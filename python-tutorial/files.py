import os

test_file = open("text.txt", "wb")  # wb - for writing

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Write me to the file\n", "UTF-8"))

test_file.close()

test_file = open("text.txt", "r+")  # for reading and writing

text_in_file = test_file.read()

print(text_in_file)

os.remove("text.txt")
