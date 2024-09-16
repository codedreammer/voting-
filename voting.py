print("Welcome to the Voting Machine!")
age = int(input("Enter your age: "))

if age < 18:
    print("You can't vote")
else:
    print("You can vote!")
    print("Choose your party:")
    print("1. BJP")
    print("2. Congress")

    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        print("You voted for the BJP. Thank you!")
    elif choice == "2":
        print("You voted for the Congress. Thank you!")
    else:
        print("Invalid choice. Please select 1 for BJP or 2 for Congress.")
