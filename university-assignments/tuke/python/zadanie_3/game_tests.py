import random

from game import Game, find_best_strategy
from player import *

from structure_tests import *


def test_get_player_rolls():
    print("Checking Game.get_player_rolls()")
    passed, total = 0, 0

    try:
        test_game = Game([RandomPlayer, RandomPlayer, RandomPlayer, RandomPlayer])
    except Exception as e:
        print("\tCould not create Game object:")
        print("\t", e)
        print()
        return 0

    inactive_p = test_game.players[0]
    active_p = test_game.players[1]

    active_piece = active_p.pieces[0]
    active_piece.active = True
    active_piece.position = random.randint(1, 39)

    # player does not have active
    for _ in range(1000):
        total += 1
        st_res = test_game.get_player_rolls(inactive_p)

        if not isinstance(st_res, list):
            print("\tGame.get_player_rolls() returned wrong value type:")
            print("\tExpected list, got {}".format(type(st_res)))
            print()
        elif not all([isinstance(elem, int) for elem in st_res]):
            print("\tGame.get_player_rolls() returned wrong value type:")
            print("\tExpected integers, got {}".format([type(elem) for elem in st_res]))
            print()
        else:
            correct = True
            if 6 not in st_res:
                if len(st_res) != 3:
                    correct = False
            elif st_res[-1] == 6 or st_res[-2] != 6:
                correct = False

            if not correct:
                print("\tGame.get_player_rolls() returned invalid rolls for inactive player")
                print("\t", st_res)
                print()
            passed += correct

    # player has active pieces
    for _ in range(1000):
        total += 1
        st_res = test_game.get_player_rolls(active_p)

        if not isinstance(st_res, list):
            print("\tGame.get_player_rolls() returned wrong value type:")
            print("\tExpected list, got {}".format(type(st_res)))
            print()
        elif not all([isinstance(elem, int) for elem in st_res]):
            print("\tGame.get_player_rolls() returned wrong value type:")
            print("\tExpected integers, got {}".format([type(elem) for elem in st_res]))
            print()
        else:
            correct = True
            if 6 not in st_res:
                if len(st_res) != 1:
                    correct = False
            elif st_res[-1] == 6 or st_res[-2] != 6:
                correct = False

            if not correct:
                print("\tGame.get_player_rolls() returned invalid rolls for active player")
                print("\t", st_res)
                print()
            passed += correct

    points = (passed / total)
    print("Checking Game.get_player_rolls() finished: {:.2f}/1".format(points))
    return points


def test_run_game():
    print("Checking Game.run_game()")
    passed, total = 0, 0

    lengths = list()
    orders = list()

    for _ in range(100):
        total += 1
        p_types = [random.choice([RandomPlayer, SafePlayer, MeanPlayer, EagerPlayer]) for _ in range(4)]

        try:
            test_game = Game(p_types)

            length, order = test_game.run_game()
        except Exception as e:
            print("\tCalling Game.run_game() caused an exception:")
            print("\t", e)
            print()
        else:
            # test return value types
            if not isinstance(length, int):
                print("\tGame.run_game() returned wrong value type")
                print("\tExpected first int, got {}".format(type(length)))
                print()
                break
            if not isinstance(order, list):
                print("\tGame.run_game() returned wrong value type")
                print("\tExpected second list, got {}".format(type(order)))
                print()
                break

            for player in test_game.players:
                # test all players in order
                if player not in order:
                    print("\tCould not find player {} in final order: {}".format(player, order))
                    print()
                    break

                # test all pieces in house
                piece_actives = [piece.active for piece in player.pieces]
                piece_positions = [piece.position for piece in player.pieces]
                for num in [40, 41, 42, 43]:
                    if num not in piece_positions:
                        print("\tCould not find piece on position {}".format(num))
                        print("\tPiece positions: {}".format(piece_positions))
                        print()
                        break

            # test board empty
            for idx, cell in enumerate(test_game.board.board):
                if cell is not None:
                    print("\tBoard should be empty at the end of a game")
                    print("\tFound {} at position {}".format(cell, idx))
                    print()
                    break

            lengths.append(length)

            coded_order = [test_game.players.index(player) for player in order]
            orders.append(tuple(coded_order))
            passed += 1

    if len(set(lengths)) == 1 or len(set(orders)) == 1:
        print("\tGame.run_game() should not return the same value all the time")
        print()
        passed = 0

    points = (passed / total)
    print("Checking Game.run_game() finished: {:.2f}/1".format(points))
    return points


def test_find_best_strategy():
    print("Checking find_best_strategy()")
    passed, total = 0, 0

    for _ in range(25):
        correct = True
        total += 1
        p_types = [random.choice([RandomPlayer, SafePlayer, MeanPlayer, EagerPlayer]) for _ in range(4)]
        runs = random.randint(20, 50)

        try:
            winning, overview = find_best_strategy(p_types, runs)
        except Exception as e:
            print("Calling find_best_strategy() caused an error:")
            print("\t", e)
            print()
            correct = False
        else:
            # first is player type
            if winning not in p_types:
                print("\tfind_best_strategy() returned wrong value")
                print("\tExpected type from {}, got {}".format(p_types, winning))
                print()
                correct = False

            # is dictionary
            elif not isinstance(overview, dict):
                print("\tfind_best_strategy() returned wrong value type")
                print("\tExpected second value to be dict, got {}".format(type(overview)))
                print()
                correct = False

            # all player types in keys
            else:
                for p_type in p_types:
                    if p_type not in overview:
                        print("\tfind_best_strategy() returned wrong value")
                        print("\tDid not find {} in result {}".format(p_type, overview))
                        print()
                        correct = False
                    elif not isinstance(overview[p_type], int):
                        print("\tfind_best_strategy() returned wrong value type")
                        print("\tExpected dictionary values to be integers, got {}".format(type(overview[p_type])))
                        print()
                        correct = False
                else:
                    # sum is equal to runs?
                    total_runs = sum([val for val in overview.values()])
                    if total_runs != runs:
                        print("\tfind_best_strategy() returned wrong value")
                        print("\tExpected {} total runs, found {} ({})".format(runs, total_runs, overview))
                        print()
                        correct = False

            passed += correct

    points = (passed / total) * 0.5
    print("Checking find_best_strategy() finished: {:.2f}/0.5".format(points))
    return points


def test_game():
    try:
        test_piece_structure()
        test_board_structure()
        test_player_structure()
        test_game_structure()
    except RuntimeError:
        print("Cannot test Game class")
        return 0

    p1 = test_get_player_rolls()
    print()

    p2 = test_run_game()
    print()

    p3 = test_find_best_strategy()
    print()

    total = sum([p1, p2, p3])
    print("GAME POINTS: {:.2f}/2.5".format(total))
    return total


if __name__ == '__main__':
    test_game()
