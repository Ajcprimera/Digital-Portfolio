import modules_conditions as md
import options as pt
import operations as op

def main():
    print('='*20)
    print('Welcome to matrix calculator')
    print('='*20, '\n')

    print('Please the select the option of would you like to create your matrix', '\n')
    print('* 1. Generate a matrix introducing your own values')
    print('* 2. Generate a matrix with ramdom numbers')
    user_selection_1 = md.module_1()
    m1 = pt.matrix_options(user_selection_1)
    print('Would you like to create another matrix for oporations with 2 matrix? yes/no')
    user_selection_2 = input('=> ')
    user = md.module_2(user_selection_2)
    if user != None:
        m2 = pt.matrix_options(user)
        md.module_3(m1, m2)
    md.module_3(m1, user)

def again(user):
    while True:
        try:
            if user == 'yes':
                main()
            elif user == 'no':
                break
            else:
                raise Exception ('This option is not valid')
        except Exception as error:
                print(error)
        user = int(input('=> '))



if __name__ == '__main__':
    main()
    again(user = input('Would you like to use again the matrix calculator? yes/no: '))