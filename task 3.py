import random
import numpy as np

matrix_size = int(input("Set number of rows and columns in matrix"))
my_matrix = [[random.randint(1, 100) for j in range(matrix_size)] for i in range(matrix_size)]

for row in my_matrix:
    print(("{:<5}" * len(row)).format(*row))


def sumColumn(matrix):
    sum_of_column = [sum(col) for col in zip(*matrix)]
    print('sum of columns')
    print(("{:<5}" * len(sum_of_column)).format(*sum_of_column))
    matrix.append(sum_of_column)

sumColumn(my_matrix)


def bubble_sort(matrix, x):
    flag = True
    while flag:
        flag = False
        for i in range(len(matrix[x]) - 1):
            if matrix[x][i] > matrix[x][i + 1]:
                for j in range(len(matrix)):
                    matrix[j][i], matrix[j][i + 1] = matrix[j][i + 1], matrix[j][i],
                flag = True


bubble_sort(my_matrix, -1)
my_matrix.pop()


print('new sorted matrix')


for row in my_matrix:
    print(("{:<5}" * len(row)).format(*row))

