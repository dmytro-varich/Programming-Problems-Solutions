import pickle
import random

from board import Board
from piece import Piece
from player import Player
from structure_tests import *


def test_is_done():
    print("Checking Player.is_done()")
    passed, total = 0, 0

    possibles = [None] + list(range(45))
    for _ in range(1000):
        total += 1
        if random.random() < 0.9:
            setup = random.sample(possibles, 4)
        else:
            setup = [40, 41, 42, 43]
            random.shuffle(setup)
        color = random.choice(["black", "yellow", "green", "red"])

        try:
            board = Board()
            player = Player(color, board)
            for piece, pos in zip(player.pieces, setup):
                piece.position = pos
                piece.active = False if pos is None else True
            st_res = player.is_done()
        except Exception as e:
            print("\tCalling Player.is_done() caused an exception:")
            print("\t", e)
            print()
        else:
            corr = all([num in setup for num in [40, 41, 42, 43]])
            if st_res != corr:
                print("\tPlayer.is_done() returned wrong value")
                print("\tExpected {}, got {}".format(corr, st_res))
                print("\tPiece positions: {}".format(setup))
                print()
            else:
                passed += 1

    points = (passed / total) * 0.1
    print("Checking Player.is_done() finished: {:.2f}/0.1".format(points))
    return points


def test_has_active():
    print("Checking Player.has_active()")
    passed, total = 0, 0

    possibles = [None] + list(range(45))
    for _ in range(1000):
        has_active = False
        total += 1
        if random.random() < 0.9:
            setup = random.sample(possibles, 4)
        else:
            setup = [None, None, None, None]
        color = random.choice(["black", "yellow", "green", "red"])

        try:
            board = Board()
            player = Player(color, board)
            for piece, pos in zip(player.pieces, setup):
                piece.position = pos
                piece.active = False if pos is None else True
                has_active = has_active or piece.active
            st_res = player.has_active()
        except Exception as e:
            print("\tCalling Player.has_active() caused an exception:")
            print("\t", e)
            print()
        else:
            if st_res != has_active:
                print("\tPlayer.has_active() returned wrong value")
                print("\tExpected {}, got {}".format(has_active, st_res))
                print("\tPiece positions: {}".format(setup))
                print()
            else:
                passed += 1

    points = (passed / total) * 0.1
    print("Checking Player.has_active() finished: {:.2f}/0.1".format(points))
    return points


def test_get_piece_positions():
    print("Checking Player.get_piece_positions()")
    passed, total = 0, 0

    possibles = [None] + list(range(45))
    for _ in range(1000):
        total += 1
        setup = random.sample(possibles, 4)
        color = random.choice(["black", "yellow", "green", "red"])

        try:
            board = Board()
            player = Player(color, board)
            for piece, pos in zip(player.pieces, setup):
                piece.position = pos
                piece.active = False if pos is None else True
            st_res = player.get_piece_positions()
        except Exception as e:
            print("\tCalling Player.get_piece_positions() caused an exception:")
            print("\t", e)
            print()
        else:
            for pos in setup:
                if pos not in st_res:
                    print("\tPlayer.get_piece_positions() returned wrong value")
                    print("\tExpected {}, got {}".format(setup, st_res))
                    print()
                    break
            else:
                passed += 1

    points = (passed / total) * 0.1
    print("Checking Player.get_piece_positions() finished: {:.2f}/0.1".format(points))
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


def test_get_valid_moves():
    print("Checking Player.get_valid_moves()")
    passed, total = 0, 0

    with open("test_files/get_valid_moves_tests.pkl", 'rb') as infile:
        test_cases = pickle.load(infile)

    for setup, (pl_id, roll), corr_res in test_cases:
        total += 1
        board, players = prepare_setup(setup)

        try:
            test_player = players[pl_id]
            st_res = test_player.get_valid_moves(roll)
        except Exception as e:
            print("\tCalling Player.get_valid_moves() caused an exception:")
            print("\t", e)
            print()
        else:
            st_coded = list()
            for piece, pos in st_res:
                p_id = test_player.pieces.index(piece)
                st_coded.append((p_id, pos))

            for elem in corr_res:
                if elem not in st_coded:
                    print("\tPlayer.get_valid_moves() returned wrong value")
                    print("\tExpected {}, got {} (player {}, roll {})".format(corr_res, st_coded, pl_id, roll))
                    print("\tSetup: {}".format(setup))
                    print()
                    break
            else:
                passed += 1

    points = (passed / total) * 0.5
    print("Checking Player.get_valid_moves() finished: {:.2f}/0.5".format(points))
    return points


def test_prepare_targets():
    print("Checking Player.prepare_targets()")
    passed, total = 0, 0

    with open("test_files/prepare_targets_tests.pkl", 'rb') as infile:
        test_cases = pickle.load(infile)

    for color, p_id, act, pos, rolls, final_pos in test_cases:
        total += 1

        try:
            board = Board()
            player = Player(color, board)

            piece = player.pieces[p_id]
            piece.active = act
            piece.position = pos

            moves = [(piece, r) for r in rolls]
            st_res = player.prepare_targets(moves)
        except Exception as e:
            print("\tCalling Player.prepare_targets() caused an exception:")
            print("\t", e)
            print()
        else:
            corr = [(piece, final_pos)]
            if st_res != corr:
                print("\tPlayer.prepare_targets() returned wrong value")
                print("\tExpected {}, got {}".format(corr, st_res))
                print("\tStarting position: {} (active={}), rolls {}".format(pos, act, rolls))
                print()
            else:
                passed += 1


    points = (passed / total) * 0.2
    print("Checking Player.prepare_targets() finished: {:.2f}/0.2".format(points))
    return points


def test_strategy(p_type):
    type_str = p_type.__name__
    print("Checking {}.get_move()".format(type_str))
    passed, total = 0, 0

    with open("test_files/get_move_tests_{}.pkl".format(type_str), 'rb') as infile:
        test_cases = pickle.load(infile)

    for setup, (pl_id, roll), (coded, det_coded) in test_cases:
        total += 1
        board, players = prepare_setup(setup)

        test_player = players[pl_id]

        try:
            st_res = test_player.get_move(roll)
        except Exception as e:
            print("\tCalling {}.get_move() caused an exception:".format(type_str))
            print("\t", e)
            print()
        else:
            allowed = [1]
            if len(coded) == 0:
                allowed.append(0)
            if not isinstance(st_res, list):
                print("\t{}.get_move() returned value of wrong type".format(type_str))
                print("\tExpected list, got {}".format(type(st_res)))
                print()
            elif len(st_res) not in allowed:
                print("\t{}.get_move() returned wrong value".format(type_str))
                print("\tExpected list with one value, got {}".format(len(st_res)))
                print()
            elif len(st_res) == 0:
                passed += 1
            elif not isinstance(st_res[0], tuple):
                print("\t{}.get_move() returned value of wrong type".format(type_str))
                print("\tExpected list with one tuple, got {}".format(type(st_res[0])))
                print()
            elif len(st_res[0]) != 2:
                print("\t{}.get_move() returned wrong value".format(type_str))
                print("\tExpected tuple with two values, got {}".format(len(st_res[0])))
                print()
            else:
                piece, pos = st_res[0]
                try:
                    p_id = test_player.pieces.index(piece)
                except ValueError:
                    print("\t{}.get_move() returned move for incorrect piece".format(type_str))
                    print("\tCannot find {} in {}".format(piece, test_player.pieces))
                    print()
                else:
                    st_coded = (p_id, pos)
                    if len(det_coded) != 0:
                        # check for deterministic
                        if [st_coded] not in det_coded:
                            print("\t{}.get_move() did not find deterministic move".format(type_str))
                            print("\t", test_player.get_piece_positions())
                            print("\tCannot find {} in {}".format(st_coded, det_coded))
                            print()
                        else:
                            passed += 1
                    else:
                        if st_coded not in coded:
                            print("\t{}.get_move() returned illegal move".format(type_str))
                            print("\tCannot find {} in {}".format(st_coded, coded))
                            print()
                        else:
                            passed += 1

    points = (passed / total)
    print("Checking {}.get_move() finished: {:.2f}/1".format(type_str, points))
    return points


def test_player():
    try:
        test_piece_structure()
        test_board_structure()
        test_player_structure()
    except RuntimeError:
        print("Cannot test Player class")
        return 0

    p1 = test_is_done()
    print()

    p2 = test_has_active()
    print()

    p3 = test_get_piece_positions()
    print()

    p4 = test_get_valid_moves()
    print()

    p5 = test_prepare_targets()
    print()

    total = sum([p1, p2, p3, p4, p5])
    print("PLAYER POINTS: {:.2f}/1".format(total))
    return total


if __name__ == '__main__':
    test_player()

    test_strategy(RandomPlayer)
    test_strategy(SafePlayer)
    test_strategy(MeanPlayer)
    test_strategy(EagerPlayer)
