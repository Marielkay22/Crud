users = []

while True:
    print("\nMenu")
    print("1 - Show Users")
    print("2 - Add User")
    print("3 - Update User")
    print("4 - Delete User")
    print("5 - Exit")

    choice = input("Choose number: ")

    if choice == "1":
        if users == []:
            print("No users yet.")
        else:
            print("Users:")
            for i in range(len(users)):
                print(i+1, users[i])

    elif choice == "2":
        name = input("Enter name: ")
        users.append(name)
        print("User added.")

    elif choice == "3":
        if users == []:
            print("Nothing to update.")
        else:
            for i in range(len(users)):
                print(i+1, users[i])
            num = int(input("Enter number to update: "))
            new_name = input("Enter new name: ")
            users[num-1] = new_name
            print("User updated.")

    elif choice == "4":
        if users == []:
            print("Nothing to delete.")
        else:
            for i in range(len(users)):
                print(i+1, users[i])
            num = int(input("Enter number to delete: "))
            users.pop(num-1)
            print("User deleted.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")



