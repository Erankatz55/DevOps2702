names = ["inbar", "yanir", "eran", "kfir", "alina"]
print(list(range(20, 1, -3)))
for name in names:
    print(name, end=',')

for i in range(30):
    print(i)


for c in range(len(names)):
    names[c] = "liran"
    print(c)

a = 0
while a < 5:
    print(a)
    a = a + 1

for number in numbers:
    if number == 3:
        continue
    if number == 2:
        break
    print(number)
else:
    print("Finish")