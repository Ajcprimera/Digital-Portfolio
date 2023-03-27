import numpy as np

class Operation:
    def __init__(self):
        self.matrix_1 = []
        self.matrix_2 = []
        self.solution = None

    def __str__(self):
        return self.solution
    
    def __sum__ (self, m1, m2):
        self.matrix_1 = m1
        self.matrix_2 = m2
        sum_1 = np.array(m1)
        sum_2 = np.array(m2)
        self.solution = sum_1 + sum_2
        return print(f'The sum of {sum_1} and {sum_2} is: {self.solution}')

    def __subtraction__ (self, m1, m2):
        self.matrix_1 = m1
        self.matrix_2 = m2
        sub_1 = np.array(m1)
        sub_2 = np.array(m2)
        solution = sub_1 - sub_2
        return print(f'The subtration between {sub_1} and {sub_2} is: {solution}')

    def __determinant__ (self, m1):
        self.matrix_1 = m1
        det = np.array(m1)
        self.solution = np.linalg.det(det)
        return print(f'The determinant of {det} is: {self.solution}')

    def __transpose__ (self, m1):
        self.matrix_1 = m1
        trans = np.array(m1)
        self.solution = np.transpose(trans)
        return print(f'The transpose of {trans} is: {self.solution}')

    def __diagonal__ (self, m1):
        self.matrix_1 = m1
        diag = np.array(m1)
        self.solution = np.diag(diag)
        return print(f'Ihe inverse of {self.solution}')

    def __multiply__ (self, m1, m2):
        self.matrix_1 = m1
        self.matrix_2 = m2
        mul_1 = np.array(m1)
        mul_2 = np.array(m2)
        if len(mul_1[0, :]) != len(mul_2[:, 0]):
            return print(f'Is not possible to make the multiplication due to the diffence of rows and columns between {mul_1} and {mul_2}')
        else:
            self.solution = np.matmul(mul_1, mul_2)
            return print(f'{mul_1} multiply by {mul_2} is: {self.solution}')
        
    def __inverse__ (self, m1):
        self.matrix_1 = m1
        inv = np.array(m1)
        if len(inv[0, :]) != len(inv[:, 0]) and np.linalg.det(inv) == 0:
            return print(f'The number of rows is different of number of columns and also the determinant of the matrix is 0')
        else: 
            self. solution = np.linalg.inv(inv)
            return print(f'The diagonal of {inv} is: {self.solution}')