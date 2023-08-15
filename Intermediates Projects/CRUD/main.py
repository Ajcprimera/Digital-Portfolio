import connection
import operations

def main():
    print('***WELCOME TO EMPLOYEES MANAGEMENT PAYMENT METHOD***')
    while True:
        print('Please choose the options below:')
        print('1- View data employment')
        print('2- Add new employee')
        print('3- Delete employee')
        print('4- Pay employee')
        print('5- Update Employee')
        print('6- Exit program')
        user_selection = int(input('=> '))

        if user_selection < 1 or user_selection > 6:
            print('This option is not valid')
        elif user_selection == 6:
            print('See you soon')
            break
        else:
            options(user_selection)

def options(option):
    connect = connection.connectdb()
    try:
        if option == 1:
                data = connect.listEmployees()
                if len(data) > 0:
                    operations.opt1(data)
                else:
                    print("you don't have employees in your data base")
        elif option == 2:
            employee = operations.opt2()
            connect.addemployee(employee)
        elif option == 3:
            data = connect.listEmployees()
            if len(data) > 0:
                operations.opt1(data)
                total ,id = operations.opt3(data)
                if id == None:
                    print('Id not found')
                else:
                    connect.removeemployee(id)
            else:
                print("you don't have employees in your data base")
            
        elif option == 4:
                data = connect.listEmployees()
                if len(data) > 0:
                    operations.opt1(data)
                    total, id = operations.opt4(data)
                    if id == None:
                        print('Id not found')
                    else:
                        if isinstance(total, str):
                            print(total)
                        else:
                            print("You'll recieve the amount of ", total, "according the numbers of fouls")
                else:
                    print("you don't have employees in your data base")
        elif option == 5:
            data = connect.listEmployees()
            if len(data) > 0:
                operations.opt1(data)
                employee, id = operations.opt5(data)
                if id == None:
                    print('Id not found')
                else:
                    connect.updateemployee(employee, id)
            else:
                print("you don't have employees in your data base")
    except:
            print('Something goes wrong, try again')
        

if __name__ == '__main__':
    main()