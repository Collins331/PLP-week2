set1 = set()
set2 = set()

while True:
    add = int(input("Add integer to:\n\t1. Set 1\n\t2. Set 2\n3. Add the sets\n___: "))
    if (add == 1):
        num1 = int(input("Enter valid integer: "))
        set1.add(num1)
    elif (add == 2):
        num2 = int(input("Enter valid integer: "))
        set2.add(num2)
    elif (add == 3):
        print(f"Common elements : {set1 & set2}")
        break
    else:
        print("Invalid input")