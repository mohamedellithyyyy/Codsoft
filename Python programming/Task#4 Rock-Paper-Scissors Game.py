import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        print("Welcome to Rock-Paper-Scissors Game!")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1
        
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

if __name__ == "__main__":
    main()
