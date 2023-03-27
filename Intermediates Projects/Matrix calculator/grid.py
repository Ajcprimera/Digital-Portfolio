import random

class Matrix:
    def __init__(self):
        self.matrix = []
        self.rows = 0
        self.columns = 0

    def __str__(self):
        return self.matrix

    def generate_user_values(self, rows, columns, value = None):
        number = 1
        self.rows = rows
        self.columns = columns
        self.matrix = [[None for i in range(columns)] for j in range(rows)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                value = int(input(f'Input the value number {number}: '))
                self.matrix[i][j] = value
                number += 1
        return self.matrix
    
    def generate_random_value(self, rows, columns, value = None):
        self.rows = rows
        self.columns = columns
        lower_number = int(input('Please input the lower number range: '))
        higher_number = int(input('Please input the higher number range: '))
        while higher_number < lower_number:
            higher_number = int(input('Input a number bigger than the lower number range: '))
        self.matrix = [[None for i in range(columns)] for j in range(rows)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                value = random.randint(lower_number, higher_number)
                self.matrix[i][j] = value
        return self.matrix