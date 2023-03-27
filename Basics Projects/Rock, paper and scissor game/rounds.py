import conditions
import options

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('=' * 10)
    print('ROUND', rounds)
    print('=' * 10,'\n')

    print('Computer wins: ', computer_wins)
    print('User wins: ', user_wins)
    rounds += 1

    user_option = options.user_options()
    computer_option = options.computer_option()
    user_wins, computer_wins = conditions.check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('Computer wins', '\n')
      break

    if user_wins == 2:
      print('User wins', '\n')
      break
