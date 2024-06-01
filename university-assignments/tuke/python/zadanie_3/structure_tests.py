from board import Board
from game import Game
from piece import Piece
from player import *


def test_structure(list_of_attributes, must_have):
    for attribute in must_have:
        if attribute not in list_of_attributes:
            return attribute


def test_piece_structure():
    try:
        piece = Piece("black")
    except Exception as e:
        print("Cannot check Piece structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "color",
        "active",
        "position",
        "activate",
        "throw_out",
        "is_done",
        "move",
        "move_to_place"
    ]

    missing = test_structure(dir(piece), all_attributes)
    if missing:
        raise RuntimeError(
            "Piece structure incorrect, attribute {} missing".format(missing))


def test_board_structure():
    try:
        board = Board()
    except Exception as e:
        print("Cannot check Board structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "board",
        "normalize_position",
        "can_move_there",
        "process_player_moves"
    ]

    missing = test_structure(dir(board), all_attributes)
    if missing:
        raise RuntimeError(
            "Board structure incorrect, attribute {} missing".format(missing))


def test_player_structure():
    try:
        board = Board()
        player = Player("black", board)
    except Exception as e:
        print("Cannot check Player structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "color",
        "board",
        "pieces",
        "is_done",
        "has_active",
        "get_piece_positions",
        "get_valid_moves",
        "prepare_targets",
        "get_move"
    ]

    missing = test_structure(dir(player), all_attributes)
    if missing:
        raise RuntimeError(
            "Player structure incorrect, attribute {} missing".format(missing))


def test_game_structure():
    try:
        game = Game(
            [RandomPlayer, RandomPlayer, RandomPlayer, RandomPlayer]
        )
    except Exception as e:
        print("Cannot check Game structure, calling constructor caused an error")
        print(e)
        raise RuntimeError()
    all_attributes = [
        "board",
        "players",
        "get_player_rolls",
        "run_game"
    ]

    missing = test_structure(dir(game), all_attributes)
    if missing:
        raise RuntimeError(
            "Game structure incorrect, attribute {} missing".format(missing))


def test_strategies_structure():
    for strat in [RandomPlayer, SafePlayer, MeanPlayer, EagerPlayer]:
        try:
            board = Board()
            player = strat("black", board)
        except Exception as e:
            print("Cannot check {} structure, calling constructor caused an error".format(strat))
            print(e)
            raise RuntimeError()
        all_attributes = [
            "color",
            "board",
            "pieces",
            "is_done",
            "has_active",
            "get_piece_positions",
            "get_valid_moves",
            "prepare_targets",
            "get_move"
        ]

        missing = test_structure(dir(player), all_attributes)
        if missing:
            raise RuntimeError(
                "{} structure incorrect, attribute {} missing".format(strat.__name__, missing))

        if Player not in strat.__mro__:
            raise RuntimeError(
                "{} class incorrect, should inherit from Player".format(strat.__name__))


if __name__ == '__main__':
    test_piece_structure()

    test_board_structure()

    test_player_structure()

    test_game_structure()

    test_strategies_structure()
