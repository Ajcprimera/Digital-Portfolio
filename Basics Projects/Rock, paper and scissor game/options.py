import random

def user_options():
    user_option = input('rock, paper or scissor: ')
    user_option = user_option.lower()
    if not user_option in ('rock','paper','scissor'):
        print('This option isnt valid')
        return None
    return user_option


def computer_option():
    computer_option = random.choice(('rock','paper','scissor'))
    return computer_option

