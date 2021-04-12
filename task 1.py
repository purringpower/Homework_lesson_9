my_matrix = [[3, -2, 6, 4],
[8, 1, 12, 2],
[5, 4, -8, 0]]



def bubble_sort(matrix, x):
    flag = True
    while flag:
        flag = False
        for i in range(len(matrix[x]) - 1):
            if matrix[x][i] > matrix[x][i + 1]:
                for j in range(len(matrix)):
                    matrix[j][i], matrix[j][i + 1] = matrix[j][i + 1], matrix[j][i],
                flag = True


bubble_sort(my_matrix, 0)

print(my_matrix)

