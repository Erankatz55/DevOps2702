n = input("Enter 5 ages separated by space: ")  # enter 5 numbers as 1 string
ages = [int(d) for d in n.split()]  # split the inputted string to a list, convert each element to an integer, store ver
x = 0  # variable to compare
for age in ages:
    if age > x:
        x = age  # stores the higher value in x
print("the oldest age is: ", x)


# write a function the get name as input
# from the user until the name 'moshe' and return a list of those names

def GetName():
    names = []
    name = input("enter a name: ")
    while name != "moshe":
        names.append(name)
    return names


GetName()
