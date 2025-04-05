# TODO:
#
# - if configured to prompt for x/y, going first or not etc., do it per
#   match, not per program run.
# - support >2 players (though rules would be unclear).

import random, os

HUMAN = 'h'
COMPUTER = 'c'

X_SIDE = 'x'
O_SIDE = 'o'


## -------------------------------------------------
# Config for gameplay options -- you may edit these
HUMAN_SIDE = X_SIDE # or O_SIDE or 'choose'
PLAYS_FIRST = HUMAN # or COMPUTER or 'choose'
## -------------------------------------------------


VALID_CELLS = [row + col
               for col in ['1', '2', '3']
               for row in ['A', 'B', 'C']]
WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
    [0, 4, 8], [2, 4, 6]             # diagonals
    ]


X_PP = [l.ljust(11) for l in """
8b,     ,d8
 `Y8, ,8P'
   )888(
 ,d8" "8b,
8P'     `Y8
""".strip('\n').split('\n')]

O_PP = [l.ljust(11) for l in """
 ,adPPYba,
a8"     "8a
8b       d8
"8a,   ,a8"
 `"YbbdP"'
""".strip('\n').split('\n')]


def get_pp_row(player_id, config, row_index):
    for c in config:
        if c['player'] == player_id:
            return X_PP[row_index] if c['side'] == X_SIDE else O_PP[row_index]
    return ' ' * 11

def cell_row(board, config, cell, row):
    result = ''
    if board[cell] is None:
        result += ' '*11
    else:
        result += get_pp_row(board[cell], config, row)
    return result

# sample board: [None, 'x', None, None, None, 'o', 'o', None, 'x']

def print_board(b, c):
    os.system('clear')
    print('  ' + (' '*5) + 'A' + (' '*5) + '   ' + (' '*5) + 'B' + (' '*5) + '   ' + (' '*5) + 'C')
    print('  ' + (' '*11) + ' | ' + (' '*11) + ' |')
    print('  ' + cell_row(b, c, cell=0, row=0) + ' | ' + cell_row(b, c, cell=1, row=0) + ' | ' + cell_row(b, c, cell=2, row=0))
    print('  ' + cell_row(b, c, cell=0, row=1) + ' | ' + cell_row(b, c, cell=1, row=1) + ' | ' + cell_row(b, c, cell=2, row=1))
    print('1 ' + cell_row(b, c, cell=0, row=2) + ' | ' + cell_row(b, c, cell=1, row=2) + ' | ' + cell_row(b, c, cell=2, row=2))
    print('  ' + cell_row(b, c, cell=0, row=3) + ' | ' + cell_row(b, c, cell=1, row=3) + ' | ' + cell_row(b, c, cell=2, row=3))
    print('  ' + cell_row(b, c, cell=0, row=4) + ' | ' + cell_row(b, c, cell=1, row=4) + ' | ' + cell_row(b, c, cell=2, row=4))
    print('  ' + (' '*11) + ' | ' + (' '*11) + ' |')
    print('  ' + ('-'*11) + '-+-' + ('-'*11) + '-|-' + ('-'*11) + '-')
    print('  ' + (' '*11) + ' | ' + (' '*11) + ' |')
    print('  ' + cell_row(b, c, cell=3, row=0) + ' | ' + cell_row(b, c, cell=4, row=0) + ' | ' + cell_row(b, c, cell=5, row=0))
    print('  ' + cell_row(b, c, cell=3, row=1) + ' | ' + cell_row(b, c, cell=4, row=1) + ' | ' + cell_row(b, c, cell=5, row=1))
    print('2 ' + cell_row(b, c, cell=3, row=2) + ' | ' + cell_row(b, c, cell=4, row=2) + ' | ' + cell_row(b, c, cell=5, row=2))
    print('  ' + cell_row(b, c, cell=3, row=3) + ' | ' + cell_row(b, c, cell=4, row=3) + ' | ' + cell_row(b, c, cell=5, row=3))
    print('  ' + cell_row(b, c, cell=3, row=4) + ' | ' + cell_row(b, c, cell=4, row=4) + ' | ' + cell_row(b, c, cell=5, row=4))
    print('  ' + (' '*11) + ' | ' + (' '*11) + ' |')
    print('  ' + ('-'*11) + '-+-' + ('-'*11) + '-|-' + ('-'*11) + '-')
    print('  ' + (' '*11) + ' | ' + (' '*11) + ' |')
    print('  ' + cell_row(b, c, cell=6, row=0) + ' | ' + cell_row(b, c, cell=7, row=0) + ' | ' + cell_row(b, c, cell=8, row=0))
    print('  ' + cell_row(b, c, cell=6, row=1) + ' | ' + cell_row(b, c, cell=7, row=1) + ' | ' + cell_row(b, c, cell=8, row=1))
    print('3 ' + cell_row(b, c, cell=6, row=2) + ' | ' + cell_row(b, c, cell=7, row=2) + ' | ' + cell_row(b, c, cell=8, row=2))
    print('  ' + cell_row(b, c, cell=6, row=3) + ' | ' + cell_row(b, c, cell=7, row=3) + ' | ' + cell_row(b, c, cell=8, row=3))
    print('  ' + cell_row(b, c, cell=6, row=4) + ' | ' + cell_row(b, c, cell=7, row=4) + ' | ' + cell_row(b, c, cell=8, row=4))
    print('  ' + (' '*11) + ' | ' + (' '*11) + ' |')
    #print("Remaining choices", remaining_choices(b))

def initialize_board():
    return [None for _ in range(0,9)]

def set_cell(board, cell, player_id):
    if player_id not in [HUMAN, COMPUTER]:
        raise ValueError(f"Player must be {HUMAN} or {COMPUTER}; {player_id} given.")
    if not isinstance(cell, int) or len(board) > cell < 0:
        raise ValueError(f"Cell index not an int within the board range: {cell}")
    board[cell] = player_id

def remaining_choices(board):
    return [i for i, mark in enumerate(board) if mark is None]

def players_turn(board):
    while True:
        remaining = remaining_choices(board)
        if len(remaining) == 1:
            # Skip the question to the player, there's only one choice
            selection_index = remaining[0]
        else:
            selection = input("Choose a cell using spreadsheet notation e.g. C2: ").strip().upper()
            if selection not in VALID_CELLS:
                print("Invalid choice, try again.")
                continue
            selection_index = VALID_CELLS.index(selection)
            if board[selection_index] is not None:
                print("Cell is already taken, try again.")
                continue
        set_cell(board, selection_index, HUMAN)
        break

def find_completable_line(board, player_id):
    if player_id not in [HUMAN, COMPUTER]:
        raise ValueError("Not a valid player identifier: " + player_id)
    for combo in WINNING_COMBOS:
        line = [board[cell] for cell in combo]
        if line.count(player_id) == 2 and line.count(None) == 1:
            return combo[line.index(None)]
    return None

def computers_turn(board):
    # offense, then defense
    choice = find_completable_line(board, COMPUTER) or \
        find_completable_line(board, HUMAN)

    # if the center square is available, take it
    if choice is None and 4 in remaining_choices(board):
        choice = 4

    # todo: place in a square adjacent to a previous move, if possible
        
    # Fallback: random
    if choice is None:
        choice = random.choice(remaining_choices(board))

    set_cell(board, choice, COMPUTER)

def winner(board):
    for combo in WINNING_COMBOS:
        sq1, sq2, sq3 = combo
        if board[sq1] == board[sq2] == board[sq3] and board[sq1]:
            return board[sq1]
    return None

# Config expresses playing order and which player is 'x' vs 'o'
# Sample config: [{'player': 'c', 'side': 'o'}, {'player': 'h', 'side': 'x'}]
def play_game(config):
    board = initialize_board()
    turn_number = -1
    try:
        while True:
            print_board(board, config)

            turn_number += 1
            current_player = config[turn_number % len(config)]
            if current_player['player'] == HUMAN:
                players_turn(board)
            else:
                computers_turn(board)

            maybe_winner = winner(board)
            if maybe_winner:
                print_board(board, config)
                print("Winner: " + ('Human' if maybe_winner == HUMAN else 'Computer'))
                return maybe_winner
            if len(remaining_choices(board)) == 0:
                print_board(board, config)
                print("Board full - Tie.")
                return None
    finally:
        print(f"Game ended after {turn_number + 1} turns.")

def get_yn_choice(prompt):
    while True:
        response = input(prompt + " (y/n) ")
        try:
            return bool(['n', 'y'].index(response[:1].lower()))
        except ValueError:
            print(f"Invalid value '{response}', try again.")
        
def get_player_order_choice():
    if get_yn_choice("Do you want to play first?"):
        return HUMAN
    return COMPUTER
            
def get_human_side_choice():
    if get_yn_choice("Do you want to be 'x'?"):
        return X_SIDE
    return O_SIDE

def main_loop():
    print("Welcome to TTT.")

    # TODO refactor to do the choice prompting per match instead of
    #      making the user restart the program.

    # First determine which player is which side
    human_side = get_human_side_choice() if HUMAN_SIDE == 'choose' else HUMAN_SIDE

    # Next work out playing order
    plays_first = get_player_order_choice() if PLAYS_FIRST == 'choose' else PLAYS_FIRST

    player_config = [{'player': HUMAN, 'side': human_side}]
    insert_computer_at = 0 if plays_first == COMPUTER else 1
    player_config.insert(insert_computer_at, {'player': COMPUTER, 'side': O_SIDE if human_side == X_SIDE else X_SIDE})
    
    # The main loop keeps track of matches inline.
    # TODO probably move the match score into the player config, also add
    #      pretty printable player names -- this would help with >2 players
    num_games = 0
    human_score = 0
    computer_score = 0
    while True:
        num_games += 1
        winner = play_game(player_config)
        if winner == HUMAN:
            human_score += 1
        elif winner == COMPUTER:
            computer_score += 1
        print(f"Current match score: Human {human_score}, Computer {computer_score} after {num_games} game(s).")
        if num_games >= 2 and human_score != computer_score:
            match_winner = HUMAN if human_score > computer_score else COMPUTER
            print(f"{'Human' if match_winner == HUMAN else 'Computer'} wins the match!!")
            num_games = human_score = computer_score = 0
        if not get_yn_choice("Do you want to play again?"):
            break
    print("Goodbye!")

main_loop()

