#Cited from https://www.jianshu.com/p/53d1cab0f2f5

import math
from generategrid.list.randomlist import generate_random_list

def get_row(matrix, row):
        row_arr = []
        for v in matrix[row]:
            if v == 0:
                continue
            row_arr.append(v)
        return row_arr

def get_col(matrix, col):
        col_arr = []
        for i in range(9):
            val = matrix[i][col]
            if val == 0:
                continue
            col_arr.append(matrix[i][col])
        return col_arr

def get_block(matrix, num):
    col_arr = []
    seq = num % 3
    col_end = 9 if seq == 0 else seq * 3
    row_end = int(math.ceil(num / 3) * 3)
    for i in range(row_end - 3, row_end):
        for j in range(col_end - 3, col_end):
            val = matrix[i][j]
            if val != 0:
                col_arr.append(matrix[i][j])
    return col_arr

def get_block_seq(row, col):
        col_seq = int(math.ceil((col + 0.1) / 3))
        row_seq = int(math.ceil((row + 0.1) / 3))
        return 3 * (row_seq - 1) + col_seq

def get_enable_arr(matrix, row, col):
        avail_arr = generate_random_list()
        seq = get_block_seq(row, col)
        block = get_block(matrix, seq)
        row = get_row(matrix, row)
        col = get_col(matrix, col)
        unable_arr = list(set(block + row + col))
        for v in unable_arr:
            if v in avail_arr:
                avail_arr.remove(v)
        return avail_arr

