import random
playing = True

while playing:
    user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    choices = "rock", "lizard", "scissors", "paper", "spock"
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        print("It's a tie")

    elif user_choice == "rock" and computer_choice == "lizard":
        print(user_choice + " crushes " + computer_choice+". You win!")

    elif user_choice == "rock" and computer_choice == "scissors":
        print(user_choice + " destroys " + computer_choice+". You win!")

    elif user_choice == "paper" and computer_choice == "spock":
        print(user_choice + " disproves " + computer_choice+". You win!")

    elif user_choice == "paper" and computer_choice == "rock":
        print(user_choice + " covers " + computer_choice+". You win!")

    elif user_choice == "scissors" and computer_choice == "paper":
        print(user_choice + " cuts " + computer_choice+". You win!")

    elif user_choice == "scissors" and computer_choice == "lizard":
        print(user_choice + " decapitates " + computer_choice+". You win!")

    elif user_choice == "lizard" and computer_choice == "paper":
        print(user_choice + " eats " + computer_choice+". You win!")

    elif user_choice == "lizard" and computer_choice == "spock":
        print(user_choice + " poisons " + computer_choice+". You win!")

    elif user_choice == "spock" and computer_choice == "scissors":
        print(user_choice + " smashes " + computer_choice+". You win!")

    elif user_choice == "spock" and computer_choice == "rock":
        print(user_choice + " vaporizes " + computer_choice+". You win!")
    else:
        print("Invalid Input!")

    playing = False
    play_again = input("Play again? (yes / no)").lower()
    if play_again == "yes":
        playing = True
print("Bye")
