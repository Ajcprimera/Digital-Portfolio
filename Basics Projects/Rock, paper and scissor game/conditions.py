def check_rules(user_option, computer_option, user_wins, computer_wins):
    if computer_option == "rock" and user_option == "paper":
        print("You win, paper wins againts rock")
        user_wins += 1
    elif computer_option == "paper" and user_option == "scissor":
        print("You win, scissor wins againts paper")
        user_wins += 1
    elif computer_option == "scissor" and user_option == "rock":
        print("You win, rock wins againts scissor")
        user_wins += 1
    if computer_option == "paper" and user_option == "rock":
        print("You lose, paper wins againts rock")
        computer_wins += 1
    elif computer_option == "scissor" and user_option == "paper":
        print("You lose, scissor wins againts paper")
        computer_wins += 1
    elif computer_option == "rock" and user_option == "scissor":
        print("You lose, rock wins againts scissor")
        computer_wins += 1
    elif computer_option == user_option:
        print("Tie")
    return user_wins, computer_wins