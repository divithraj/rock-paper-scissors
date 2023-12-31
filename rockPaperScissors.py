import random

def rockPaperScissors(userChoice, computerChoice):
    if userChoice != "rock" and userChoice != "scissors" and userChoice != "paper":
        return "Invalid Choice. Please select rock, paper, or scissors."
    
    if userChoice == computerChoice:
        return "Tie Game.  You both selected: " + userChoice 
    else:
        if userChoice == "rock" and computerChoice == "paper":
            return "You lose. Paper beats Rock."
        if userChoice == "rock" and computerChoice == "scissors":
            return "You win.  Rock beats Scissors."
        if userChoice == "paper" and computerChoice == "rock":
            return "You win. Paper beats Rock."
        if userChoice == "paper" and computerChoice == "scissors":
            return "You lose.  Scissors beats paper."
        if userChoice == "scissors" and computerChoice == "paper":
            return "You win. Scissors beats Paper."
        if userChoice == "scissors" and computerChoice == "rock":
            return "You lose.  Rock beats Scissors."

# Start the game loop
while True:
    userChoice = input("\nRock, Paper, or Scissors? (or type 'exit' to quit) ").lower().strip()
    
    # Check if user wants to exit
    if userChoice == "exit":
        print("Thanks for playing!")
        break

    options = ["rock", "paper", "scissors"]
    computerChoice = random.choice(options)
    print(rockPaperScissors(userChoice, computerChoice))