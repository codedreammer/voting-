print("Welcome to the Voting Machine!")
name = input("Enter the your name: ")
Id = float(input("Enter your voter Id: "))
bjp_votes = 0
congress_votes = 0
total_voters = 0

while total_voters < 10:
    print("Voter", total_voters + 1)
    age = int(input("Enter your age: "))

    if age < 18:
        print("You can't vote")
        continue
    
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
        
        total_voters += 1

    print("Voting has ended!")
    print("Total votes for BJP", bjp_votes)
    print("Total votes for congress:", congress_votes)

    if bjp_votes > congress_votes:
        print("BJP is the winnwer!")
    elif congress_votes > bjp_votes:
        print("Congress is the winner!")
    else:
        print("Its's a Tie!")
        