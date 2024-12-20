# Write your code here
import numpy as np


def interpret_command_input():
    inp = input()
    if inp == 'O':
        return [[5, 6, 9, 10]]
    if inp == 'I':
        return [[1, 5, 9, 13], [4, 5, 6, 7]]
    if inp == 'S':
        return [[5, 6, 8, 9], [5, 9, 10, 14]]
    if inp == 'Z':
        return [[4, 5, 9, 10], [2, 5, 6, 9]]
    if inp == 'L':
        return [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
    if inp == 'J':
        return [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
    if inp == 'T':
        return [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]


def create_grid():
    count = 0
    grid = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(j + count)
        count += 4
        grid.append(row)
    return grid


def create_first_grid():
    outer = []
    for i in range(4):
        inner = []
        for j in range(4):
            inner.append('-')
        outer.append(inner)
    return outer


def create_filled_grid(empty_grid, shaped_piece, row_count):
    len_count = len(shaped_piece[0]) - 1
    piece_count = 0
    filled_grid = []
    for i in empty_grid:
        grid_line = []
        for j in i:
            if j != shaped_piece[row_count][piece_count]:
                grid_line.append('-')
            if j == shaped_piece[row_count][piece_count]:
                grid_line.append(0)
                if piece_count < len_count:
                    piece_count += 1
        filled_grid.append(grid_line)
    return filled_grid


def print_piece(length):
    empty_one = create_first_grid()
    for k in empty_one:
        print(" ".join(np.array(k)))
    print()
    for i in range(1):
        count = 0
        for i in range(5):
            piece = create_filled_grid(empty_grid_numbers, shape, count)
            if count != length:
                count += 1
            else:
                count = 0
            for j in piece:
                print(" ".join(np.array(j)))
            print()


empty_grid_numbers = create_grid()
shape_and_len = interpret_command_input()
shape = shape_and_len[0]
length = len(shape) - 1
print_piece(length)
