# A
x = 5
y = 7
if x > y:
    print("BIG")
if x < y:
    print("small")

# B
for i in range(1, 6):
    print(i)

# C
for season in range(1, 5):
    if season == 1:
        print("summer")
    elif season == 2:
        print("winter")
    elif season == 3:
        print("fall")
    else:
        print("spring")

# D
10

# E
age = 32
letter = "E"
currency = 3.59
flew = True
apartment = 14
print(age, letter, currency, flew, apartment)
print(age + currency)

# F
phone = input("Enter your phone number: ")
print("your phone number is: ", phone)

# G
def printHello():
    print("hello")
def calculate():
    print("5+3.2=", 5+3.2)

printHello()
calculate()

# H
def yourName(name):
    print(name)
def divideNumber(number):
    print("Your number divided by 2 equal to:", number / 2)

yourName("eran")
divideNumber(8)

# I
def twonum(a, b):
    return (a + b)
def twostring(str1, str2):
    string = str1 + " " + str2
    return (string)

twonum(4, 7)
twostring("Hello", "World")

# L
len = 7
for K in range(len):
    for J in range(len):
       if (K == J) or (K + J == len-1):
           print("#", end="")
       else:
           print(" ", end="")
    print()
