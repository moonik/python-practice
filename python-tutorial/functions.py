def addNumbeer(first, second):
    return first + second


print(addNumbeer(1, 2))

myString = "Hello Roman"

print(myString[0:3])  # chars from 0 to 2

print(myString[-3:])  # last 3 chars

print(myString[:-3])  # full string except last 3 chars

print(myString[:5] + " Romchik")  # concatenation of first 5 chars and word Romchik

print("%c is my %s letter and my number %d number is %.5f" %
      ("R", "favourite", 13, .14))

print(myString.capitalize())

print(myString.find("Roman"))

print(myString.isalpha())

print(myString.isalnum())



