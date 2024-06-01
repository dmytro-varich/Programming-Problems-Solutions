import pickle

from board import Board
from piece import Piece
from player import Player
from structure_tests import *


def test_normalize_positions():
    print("Checking Board.normalize_positions()")
    passed, total = 0, 0
    works_for_none = False

    with open("test_files/normalize_position_tests.pkl", 'rb') as infile:
        test_cases = pickle.load(infile)

    for color, pos, corr in test_cases:
        board = Board()
        try:
            total += 1
            st_res = board.normalize_position(pos, color)
        except Exception as e:
            print("\tCalling Board.normalize_position() caused an exception:")
            print("\t", e)
            print()
        else:
            if st_res != corr:
                print("\tBoard.normalize_positions() returned wrong value")
                print("\tExpected {}, got {}".format(corr, st_res))
                print("\tColor={}, piece position={}".format(color, pos))
                print()
            else:
                if corr is None:
                    works_for_none = True
                passed += 1

    points = (passed / total) * 0.5
    if not works_for_none:
        points -= 0.09
    print("Checking Board.normalize_positions() finished: {:.2f}/0.5".format(points))
    return points


def prepare_setup(setup):
    str_to_type = {
        "Player": Player,
        "RandomPlayer": RandomPlayer,
        "SafePlayer": SafePlayer,
        "MeanPlayer": MeanPlayer,
        "EagerPlayer": EagerPlayer
    }

    board = Board()
    players = list()

    for _, player_color in setup:
        player = str_to_type[_](player_color, board)
        players.append(player)
        for piece_id, (act, pos, idx) in enumerate(setup[(_, player_color)]):
            piece = player.pieces[piece_id]
            piece.active = act
            piece.position = pos
            if pos is not None and pos < 40:
                board.board[idx] = piece

    return board, players


def test_can_move_there():
    print("Checking Board.can_move_there()")
    passed, total = 0, 0

    with open("test_files/can_move_there_tests.pkl", 'rb') as infile:
        test_cases = pickle.load(infile)

    for setup, (pl_id, p_id, new_pos, corr) in test_cases:
        total += 1
        board, players = prepare_setup(setup)

        test_player = players[pl_id]
        test_piece = test_player.pieces[p_id]

        try:
            st_res = board.can_move_there(test_player, test_piece, new_pos)
        except Exception as e:
            print("\tCalling Board.can_move_there() caused an exception:")
            print("\t", e)
            print()
        else:
            if st_res != corr:
                print("\tBoard.can_move_there() returned wrong value")
                print("\tExpected {}, got {}".format(corr, st_res))
                print()
            else:
                passed += 1

    points = (passed / total) * 0.5
    print("Checking Board.can_move_there() finished: {:.2f}/0.5".format(points))
    return points


def build_setup(board, players):
    setup = dict()
    for player in players:
        pl_list = list()
        for piece in player.pieces:
            try:
                board_pos = board.board.index(piece)
            except ValueError:
                board_pos = None
            pl_list.append((piece.active, piece.position, board_pos))
        setup[(type(player).__name__, player.color)] = pl_list

    return setup


def test_process_player_moves():
    print("Checking Board.process_player_moves()")
    passed, total = 0, 0

    with open("test_files/process_player_moves_tests.pkl", 'rb') as infile:
        test_cases = pickle.load(infile)

    for setup, (pl_id, p_id, new_pos), corr_setup in test_cases:
        total += 1
        board, players = prepare_setup(setup)

        test_player = players[pl_id]
        test_piece = test_player.pieces[p_id]

        try:
            targets = [(test_piece, new_pos)]
            board.process_player_moves(test_player, targets)
            st_setup = build_setup(board, players)
        except Exception as e:
            print("\tCalling Board.process_player_moves() caused an exception:")
            print("\t", e)
            print()
        else:
            if st_setup != corr_setup:
                print("\tBoard.process_player_moves() did not update board correctly")
                print("\tExpected {} piece positions, got {}".format(corr_setup, st_setup))
                print()
            else:
                passed += 1

    points = (passed / total)
    print("Checking Board.process_player_moves() finished: {:.2f}/1".format(points))
    return points


def test_board():
    try:
        test_piece_structure()
        test_board_structure()
        test_player_structure()
    except RuntimeError:
        print("Cannot test Board class")
        return 0

    p1 = test_normalize_positions()
    print()

    p2 = test_can_move_there()
    print()

    p3 = test_process_player_moves()
    print()

    total = max(sum([p1, p2, p3]), 0)
    print("BOARD POINTS: {:.2f}/2".format(total))
    return total


if __name__ == '__main__':
    test_board()
