import random
def main():
    userName  = input("Enter your name")
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    computer = random.choice(["rock","paper","scissors"])

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    
    elif user == "rock":
        if computer == "scicssors":
            print("Rock crushes scissors! and you win!",userName)
        else:
            print("Paper covers rock and you lose!",userName)
    
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! and you win!", userName)
        else:
            print("Scissors cuts paper and you lose!",userName)
    
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! and you win!",userName)
        else:
            print("Rock crushes scissors and you lose!",userName)
    else:
        print("Invalid choice! please choose rock , paper, scissors")

main()
    