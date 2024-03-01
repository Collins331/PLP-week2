user_list = []
sum = 0
# Infinite loop that breaks on when user prints sum
while True:
    option = int(input("Reply:\n\t1. Add integer\n\t2. Print sum of integers added\n__: "))
    
    if (option == 1):
        # user integer input
        user = int(input("\nPlease enter a valid integer: "))
        user_list.append(user)
    elif (option == 2):
        # adding integers added in the list by user
        for num in user_list:
            sum += num
        print(f"The total sum is:  {sum}")
        break
