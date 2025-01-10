# Write your code here
import numpy as np


def create_first_grid(width, height):
    outer = []
    for i in range(height):
        inner = []
        for j in range(width):
            inner.append('-')
        outer.append(inner)
    for j in outer:
        print(" ".join(np.array(j)))
    print()
    return outer


def interpret_input_piece():
    shape_input = input()
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


def check_boarders(piece, step, width, height):
    if (piece[-1] + step + width) >= (width * height):
        return 'down'
    elif (piece[0] + step) % width == 0 and (piece[-1] + step) < (width * height):
        return 'left'
    elif (piece[-1] + step) % width == (width - 1) and (piece[-1] + step) < (width * height):
        return 'right'


def moved_piece(step, shape):
    moved_piece = []
    for i in shape:
        moved_piece.append(i + step)
    return moved_piece


dimensions = input().split()
board_width = int(dimensions[0])
board_height = int(dimensions[1])
grid = create_first_grid(board_width, board_height)

while True:
    commands = ['piece', 'rotate', 'left', 'right', 'down', 'break', 'exit']
    command = input()
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
                move = input()
                checked_boarders = check_boarders(shape[count], step, board_width, board_height)
                if move == 'left':
                    if checked_boarders != 'left' and checked_boarders != 'down':
                        step += board_width - 1
                        shifted_piece = moved_piece(step, shape[count])
                        put_piece_on_grid(grid, shifted_piece)
                    elif checked_boarders == 'left':
                        step += board_width
                        shifted_piece = moved_piece(step, shape[count])
                        put_piece_on_grid(grid, shifted_piece)
                    if checked_boarders == 'down':
                        #piece should be printed on grid and program moves to the following piece
                        break
                if move == 'right':
                    if checked_boarders != 'right' and checked_boarders != 'down':
                        step += board_width + 1
                        shifted_piece = moved_piece(step, shape[count])
                        put_piece_on_grid(grid, shifted_piece)
                    if checked_boarders == 'right':
                        step += board_width
                        shifted_piece = moved_piece(step, shape[count])
                        put_piece_on_grid(grid, shifted_piece)
                    if checked_boarders == 'down':
                        #piece should be printed on grid and program moves to the following piece
                        break
                elif move == 'down':
                    if checked_boarders != 'down':
                        step += board_width
                        shifted_piece = moved_piece(step, shape[count])
                        put_piece_on_grid(grid, shifted_piece)
                    elif checked_boarders == 'down':
                        # piece should be printed on grid and program moves to the following piece
                        break
                elif move == 'rotate':
                    if (len(shape) - 1) > count:
                        count += 1
                    elif (len(shape) - 1) == count:
                        count = 0
                    checked_boarders = check_boarders(shape[count], step, board_width, board_height)
                    if checked_boarders != 'right' and checked_boarders != 'down' and checked_boarders != 'left':
                        step += board_width
                        shifted_piece = moved_piece(step, shape[count])
                        put_piece_on_grid(grid, shifted_piece)
                    elif checked_boarders == 'down':
                        # piece should be printed on grid and program moves to the following piece
                        break
