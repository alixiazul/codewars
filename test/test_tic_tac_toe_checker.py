from src.tic_tac_toe_checker import is_solved


def test_game_not_yet_finished_1():
    # not yet finished
    board = [[0, 0, 1],
             [0, 1, 2],
             [2, 1, 0]]

    assert is_solved(board) == -1


def test_game_not_yet_finished_2():
    # not yet finished
    board = [[0, 0, 2],
             [0, 0, 0],
             [1, 0, 1]]

    assert is_solved(board) == -1


def test_game_winning_row():
    # winning row
    board = [[1, 1, 1],
             [0, 2, 2],
             [0, 0, 0]]
    assert is_solved(board) == 1


def test_game_winning_column():
    # winning column
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 1, 2]]
    assert is_solved(board) == 1


def test_game_draw():
    # draw
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 2, 1]]
    assert is_solved(board) == 0
