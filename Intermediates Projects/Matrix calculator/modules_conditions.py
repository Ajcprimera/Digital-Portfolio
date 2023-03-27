from operations import Operation
def module_1():
    while True:
        try:
            user_selection = int(input('=> '))
            return user_selection
        except ValueError:
            print('The value that you introduce is not a number, try again')

def module_2(matrix_generator_condition):
    while True:
        try:
            if matrix_generator_condition == 'yes':
                print('* 1. Generate a matrix introducing your own values')
                print('* 2. Generate a matrix with ramdom numbers')
                m2 = module_1()
                return m2
            elif matrix_generator_condition == 'no':
                return None
            elif matrix_generator_condition != 'no' or matrix_generator_condition != 'yes':
                raise Exception ('This option is not valid')
        except Exception as error:
            print(error)
        matrix_generator_condition = input('=> ')

def module_3(m1,m2):
    if type(m2) is list:
        print(m1)
        print(m2)
        print('This are the operations aviable with 2 matrix:')
        print('* 1. Sum of matrix')
        print('* 2. Substraction of matrix')
        print('* 3. Multiplication of matrix')
        option = int(input('=> '))
        solution = Operation()
        while True:
            try:
                if option == 1:
                    return solution.__sum__(m1,m2)
                elif option == 2:
                    return solution.__subtraction__(m1,m2)
                elif option == 3:
                    return solution.__multiply__(m1,m2)
                else:
                    raise Exception ('This option is not valid')
            except Exception as error:
                print(error)
            option = int(input('=> '))
    else:
        print(m1)
        print('This are the operations aviable with one matrix:')
        print('* 1. Determinant of a matrix')
        print('* 2. Inverse of a matrix')
        print('* 3. Prinipal diagonal of a matrix')
        print('* 4. Transpose of a matrix')
        option = int(input('=> '))
        solution = Operation()
        while True:
            try:
                if option == 1:
                    return solution.__determinant__(m1)
                elif option == 2:
                    return solution.__inverse__(m1)
                elif option == 3:
                    return solution.__diagonal__(m1)
                elif option == 4:
                    return solution.__transpose__(m1)
                else:
                    raise Exception ('This option is not valid')
            except Exception as error:
                print(error)
            option = int(input('=> '))