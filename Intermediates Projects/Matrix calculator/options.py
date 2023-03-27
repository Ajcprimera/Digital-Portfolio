import convertion

def matrix_options(user_selection):
    while True:
        try:
            if user_selection == 1:
                while True:
                    try:
                        rows = int(input('Input the number of rows: '))
                        columns = int(input('Input the number of columns: '))
                        selection = convertion.convertion_u(rows, columns)
                        return selection
                    except ValueError:
                        print('The value that you introduce is not a number, try again')
            elif user_selection == 2:
                while True:
                    try:
                        rows = int(input('Input the number of rows: '))
                        columns = int(input('Input the number of columns: '))
                        selection = convertion.convertion_r(rows, columns)
                        return selection
                    except ValueError:
                        print('The value that you introduce is not a number, try again')
            elif user_selection != 1 and user_selection != 2:
                raise Exception ('This option does not exist')
        except Exception as error:
            print(error)
        try:
            user_selection = int(input('=>'))
        except ValueError:
            print('The value that you introduce is not a number, try again')