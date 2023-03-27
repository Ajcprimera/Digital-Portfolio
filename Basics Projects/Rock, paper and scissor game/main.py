import rounds

def game ():
    print('*' * 40)
    print('Welcome to rock, paper and scissor game')
    print('*' * 40)
    rounds.run_game()
    while True:
        play_again = input('Would you like to play again? (yes/no): '.lower())
        
        try:
            if play_again == 'yes':
                rounds.run_game()
            elif play_again == 'no':
                print('Have a nice day!')
                break
            elif play_again != 'no' or play_again != 'yes':
                raise Exception ('This option is not valid')
        except Exception as error:
            print(error)
            
game()