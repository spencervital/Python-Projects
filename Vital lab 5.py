# Define validation functions
def validate_num_black_pieces(board):
    num_black_pieces = sum(row.count('b') for row in board)
    if num_black_pieces != 16:
        print(f"Fail: Number of black pieces – {num_black_pieces} black pieces.")
    else:
        print("Pass: Number of black pieces – 16 black pieces.")


def validate_num_white_pieces(board):
    num_white_pieces = sum(row.count('w') for row in board)
    if num_white_pieces != 16:
        print(f"Fail: Number of white pieces – {num_white_pieces} white pieces.")
    else:
        print("Pass: Number of white pieces – 16 white pieces.")


def validate_kings(board):
    num_white_kings = sum(row.count('wk') for row in board)
    num_black_kings = sum(row.count('bk') for row in board)
    if num_white_kings != 1 or num_black_kings != 1:
        print("Fail: Kings – One of each color.")
    else:
        print("Pass: Kings – One of each color.")


def validate_queens(board):
    num_white_queens = sum(row.count('wq') for row in board)
    num_black_queens = sum(row.count('bq') for row in board)
    if num_white_queens > 1 or num_black_queens > 1:
        print("Fail: Queens – No more than 1 of each color.")
    else:
        print("Pass: Queens – No more than 1 of each color.")


def validate_rooks(board):
    num_white_rooks = sum(row.count('wr') for row in board)
    num_black_rooks = sum(row.count('br') for row in board)
    if num_white_rooks > 2 or num_black_rooks > 2:
        print("Fail: Rooks – No more than 2 of each color.")
    else:
        print("Pass: Rooks – No more than 2 of each color.")


def validate_bishops(board):
    num_white_bishops = sum(row.count('wb') for row in board)
    num_black_bishops = sum(row.count('bb') for row in board)
    if num_white_bishops > 2 or num_black_bishops > 2:
        print("Fail: Bishops – No more than 2 of each color.")
    else:
        print("Pass: Bishops – No more than 2 of each color.")


def validate_knights(board):
    num_white_knights = sum(row.count('wn') for row in board)
    num_black_knights = sum(row.count('bn') for row in board)
    if num_white_knights > 2 or num_black_knights > 2:
        print("Fail: Knights – No more than 2 of each color.")
    else:
        print("Pass: Knights – No more than 2 of each color.")


def validate_pawns(board):
    num_white_pawns = sum(row.count('wp') for row in board)
    num_black_pawns = sum(row.count('bp') for row in board)
    if num_white_pawns > 8 or num_black_pawns > 8:
        print("Fail: Pawns – No more than 8 of each color.")
    else:
        print("Pass: Pawns – No more than 8 of each color.")


# Define validation dictionary
validation_dict = {
    'Number of black pieces': validate_num_black_pieces,
    'Number of white pieces': validate_num_white_pieces,
    'Kings': validate_kings,
    'Queens': validate_queens,
    'Rooks': validate_rooks,
    'Bishops': validate_bishops,
    'Knights': validate_knights,
    'Pawns': validate_pawns
}

# Define the chess board
board = [
    ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
]


# Define validation criteria
def validate_chess_board(board):
    # Check that there are 16 black pieces and 16 white pieces
    num_black_pieces = len([piece for row in board for piece in row if piece[0] == 'B'])
    num_white_pieces = len([piece for row in board for piece in row if piece[0] == 'W'])
    if num_black_pieces != 16:
        print('FAIL: Number of black pieces -', num_black_pieces, 'black pieces.')
    else:
        print('PASS: Number of black pieces -', num_black_pieces, 'black pieces.')
    if num_white_pieces != 16:
        print('FAIL: Number of white pieces -', num_white_pieces, 'white pieces.')
    else:
        print('PASS: Number of white pieces -', num_white_pieces, 'white pieces.')

    # Check that there is one king of each color
    black_kings = len([piece for row in board for piece in row if piece == 'BK'])
    white_kings = len([piece for row in board for piece in row if piece == 'WK'])
    if black_kings != 1:
        print('FAIL: Black has', black_kings, 'kings.')
    else:
        print('PASS: Black has', black_kings, 'king.')
    if white_kings != 1:
        print('FAIL: White has', white_kings, 'kings.')
    else:
        print('PASS: White has', white_kings, 'king.')


# Call the validation function
validate_chess_board(board)

