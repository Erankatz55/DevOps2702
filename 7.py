a = ["daniel", "Roei", "Moti"]
if "Shmulik" in a:
    print("Shmulik")
else:
    print("There is no Shmulik")


first_array = []
second_array = [1, 2, 3]
if not first_array:
    print("first has no items")
if second_array:
    print("second has no items")
if len(second_array) > 2:
    print("we have at least 3 items in second")


d = 5
g = 5
f = [1, 2, 3]
h = [1, 2, 3]
if d is g:
    print("d is g")
if f is h:
    print("f is h")
if type(d) is int:
    print("d is int")
    