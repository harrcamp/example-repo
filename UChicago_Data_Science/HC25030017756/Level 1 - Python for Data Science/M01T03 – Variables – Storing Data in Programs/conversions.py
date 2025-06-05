
# declare variables

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# convert variables between data types

num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

# print new data types for arguements on separate lines checking the type using f-string

print(f"{num1} is a {type(num1)}")
print(f"{num2} is a {type(num2)}")
print(f"{num3} is a {type(num3)}")
print(f"{string1} is a {type(string1)}")

# using empty placeholders
print("{} is a {}".format(num1,type(num1)))

# using indexes

print("{0} is a {1}".format(num1, type(num1)))