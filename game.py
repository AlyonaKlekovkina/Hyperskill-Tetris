# Write your code here
import numpy as np


def interpret_command_input():
    shape_input = input()
    dimentions_of_the_grid = input()
    shapes = {
        'O': [[4, 5, 14, 15]],
        'I': [[4, 14, 24, 34], [3, 4, 5, 6]],
        'S': [[4, 5, 13, 14], [4, 14, 15, 25]],
        'Z': [[4, 5, 15, 16], [5, 14, 15, 24]],
        'L': [[4, 14, 24, 25], [5, 13, 14, 15], [4, 5, 15, 25], [4, 5, 6, 14]],
        'J': [[5, 15, 24, 25], [3, 4, 5, 15], [4, 5, 14, 24], [4, 14, 15, 16]],
        'T': [[4, 14, 15, 24], [4, 13, 14, 15], [5, 14, 15, 25], [4, 5, 6, 15]],
    }
    if shape_input in shapes:
        return shapes[shape_input], dimentions_of_the_grid.split()
    else:
        raise ValueError("Invalid input")


def create_grid(width, height):
    count = 0
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(j + count)
        count += width
        grid.append(row)
    return grid


def create_first_grid(width, height):
    outer = []
    for i in range(height):
        inner = []
        for j in range(width):
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


#code from stage 1, not in use in stage 2
def print_piece(width, height, length):
    empty_one = create_first_grid(width, height)
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


def start_position(width, height):
    empty_grid = create_first_grid(width, height)
    for k in empty_grid:
        print(" ".join(np.array(k)))
    print()
    first_piece = create_filled_grid(empty_grid_numbers, shape, 0)
    for i in first_piece:
        print(" ".join(np.array(i)))
    print()


def make_a_move(shape):
    global iteration
    commands = ['left', 'right', 'down', 'rotate']
    piece = shape[0]
    count = 1
    move_left = 0
    move_right = 0
    iteration = 1
    while True:
        how_to_move = input()
        if how_to_move == 'left':
            step = 9
            piece = move_left_right_down(step, piece)
            move_left += 1
        if how_to_move == 'right':
            step = 11
            piece = move_left_right_down(step, piece)
            move_right += 1
        if how_to_move == 'down':
            step = 10
            piece = move_left_right_down(step, piece)
        if how_to_move == 'rotate':
            step = ((10 * iteration) - move_left) + move_right
            piece = move_left_right_down(step, shape[count])
            if count < len(shape) - 1:
                count += 1
            elif count == len(shape) - 1:
                count = 0
        if how_to_move == 'exit':
            break


def move_left_right_down(step, piece):
    global iteration
    shifted_shape = [[]]
    for i in piece:
        shifted_shape[0].append(i + step)
    shifted_piece = create_filled_grid(empty_grid_numbers, shifted_shape, 0)
    for m in shifted_piece:
        print(" ".join(np.array(m)))
    print()
    iteration += 1
    return shifted_shape[0]


shape_and_dimensions = interpret_command_input()
shape = shape_and_dimensions[0]
length = len(shape) - 1
dimensions = shape_and_dimensions[1]
board_width = int(dimensions[0])
board_height = int(dimensions[1])
empty_grid_numbers = create_grid(board_width, board_height)
start_position(board_width, board_height)
make_a_move(shape)

