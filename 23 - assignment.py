# 1

a = 1/0

# 2

try:
    a = 1/0
except ZeroDivisionError as e:
    print("could not divide by zero")
    print(e.args)

# 3 yes

# 4 Built in and user defined

# 5  Not giving enough information.

# 6
# except IOError - input and output errors.
# except ZeroDivisionError - error of divide a number with 0.

# 7

new_file = open("words.txt", "w")

# 8

new_file = open("words.txt", "w")
new_file.write(f"Eran")
new_file.close()

# 9

new_file = open("words.txt", "r")
print(new_file.read())
new_file.close()

# 10

new_file = open("words.txt", "r+", encoding='utf-8')
new_file.write(f"ערן")
new_file.close()

new_file = open("words.txt", "r")
print(new_file.read())
new_file.close()

