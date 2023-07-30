import click
import file_manager
import operator as o

@click.group()
def clic():
    pass

@clic.command()
@click.option('--name', required= True, help = 'Name of the user')
@click.option('--salary', required= True,type = int, help = 'Salary of the user')
@click.pass_context
def new_user(cl, name, salary):
    if not name or not salary:
        cl.fail('The name and the salary are required')
    else:
        data = file_manager.read_file()
        id_user = len(data) + 1
        new_user = {
            "id":id_user,
            "name":name,
            "salary":salary
        }
        data.append(new_user)
        file_manager.write_file(data)
        print(f"User {name} {salary} created sucessfully")


@clic.command()
def view_all_users():
    data = file_manager.read_file()

    if len(data) == 0:
        print("There's no users registered")
    for i in data:
        print(f"{i['id']} - {i['name']} - {i['salary']}$")

@clic.command()
def sort_salary_user():
    data = file_manager.read_file()
    s_data = sorted(data, key=o.itemgetter('salary'), reverse=True)
    for i in s_data:
        print(f"{i['id']} - {i['name']} - {i['salary']}$")

@clic.command()
@click.argument("id", type = int)
def find_user(id):
    data = file_manager.read_file()
    f_user = next((i for i in data if i['id'] == id), None)
    if f_user is None:
        print(f"User with id {id} was not found")
    else: 
        print(f"{f_user['id']} - {f_user['name']} - {f_user['salary']}")

@clic.command()
@click.argument("id", type = int)
def remove_user(id):
    data = file_manager.read_file()
    f_user = next((i for i in data if i['id'] == id), None)
    if f_user is None:
        print(f"User with id {id} is not found")
    else: 
        data.remove(f_user)
        file_manager.write_file(data)
        print(f"User with id {id} deleted sucessfully")

@clic.command()
@click.argument("id", type = int)
@click.option('--name', required= True, help = 'Name of the user')
@click.option('--salary', required= True, help = 'Salary of the user')
def update_user(id, name, salary):
    data = file_manager.read_file()
    for i in data:
        if i['id']==i:
            if name is not None:
                i['name']=name
            if salary is not None:
                i['salary']=salary
    file_manager.write_file(data)
    print(f"User with id {id} updated sucessfully")




if __name__ == '__main__':
    clic()