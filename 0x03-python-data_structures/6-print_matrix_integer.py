#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row_x in range(len(matrix)):
            for var in range(len(matrix[row_x])):
                if var != len(matrix[row_x]) - 1:
                    colum_x = ' '
                else:
                    colum_xe = ''
                    print("{:d}".format(matrix[row_x][var]), end=colum_x)
                    print()
