# Write your code here
import numpy as np


def create_first_grid(width, height):
    outer = []
    for i in range(height):
        inner = []
        for j in range(width):
            inner.append('-')
        outer.append(inner)
    for k in outer:
        print(" ".join(np.array(k)))
    print()
    return outer


def interpret_input_piece():
    shape_input = input('Select a shape: ')
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
    return grid_height


def violates_bottom_boundary(piece, step, width, height, dropped_pieces):
    all_dropped_positions = sorted(np.concatenate(dropped_pieces)) if dropped_pieces else []
    for pos in piece:
        future_pos = pos + step + width
        if future_pos >= width * height:
            return True  # Hits the floor
        if future_pos in all_dropped_positions:
            return True  # Collides with another piece
    return False


def violates_left_boundary(piece, step, width):
    for i in piece:
        if (i + step) % width == 0:
            return True


def violates_right_boundary(piece, step, width):
    for i in piece:
        if (i + step) % width == (width - 1):
            return True


def moved_piece(step, shape):
    moved_piece = []
    for i in shape:
        moved_piece.append(i + step)
    return moved_piece


def put_dropped_pieces_on_grid(dropped_pieces, width, height):
    sorted_pieces = sorted(np.concatenate(dropped_pieces))
    grid_row = 0
    piece_count = 0
    grid_height = []
    for i in range(height):
        grid_line = []
        for j in range(width):
            if sorted_pieces[piece_count] == j + grid_row:
                grid_line.append('0')
                if piece_count < (len(sorted_pieces) - 1):
                    piece_count += 1
            else:
                grid_line.append('-')
        grid_height.append(grid_line)
        grid_row += 10
    return grid_height


def merge_two_grids(moving, static):
    outer = []
    for i, j in zip(moving, static):
        inner = []
        for k in range(len(i)):
            if i[k] == '0' or j[k] == '0':
                inner.append('0')
            elif i[k] == '-' or j[k] == '-':
                inner.append('-')
        outer.append(inner)
    return outer


dimensions = input().split()
board_width = int(dimensions[0])
board_height = int(dimensions[1])
dropped_pieces = []
grid = create_first_grid(board_width, board_height)

while True:
    commands = ['piece', 'break', 'exit']
    command = input('Enter a command "piece", "break" or "exit": ')
    if command not in commands:
        print('Such command does not exist')
    else:
        if command == 'exit':
            break
        elif command == 'piece':
            step = 0
            count = 0
            shape = interpret_input_piece()
            first_piece = put_piece_on_grid(grid, shape[count])
            for f in first_piece:
                print(" ".join(np.array(f)))
            while True:
                movements = ['rotate', 'left', 'right', 'down']
                move = input("Select movement: ")
                if move in movements:
                    if violates_bottom_boundary(shape[count], step, board_width, board_height, dropped_pieces):
                        shifted_piece = moved_piece(step, shape[count])
                        dropped_pieces.append(shifted_piece)
                        grid_with_dropped = put_dropped_pieces_on_grid(dropped_pieces, board_width, board_height)
                        for i in grid_with_dropped:
                            print(" ".join(np.array(i)))
                        break
                    else:
                        if move == 'left' and not violates_left_boundary(shape[count], step, board_width):
                            step += board_width - 1
                        elif move == 'right' and not violates_right_boundary(shape[count], step, board_width):
                            step += board_width + 1
                        elif move == 'rotate':
                            if (len(shape) - 1) > count:
                                count += 1
                            elif (len(shape) - 1) == count:
                                count = 0
                        else:
                            step += board_width
                        shifted_piece = moved_piece(step, shape[count])
                        moving_piece = put_piece_on_grid(grid, shifted_piece)
                        if len(dropped_pieces) == 0:
                            for h in moving_piece:
                                print(" ".join(np.array(h)))
                        else:
                            fallen_pieces = put_dropped_pieces_on_grid(dropped_pieces, board_width, board_height)
                            merged_grid = merge_two_grids(moving_piece, fallen_pieces)
                            for m in merged_grid:
                                print(" ".join(np.array(m)))
