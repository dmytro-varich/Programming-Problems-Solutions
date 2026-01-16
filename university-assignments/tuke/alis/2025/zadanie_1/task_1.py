"""
Logic Puzzle - 4 Houses

Four houses in a row, each with different characteristics:
- Color: black, blue, red, white
- Nationality: American, British, Canadian, Irish
- Animal: butterflies, dolphins, horses, turtles
- Sport: bowling, handball, swimming, tennis

The houses are arranged in a straight line, with the first being the furthest to the left.
When it says there is "one house" between two houses, it means there is exactly one house
between them (e.g., house 1 and house 3 have one house between them).
"""

import sys 
import logging

# Add the path to zebra project
sys.path.insert(0, r'c:\Users\admin\Desktop\github_pr\zebra')

from src import sat_utils
from src.clues import (
    consecutive,
    found_at,
    left_of,
    one_between,
    right_of,
    same_house,
    two_between,
)
from src.elements import PuzzleElement
from src.puzzle import Puzzle

logging.basicConfig(level=logging.INFO)


class Color(PuzzleElement):
    @classmethod
    def description(cls) -> str:
        return "House colors: black, blue, red, white."

    black = "Black house"
    blue = "Blue house"
    red = "Red house"
    white = "White house"

class Nationality(PuzzleElement):
    @classmethod
    def description(cls) -> str:
        return "Nationalities: American, British, Canadian, Irish."

    american = "American"
    british = "British"
    canadian = "Canadian"
    irish = "Irish"


class Animal(PuzzleElement):
    @classmethod
    def description(cls) -> str:
        return "Favorite animals: butterflies, dolphins, horses, turtles."

    butterflies = "the person who likes Butterflies"
    dolphins = "the person who likes Dolphins"
    horses = "the person who likes Horses"
    turtles = "the person who likes Turtles"


class Sport(PuzzleElement):
    @classmethod
    def description(cls) -> str:
        return "Favorite sports: bowling, handball, swimming, tennis."

    bowling = "the person who likes Bowling"
    handball = "the person who likes Handball"
    swimming = "the person who likes Swimming"
    tennis = "the person who likes Tennis"


if __name__ == "__main__":
    # Define puzzle parameters
    element_types: list[type[PuzzleElement]] = [Color, Nationality, Animal, Sport]
    literals = [el for group in element_types for el in group]

    # Create solution dictionary with all puzzle elements
    # Values don't matter for initialization, will be determined by solver
    solution = {el: 0 for el in literals}

    # set up the puzzle with constraints and clues
    puzzle = Puzzle(element_types=element_types, solution=solution)
    
    puzzle = (
        puzzle
        # 1. There are two houses between the person who likes Bowling and the person who likes Swimming.
        .add_clue(two_between(Sport.bowling, Sport.swimming, puzzle.houses))
        # 2. There is one house between the Irish and the person who likes Handball on the left.
        .add_clue(one_between(Nationality.irish, Sport.handball, puzzle.houses))
        .add_clue(left_of(Sport.handball, Nationality.irish, puzzle.houses))
        # 3. The second house is Black.
        .add_clue(found_at(Color.black, 2))
        # 4. There is one house between the person who likes Horses and the Red house on the right.
        .add_clue(one_between(Animal.horses, Color.red, puzzle.houses))
        .add_clue(right_of(Color.red, Animal.horses, puzzle.houses))
        # 5. The American lives directly to the left of the person who likes Turtles.
        .add_clue(consecutive(Nationality.american, Animal.turtles, puzzle.houses))
        # 6. There are two houses between the person who likes Horses and the person who likes Butterflies on the right.
        .add_clue(two_between(Animal.horses, Animal.butterflies, puzzle.houses))
        .add_clue(right_of(Animal.butterflies, Animal.horses, puzzle.houses))
        # 7. The person who likes Bowling lives somewhere to the right of the person who likes Tennis.
        .add_clue(right_of(Sport.bowling, Sport.tennis, puzzle.houses))
        # 8. There is one house between the person who likes Handball and the White house on the right.
        .add_clue(one_between(Sport.handball, Color.white, puzzle.houses))
        .add_clue(right_of(Color.white, Sport.handball, puzzle.houses))
        # 9. The British lives in the first house.
        .add_clue(found_at(Nationality.british, 1))
    )

    logging.info(puzzle)
    
    # Output N rules (clues)
    print("\n=== RULES (CLUES) ===")
    for i, clue in enumerate(puzzle.clues, 1):
        print(f"{i}. {clue}")
    
    # Get CNF and clues
    cnf = puzzle.as_cnf()
    
    # Solve Puzzle
    print(f"\n=== SOLVING ===")
    all_solutions = list(sat_utils.itersolve(cnf))
    logging.info(f"{len(all_solutions)} solutions found")
    print(f"{len(all_solutions)} solutions found")
    
    if all_solutions:
        print(f"\n=== SOLUTION ===")
        for solution in all_solutions:
            print("\nSolution:")
            for house in puzzle.houses:
                print(f"\nHouse {house}:")
                house_elements = [s for s in solution if s.endswith(f" {house}")]
                for element in house_elements:
                    print(f"  {element}")