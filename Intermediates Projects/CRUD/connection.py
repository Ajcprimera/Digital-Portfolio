import psycopg2

class connectdb():
    def __init__(self) -> None:
        try:
            self.connection = psycopg2.connect(
            host = 'XXXXX',
            dbname = 'XXXX',
            user = 'XXXXX',
            password = 'XXXXX',
            port = 1234)
        except Exception as error:
            print(error)
    
    def listEmployees(self):
        try:
            curs = self.connection.cursor()
            curs.execute('SELECT * FROM employees ORDER BY name ASC;')
            data = curs.fetchall()
            return data
        except Exception as error:
            print(error)

    def addemployee(self, employee):
        try:
            curs = self.connection.cursor()
            script = "INSERT INTO employees (name, salary, fouls) values ('{0}',{1},{2});"
            curs.execute(script.format(employee[0], employee[1], employee[2]))
            self.connection.commit()

            print('Employee added successfully\n')
        except Exception as error:
            print(error)

    def removeemployee(self, id):
        try:
            curs = self.connection.cursor()
            script = "DELETE FROM employees WHERE id = {0};"
            curs.execute(script.format(id))
            self.connection.commit()
            print('Employee deleted successfully\n')
        except Exception as error:
            print(error)

    def updateemployee(self, id, employee):
        try:
            curs = self.connection.cursor()
            script = "UPDATE employees SET name='{0}', salary={1}, fouls={2} WHERE id = {3};"
            curs.execute(script.format(employee[0], employee[1], employee[2], id))
            self.connection.commit()
            print('Employee updated successfully\n')
        except Exception as error:
            print(error)
