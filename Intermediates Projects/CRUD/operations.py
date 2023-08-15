from tabulate import tabulate
import operations

def opt1(data):
    print(tabulate(data, headers= ['id', 'Name', 'Salary ($)', 'Fouls']))

def opt2():
    name = input('Introduce a name => ')
    salary = int(input('Introduce the salary =>'))
    fouls = int(input('Introduce the amount of fouls (max 3)=> '))
    while True:
        if fouls >= 0 and fouls <= 3:
            employee = (name, salary, fouls)
            return employee
        else:
            fouls = int(input('Introduce the amount of fouls again=> '))

def opt3(data):
    id = int(input('Introduce the id of the employee => '))
    condition = False
    for i in data:
        if i[0] == id:
            condition = True
            break
    if not condition:
        id = None
    return id

def opt4(data):
    id = int(input('Introduce the id of the employee => '))
    condition = False
    for i in data:
        if i[0] == id:
            if i[3] == 1:
                percent = i[2] * 0.3
                total = i[2] - percent
                print(total)
                condition = True
                break
            elif i[3] == 2:
                percent = i[2] * 0.3
                total = i[2] - percent
                condition = True
                break
            elif i[3] == 3:
                total = str("You have exceeded the numbers of fouls, you won't recieve your paid")
                condition = True
                break
            else:
                total = i[2]
                condition = True
                break
    if not condition:
        id = None
    return total ,id

def opt5(data):
    id = int(input('Introduce the id of the employee => '))
    condition = False
    for i in data:
        if i[0] == id:
            condition = True
            name = input('Introduce a name => ')
            salary = int(input('Introduce the salary =>'))
            fouls = int(input('Introduce the amount of fouls (max 3)=> '))
            employee = (name, salary, fouls)
            break
    if not condition:
        id = None
    return id, employee

        
    
    