# Write your code here
import numpy as np


def create_first_grid(dropped_pieces, width, height):
    grid_row = 0
    piece_count = 0
    the_piece = dropped_pieces[0]
    outer = []
    if len(dropped_pieces) >= 2:
        for k in range(1, len(dropped_pieces)):
            the_piece = dropped_pieces[k]
            #print(the_piece)
    for i in range(height):
        inner = []
        for j in range(width):
            if the_piece[piece_count] == j + grid_row and the_piece[piece_count] != 0:
                inner.append('0')
                if piece_count < (len(the_piece) - 1):
                    piece_count += 1
            else:
                inner.append('-')
        outer.append(inner)
        grid_row += 10
    for j in outer:
        print(" ".join(np.array(j)))
    print()
    return outer


def interpret_input_piece():
    shape_input = input('select a shape: ')
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
        return shapes[shape_input]
    else:
        raise ValueError("Invalid input")


def put_piece_on_grid(grid, piece):
    grid_row = 0
    piece_count = 0
    grid_height = []
    for i in grid:
        grid_line = []
        for j in range(len(i)):
            if piece[piece_count] == j + grid_row:
                grid_line.append('0')
                if piece_count < (len(piece) -1):
                    piece_count += 1
            else:
                grid_line.append('-')
        grid_height.append(grid_line)
        grid_row += 10
    for j in grid_height:
        print(" ".join(np.array(j)))


def check_boarders_down(piece, step, width, height):
    for i in piece:
        if i + step + width >= (width * height):
            return 'down'


def check_boarders_left(piece, step, width):
    for i in piece:
        if (i + step) % width == 0:
            return 'left'


def check_boarders_right(piece, step, width):
    for i in piece:
        if (i + step) % width == (width - 1):
            return 'right'


def moved_piece(step, shape):
    moved_piece = []
    for i in shape:
        moved_piece.append(i + step)
    return moved_piece


dimensions = input().split()
board_width = int(dimensions[0])
board_height = int(dimensions[1])
dropped_pieces = [[0, 0, 0, 0]]

while True:
    grid = create_first_grid(dropped_pieces, board_width, board_height)
    commands = ['piece', 'break', 'exit']
    command = input('enter a command: ')
    if command not in commands:
        print('Such command does not exist')
    else:
        if command == 'exit':
            break
        elif command == 'piece':
            step = 0
            count = 0
            shape = interpret_input_piece()
            put_piece_on_grid(grid, shape[count])
            while True:
                movements = ['rotate', 'left', 'right', 'down']
                move = input()
                if move in movements:
                    if check_boarders_down(shape[count], step, board_width, board_height) == 'down':
                        shifted_piece = moved_piece(step, shape[count])
                        dropped_pieces.append(shifted_piece)
                        break
                    else:
                        if move == 'left' and check_boarders_left(shape[count], step, board_width) != 'left':
                            step += board_width - 1
                        elif move == 'right' and check_boarders_right(shape[count], step, board_width) != 'right':
                            step += board_width + 1
                        elif move == 'rotate':
                            if (len(shape) - 1) > count:
                                count += 1
                            elif (len(shape) - 1) == count:
                                count = 0
                            if check_boarders_right(shape[count], step, board_width) != 'right' and check_boarders_left(shape[count], step, board_width) != 'left':
                                step += board_width
                        else:
                            step += board_width
                        shifted_piece = moved_piece(step, shape[count])
                        put_piece_on_grid(grid, shifted_piece)
