import pickle
import random

from piece import Piece
from structure_tests import test_piece_structure


def test_activate():
    print("Checking Piece.activate()")
    has_error = False

    for color in ["black", "yellow", "green", "red"]:
        piece = Piece(color)

        if piece.active is not False:
            print("\tPiece.activate() test cannot run: piece should be inactive after calling constructor")
            print()
            has_error = True

        if piece.position is not None:
            print("\tPiece.activate() test cannot run: piece position should be None after calling constructor")
            print()
            has_error = True

        try:
            piece.activate()
        except Exception as e:
            print("\tCalling Piece.activate() caused an exception:")
            print("\t", e)
            print()
            has_error = True

        if piece.active is not True:
            print("\tCalling Piece.activate() did not activate Piece correctly")
            print("\tExpected Piece.active to be True, got", piece.active)
            print()
            has_error = True

        if piece.position != 0:
            print("\tCalling Piece.activate() did not activate Piece correctly")
            print("\tExpected Piece.position to be 0, got", piece.position)
            print()
            has_error = True

    points = 0.0 if has_error else 0.1
    print("Checking Piece.activate() finished: {:.1f}/0.1".format(points))
    return points


def test_throw_out():
    print("Checking Piece.throw_out()")
    has_error = False

    for color in ["black", "yellow", "green", "red"]:
        for _ in range(25):
            piece = Piece(color)
            piece.active = True
            piece.position = random.randint(0, 43)

            try:
                piece.throw_out()
            except Exception as e:
                print("\tCalling Piece.throw_out() caused an exception:")
                print("\t", e)
                print()
                has_error = True

            if piece.active is not False:
                print("\tCalling Piece.throw_out() did not update Piece correctly")
                print("\tExpected Piece.active to be False, got", piece.active)
                print()
                has_error = True

            if piece.position is not None:
                print("\tCalling Piece.throw_out() did not update Piece correctly")
                print("\tExpected Piece.position to be None, got", piece.position)
                print()
                has_error = True

    points = 0.0 if has_error else 0.1
    print("Checking Piece.throw_out() finished: {}/0.1".format(points))
    return points


def test_is_done():
    print("Checking Piece.is_done()")
    has_error = False

    with open("test_files/is_done_tests.pkl", 'rb') as infile:
        test_cases = pickle.load(infile)

    for color in ["black", "yellow", "green", "red"]:
        piece = Piece(color)
        piece.position = None

        try:
            st_res = piece.is_done()
        except Exception as e:
            print("\tCalling Piece.is_done() caused an exception:")
            print("\t", e)
            has_error = True
        else:
            if st_res is not False:
                print("\tPiece.is_done() returned wrong value for inactive piece")
                print("\tExpected False, got", st_res)
                print()
                has_error = True

    for color, pos, corr in test_cases:
        piece = Piece(color)
        piece.position = pos

        try:
            st_res = piece.is_done()
        except Exception as e:
            print("\tCalling Piece.is_done() caused an exception:")
            print("\t", e)
            has_error = True
        else:
            if st_res is not corr:
                print("\tPiece.is_done() returned wrong value for inactive piece")
                print("\tExpected {}, got {}".format(corr, st_res))
                print()
                has_error = True

    points = 0.0 if has_error else 0.1
    print("Checking Piece.is_done() finished: {}/0.1".format(points))
    return points


def test_move():
    print("Checking Piece.move()")
    has_error = False

    with open("test_files/move_tests.pkl", 'rb') as infile:
        test_cases = pickle.load(infile)

    for color, active, pos, roll, corr in test_cases:
        piece = Piece(color)
        piece.active = active
        piece.position = pos

        try:
            st_res = piece.move(roll)
        except Exception as e:
            print("\tCalling Piece.move() caused an exception:")
            print("\t", e)
            has_error = True
        else:
            if st_res != corr:
                print("\tPiece.move() returned wrong value")
                print("\tExpected {}, got {}".format(corr, st_res))
                print("\tPiece.active={}, Piece.position={}, steps={}".format(active, pos, roll))
                print()
                has_error = True

    points = 0.0 if has_error else 0.1
    print("Checking Piece.move() finished: {}/0.1".format(points))
    return points


def test_move_to_place():
    print("Checking Piece.move_to_place()")
    has_error = False

    for _ in range(100):
        color = random.choice(["black", "yellow", "green", "red"])
        position = random.randint(0, 43)
        piece = Piece(color)

        try:
            piece.move_to_place(position)
        except Exception as e:
            print("\tCalling Piece.move_to_place() caused an exception:")
            print("\t", e)
            has_error = True
        else:
            if piece.position != position:
                print("\tPiece.move_to_place() did not move the piece correctly")
                print("\tExpected {}, found {}".format(position, piece.position))
                print()
                has_error = True

    points = 0.0 if has_error else 0.1
    print("Checking Piece.move_to_place() finished: {}/0.1".format(points))
    return points


def test_piece():
    try:
        test_piece_structure()
    except RuntimeError:
        print("Cannot test Piece class")
        return 0

    p1 = test_activate()
    print()

    p2 = test_throw_out()
    print()

    p3 = test_is_done()
    print()

    p4 = test_move()
    print()

    p5 = test_move_to_place()
    print()

    total = sum([p1, p2, p3, p4, p5])
    print("PIECE POINTS: {:.1f}/0.5".format(total))
    return total


if __name__ == '__main__':
    test_piece()
