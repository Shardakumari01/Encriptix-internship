import random

def get_computer_choice():
    choices = ["rock","paper","scissor"]
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissor): ").lower()
    while user_input not in ["rock", "paper", "scissor"]:
        user_input = input("Invalid choice. Please enter rock, paper, or scissor: ").lower()
    return user_input

def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return"It is a tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissor" and computer_choice == "paper"):
        return "You win!"
    else:
       return "Computer wins!"
    
def play_game():
    while True:
         user_choice = get_user_choice()
         computer_choice = get_computer_choice()
         print(f"\nYou choose: {user_choice}")
         print(f"\ncomputer choose: {computer_choice}")

         result = determine_winner(user_choice, computer_choice)
         print(f"\n{result}\n")

         play_again = input("Do you want to play again? (yes/no): ").lower()
         if play_again != "yes":
             break
         
if __name__ == "__main__":
    play_game()


       
