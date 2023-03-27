from grid import Matrix
  
def convertion_r (rows, columns):
        matrix = Matrix()
        matrix_s = matrix.generate_random_value(rows,columns)
        return matrix_s

def convertion_u(rows, columns):
    matrix = Matrix()
    matrix_s = matrix.generate_user_values(rows, columns)
    return matrix_s