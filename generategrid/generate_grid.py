#Cited from https://www.jianshu.com/p/53d1cab0f2f5

import datetime
from generategrid.list.randomlist import generate_random_list
from generategrid.get.get import get_row, get_col, get_block, get_block_seq, get_enable_arr

class Sudo():
    def __init__(self):
        self.matrix = []

    def print_grid(self, arr):
        for i in range(9):
            print(arr[i])

    def generate(self):
        start = datetime.datetime.now()
        can_num = {}
        for i in range(9):
            self.matrix.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

        num_list = generate_random_list()
        for row in range(3):
            for col in range(3):
                self.matrix[row][col] = num_list.pop(0)

        num_list = generate_random_list()
        for row in range(3, 6):
            for col in range(3, 6):
                self.matrix[row][col] = num_list.pop(0)

        num_list = generate_random_list()
        for row in range(6, 9):
            for col in range(6, 9):
                self.matrix[row][col] = num_list.pop(0)

        box_list = []
        for row in range(9):
            for col in range(9):
                if self.matrix[row][col] == 0:
                    box_list.append({'row': row, 'col': col})

        i = 0
        while i < len(box_list):
            position = box_list[i]
            row = position['row']
            col = position['col']
            key = '%dx%d' % (row, col)
            if key in can_num:
                enable_arr = can_num[key]
            else:
                enable_arr = get_enable_arr(self.matrix, row, col)
                can_num[key] = enable_arr

            if len(enable_arr) <= 0:
                i -= 1
                if key in can_num:
                    del (can_num[key])
                self.matrix[row][col] = 0
                continue
            else:
                self.matrix[row][col] = enable_arr.pop()
                i += 1
        end = datetime.datetime.now()
        self.print_grid(self.matrix)
        print('\ncost time:', end - start)


