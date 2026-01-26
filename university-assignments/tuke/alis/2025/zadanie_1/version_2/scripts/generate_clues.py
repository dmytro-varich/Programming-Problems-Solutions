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
from enum import StrEnum
from typing import List, Tuple


class PuzzleElement(StrEnum):
    """
    Common parent class for all puzzle elements (colors, occupations, pets, etc.).
    """

    @classmethod
    def description(cls) -> str:
        return "".join(cls.__members__)


class Color(PuzzleElement):
    @classmethod
    def description(cls) -> str:
        return "House colors: black, blue, red, white."

    black = "black"
    blue = "blue"
    red = "red"
    white = "white"


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

    butterflies = "butterflies"
    dolphins = "dolphins"
    horses = "horses"
    turtles = "turtles"


class Sport(PuzzleElement):
    @classmethod
    def description(cls) -> str:
        return "Favorite sports: bowling, handball, swimming, tennis."

    bowling = "bowling"
    handball = "handball"
    swimming = "swimming"
    tennis = "tennis"
  

class CNFFormula:
    """
    A wrapper class for pretty-printing CNF (Conjunctive Normal Form) formulas.
    
    Provides methods for displaying logical formulas in a human-readable format
    with conjunction (∧) symbols and line breaks, while also allowing programmatic
    access to individual clauses.
    """
    def __init__(self, clauses: List[str]):
        self._clauses = clauses
    
    def __repr__(self) -> str:
        """Returns the formula as a conjunction of disjunctions with proper formatting."""
        if not self._clauses:
            return "⊤"  # True (empty formula)
        
        # Format each clause
        formatted_clauses = []
        for clause in self._clauses:
            formatted_clauses.append(f"({clause})")
        
        # Join with ∧ and line breaks
        return " ∧\n".join(formatted_clauses)
    
    def __str__(self) -> str:
        """For pretty printing with print()."""
        return self.__repr__()
    
    def to_list(self) -> List[str]:
        """Returns a copy of the clauses list for programmatic processing."""
        return self._clauses.copy()
    
    def __iter__(self):
        """Allows iteration over clauses."""
        return iter(self._clauses)
    
    def __len__(self) -> int:
        """Returns the number of clauses."""
        return len(self._clauses)
    
    def __getitem__(self, index: int) -> str:
        """Allows index access: formula[0]."""
        return self._clauses[index]    
    
    def to_dimacs(self, var_mapping: dict = None) -> Tuple[List[str], dict]:
        """
        Converts the CNF formula to DIMACS format.
        
        Args:
            var_mapping: Optional existing variable mapping to continue from
        
        Returns:
            Tuple of (dimacs_clauses, var_mapping)
            - dimacs_clauses: List of clauses in DIMACS format (e.g., "1 -2 3 0")
            - var_mapping: Dictionary mapping variable names to integers
        
        Example:
            formula = CNFFormula(["C_1_black ∨ C_1_blue", "¬C_1_black ∨ ¬C_1_blue"])
            dimacs_clauses, mapping = formula.to_dimacs()
            # dimacs_clauses: ["1 2 0", "-1 -2 0"]
            # mapping: {"C_1_black": 1, "C_1_blue": 2}
        """
        if var_mapping is None:
            var_mapping = {}
            var_counter = 1
        else:
            var_counter = max(var_mapping.values()) + 1 if var_mapping else 1
        
        dimacs_clauses = []
        
        for clause in self._clauses:
            # Split by ∨ to get individual literals
            literals = clause.split(" ∨ ")
            dimacs_literals = []
            
            for literal in literals:
                literal = literal.strip()
                is_negated = literal.startswith("¬")
                var_name = literal.lstrip("¬").strip()
                
                # Add to mapping if not present
                if var_name not in var_mapping:
                    var_mapping[var_name] = var_counter
                    var_counter += 1
                
                var_num = var_mapping[var_name]
                dimacs_literal = f"-{var_num}" if is_negated else str(var_num)
                dimacs_literals.append(dimacs_literal)
            
            dimacs_clauses.append(" ".join(dimacs_literals) + " 0")
        
        return dimacs_clauses, var_mapping
    

class Constraint:
    """
    Represents a binary positional constraint between two puzzle elements.

    The constraint encodes spatial relations such as:
    - exact distance between two properties,
    - one property being somewhere to the left or right of another,
    - relative ordering with optional direction.

    The constraint can be translated into logical implications or CNF clauses
    suitable for SAT solving.
    """
    def __init__(self, prop1: PuzzleElement, prop2: PuzzleElement, distance: int, num_houses: int):
        self.prop1 = prop1
        self.prop2 = prop2
        self.distance = distance
        self.num_houses = num_houses
        self.left_prop = None   # Which property is on the left
        self.right_prop = None  # Which property is on the right
        self.anywhere_left = False  # Flag for "somewhere to the left"
        self.anywhere_right = False # Flag for "somewhere to the right"

    def _get_prefix(self, prop: PuzzleElement) -> str:
        """Returns the category prefix (C for Color, N for Nationality, A for Animal, S for Sport)."""
        return prop.__class__.__name__[0].upper()
    
    def _make_var(self, prop: PuzzleElement, position: int) -> str:
        """Creates a variable name in the format: C_1_black."""
        return f"{self._get_prefix(prop)}_{position}_{prop}" 

    def left_of(self, left: PuzzleElement, right: PuzzleElement) -> 'Constraint':
        """
        Specifies that the left property is to the left of the right property.
        
        Example:
            one_between(A, B).left_of(A, B) means A is left, B is right
        """
        self.left_prop, self.right_prop = left, right
        return self
    
    def right_of(self, right: PuzzleElement, left: PuzzleElement) -> 'Constraint':
        """
        Specifies that the right property is to the right of the left property.
        
        Example:
            one_between(A, B).right_of(B, A) means A is left, B is right
        """
        self.left_prop, self.right_prop = left, right
        return self
    
    def to_forbidden_implications(self, *, cnf_form: bool = False) -> CNFFormula:
        """
        Generates forbidden implications based on the constraint type.
        
        Args:
            cnf_form: If True, returns clauses in CNF format (¬p ∨ ¬q).
                      If False, returns implications (p → ¬q).
        
        Returns:
            CNFFormula object containing the generated clauses.
        """
        clauses = []
        
        def make_clause(var1: str, var2: str, cnf: bool) -> str:
            if not cnf:
                return f"{var1} -> ¬{var2}"
            else:
                return f"¬{var1} ∨ ¬{var2}"
        
        if self.anywhere_right:
            for i in range(1, self.num_houses + 1):
                for j in range(i, self.num_houses + 1):  # j >= i
                    clause = make_clause(
                        self._make_var(self.right_prop, i), 
                        self._make_var(self.left_prop, j), 
                        cnf_form
                    )
                    clauses.append(clause)
        elif self.anywhere_left:
                    for i in range(1, self.num_houses + 1):
                        for j in range(1, i + 1):  # j <= i
                            clause = make_clause(
                                self._make_var(self.left_prop, i), 
                                self._make_var(self.right_prop, j), 
                                cnf_form
                            )
                            clauses.append(clause)
        elif self.left_prop and self.right_prop: 
            for i in range(1, self.num_houses + 1):
                for j in range(1, self.num_houses + 1):
                    if j != i + self.distance:
                        clause = make_clause(
                            self._make_var(self.left_prop, i), 
                            self._make_var(self.right_prop, j), 
                            cnf_form
                        )
                        clauses.append(clause)
        else: 
            for i in range(1, self.num_houses + 1):
                for j in range(1, self.num_houses + 1):
                    if abs(i - j) != self.distance:
                        clause = make_clause(
                            self._make_var(self.prop1, i), 
                            self._make_var(self.prop2, j), 
                            cnf_form
                        )
                        clauses.append(clause)
                        
        return CNFFormula(clauses)                
        
        
class PuzzleConstraints:
    """
    Factory class for creating logical constraints for a house-based logic puzzle.

    Provides high-level methods to express common puzzle clues such as:
    - a property being at (or not at) a specific position,
    - two properties belonging to the same house,
    - relative positioning (left/right, consecutive, with gaps).

    All constraints are converted into propositional logic or CNF formulas
    compatible with SAT solvers.
    """
    def __init__(self, num_houses: int = 4):
        self.num_houses = num_houses
    
    def found_at(self, property: PuzzleElement, position: int) -> CNFFormula:
        """
        Generates a clue that a certain property is found at a specific position.
        
        Example:
            found_at(Color.black, 2) -> ["C_2_black"]
            Meaning: The black house is in position 2
        """
        constraint = Constraint(property, None, distance=0, num_houses=self.num_houses)
        return CNFFormula([constraint._make_var(property, position)])

    def not_at(self, property: PuzzleElement, position: int) -> CNFFormula:
        """
        Generates a clue that a certain property is NOT found at a specific position.
        
        Example:
            not_at(Color.red, 3) -> ["¬C_3_red"]
            Meaning: The red house is not in position 3
        """
        constraint = Constraint(property, None, distance=0, num_houses=self.num_houses)
        var = constraint._make_var(property, position)
        return CNFFormula([f"¬{var}"])
    
    def same_house(
        self, 
        property1: PuzzleElement, 
        property2: PuzzleElement, 
        *,
        cnf_form: bool = False
    ) -> CNFFormula:
        """
        Generates clues that two properties are in the same house.
        
        Args:
            cnf_form: If True, returns CNF clauses; if False, returns biconditionals
        
        Example:
            same_house(Color.red, Nationality.american) ->
            ["C_1_red ↔ N_1_American", "C_2_red ↔ N_2_American", ...]
            
            same_house(Color.red, Nationality.american, cnf_form=True) ->
            ["¬C_1_red ∨ N_1_American", "¬N_1_American ∨ C_1_red", ...]
        """
        clues = []
        constraint = Constraint(property1, property2, distance=0, num_houses=self.num_houses)
        if not cnf_form:
            for i in range(1, self.num_houses + 1):
                clue = f"{constraint._get_prefix(property1)}_{i}_{property1} " \
                    f"↔ {constraint._get_prefix(property2)}_{i}_{property2}"
                clues.append(clue)
        else: 
            for i in range(1, self.num_houses + 1):
                clue1 = f"¬{constraint._get_prefix(property1)}_{i}_{property1} " \
                    f"∨ {constraint._get_prefix(property2)}_{i}_{property2}"
                clue2 = f"¬{constraint._get_prefix(property2)}_{i}_{property2} " \
                    f"∨ {constraint._get_prefix(property1)}_{i}_{property1}"
                clues.append(clue1)
                clues.append(clue2)
        return CNFFormula(clues)
    
    def consecutive(self, property1: PuzzleElement, property2: PuzzleElement) -> Constraint:
        """
        Creates a constraint stating that the two properties are in adjacent houses.

        The order is not fixed unless further specified using left_of or right_of.

        Examples:
            consecutive(Color.red, Nationality.english)
                → The red house and the English person live in neighboring houses.

            consecutive(A, B).left_of(A, B)
                → A is immediately to the left of B.
        """
        return Constraint(property1, property2, distance=1, num_houses=self.num_houses)
    
    def one_between(self, property1: PuzzleElement, property2: PuzzleElement) -> Constraint:
        """
        Creates a constraint stating that exactly one house lies between the two properties.

        The relative order is unspecified unless combined with left_of or right_of.

        Examples:
            one_between(Animal.cat, Color.green)
                → There is exactly one house between the cat and the green house.

            one_between(A, B).right_of(B, A)
                → A is two positions to the left of B.
        """
        return Constraint(property1, property2, distance=2, num_houses=self.num_houses)
    
    def two_between(self, property1: PuzzleElement, property2: PuzzleElement) -> Constraint:
        """
        Creates a constraint stating that exactly two houses lie between the two properties.

        This corresponds to a fixed distance of three positions.

        Examples:
            two_between(Nationality.norwegian, Sport.tennis)
                → There are exactly two houses between the Norwegian and the tennis player.

            two_between(A, B).left_of(A, B)
                → A is three positions to the left of B.
        """
        return Constraint(property1, property2, distance=3, num_houses=self.num_houses)

    def right_of(self, right_property: PuzzleElement, left_property: PuzzleElement) -> Constraint:
        """
        Creates a constraint stating that one property is located somewhere to the right
        of another property, with no restriction on exact distance.

        Examples:
            right_of(Color.blue, Color.red)
                → The blue house is somewhere to the right of the red house.

            one_between(A, B).right_of(B, A)
                → B is two houses to the right of A.
        """
        constraint = Constraint(left_property, right_property, distance=0, num_houses=self.num_houses)
        constraint.left_prop = left_property
        constraint.right_prop = right_property
        constraint.anywhere_right = True 
        return constraint
    
    def left_of(self, left_property: PuzzleElement, right_property: PuzzleElement) -> Constraint:
        """
        Creates a constraint stating that one property is located somewhere to the left
        of another property, with no restriction on exact distance.

        Examples:
            left_of(Nationality.german, Color.white)
                → The German lives somewhere to the left of the white house.

            consecutive(A, B).left_of(A, B)
                → A is immediately to the left of B.
        """
        constraint = Constraint(left_property, right_property, distance=0, num_houses=self.num_houses)
        constraint.left_prop = left_property
        constraint.right_prop = right_property
        constraint.anywhere_left = True
        return constraint
    
    def at_least_one_value_per_house(self, property_class: type[PuzzleElement]) -> CNFFormula:
        """
        Generates constraints ensuring each house has at least one value for a given property.
        
        For every house i ∈ H:
            ⋁_{v ∈ Domain(X)} (X(i) = v)
        
        Example:
            at_least_one_value_per_house(Color) ->
            For house 1: (C_1_black ∨ C_1_blue ∨ C_1_red ∨ C_1_white)
            For house 2: (C_2_black ∨ C_2_blue ∨ C_2_red ∨ C_2_white)
            ...
        """
        clauses = []
        constraint = Constraint(None, None, distance=0, num_houses=self.num_houses)
        
        for i in range(1, self.num_houses + 1):
            # Create disjunction of all possible values for this house
            literals = []
            for value in property_class:
                var = constraint._make_var(value, i)
                literals.append(var)
            
            clause = " ∨ ".join(literals)
            clauses.append(clause)
        
        return CNFFormula(clauses)
    
    def at_most_one_value_per_house(self, property_class: type[PuzzleElement]) -> CNFFormula:
        """
        Generates constraints ensuring each house has at most one value for a given property.
        
        For every house i ∈ H and every pair of values u, v (u ≠ v):
            ¬(X(i)=u ∧ X(i)=v)  ≡  ¬X(i)=u ∨ ¬X(i)=v
        
        Example:
            at_most_one_value_per_house(Color) ->
            For house 1: (¬C_1_black ∨ ¬C_1_blue), (¬C_1_black ∨ ¬C_1_red), ...
        """
        clauses = []
        constraint = Constraint(None, None, distance=0, num_houses=self.num_houses)
        values = list(property_class)
        
        for i in range(1, self.num_houses + 1):
            # For each pair of different values
            for idx1 in range(len(values)):
                for idx2 in range(idx1 + 1, len(values)):
                    var1 = constraint._make_var(values[idx1], i)
                    var2 = constraint._make_var(values[idx2], i)
                    clause = f"¬{var1} ∨ ¬{var2}"
                    clauses.append(clause)
        
        return CNFFormula(clauses)
    
    def exactly_one_value_per_house(self, property_class: type[PuzzleElement]) -> CNFFormula:
        """
        Combines at_least_one and at_most_one constraints.
        
        Ensures each house has exactly one value for the given property.
        
        Example:
            exactly_one_value_per_house(Color) ->
            Combines clauses from at_least_one and at_most_one
        """
        at_least = self.at_least_one_value_per_house(property_class)
        at_most = self.at_most_one_value_per_house(property_class)
        
        combined_clauses = at_least.to_list() + at_most.to_list()
        return CNFFormula(combined_clauses)
    
    def each_value_used_once(self, property_class: type[PuzzleElement]) -> CNFFormula:
        """
        Generates constraints ensuring each property value is used exactly once across all houses.
        
        For every value v ∈ Domain(X) and every pair of houses i, j (i ≠ j):
            ¬(X(i)=v ∧ X(j)=v)  ≡  ¬X(i)=v ∨ ¬X(j)=v
        
        Example:
            each_value_used_once(Color) ->
            For black: (¬C_1_black ∨ ¬C_2_black), (¬C_1_black ∨ ¬C_3_black), ...
        """
        clauses = []
        constraint = Constraint(None, None, distance=0, num_houses=self.num_houses)
        
        for value in property_class:
            # For each pair of different houses
            for i in range(1, self.num_houses + 1):
                for j in range(i + 1, self.num_houses + 1):
                    var_i = constraint._make_var(value, i)
                    var_j = constraint._make_var(value, j)
                    clause = f"¬{var_i} ∨ ¬{var_j}"
                    clauses.append(clause)
        
        return CNFFormula(clauses)
    
    def generate_base_constraints(self, property_classes: list[type[PuzzleElement]]) -> List[CNFFormula]:
        """
        Generates all base constraints for the puzzle.
        
        Returns a list of CNFFormula objects containing:
        1. Exactly one value per house for each property type
        2. Each value used exactly once across all houses
        
        This ensures a valid puzzle configuration.
        """
        base_constraints = []
        
        for prop_class in property_classes:
            # Each house has exactly one value
            base_constraints.append(self.exactly_one_value_per_house(prop_class))
            
            # Each value is used exactly once
            base_constraints.append(self.each_value_used_once(prop_class))
        
        return base_constraints
    
    
def display_generated_clues(clues: List[CNFFormula]) -> None:
    """Displays the generated clues in a readable format."""
    for idx, cnf_constraint in enumerate(clues, start=1):
        print(f"\n=== Rule {idx} ===")
        print(cnf_constraint)


def display_lengths_of_clauses(clues: List[CNFFormula]) -> None:
    """Displays the lengths of the CNF formulas for each clue."""
    from tabulate import tabulate
    print("\n=== Lengths of CNF Formulas ===")
    data = [(f'Rule #{idx}', len(clue)) for idx, clue in enumerate(clues, start=1)]
    header = ["Rule Number", "CNF Length"]
    total = sum(len(clue) for clue in clues)
    print(tabulate(data, headers=header, tablefmt="grid"))
    print(f"Total CNF clauses: {total}")


def save_clues_to_file(clues: List[CNFFormula], file_path: str = "puzzle_clues.txt") -> None:
    """Saves the generated clues to a specified file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for idx, cnf_constraint in enumerate(clues, start=1):
            if idx == len(clues):
                file.write(repr(cnf_constraint) + "\n")
            else:
                file.write(repr(cnf_constraint) + " ∧\n")  
            

def save_clues_to_dimacs(clues: List[CNFFormula], file_path: str = "puzzle.cnf") -> None:
    """
    Saves all clues to DIMACS format for SAT solvers.
    
    Creates two files:
    - .cnf file with DIMACS format
    - _mapping.txt file with variable mapping
    """
    all_dimacs_clauses = []
    var_mapping = {}
    
    # Convert all CNFFormulas to DIMACS
    for cnf_formula in clues:
        dimacs_clauses, var_mapping = cnf_formula.to_dimacs(var_mapping)
        all_dimacs_clauses.extend(dimacs_clauses)
    
    # Write DIMACS file
    with open(file_path, 'w', encoding='utf-8') as file:
        # Header: p cnf <num_vars> <num_clauses>
        file.write(f"p cnf {len(var_mapping)} {len(all_dimacs_clauses)}\n")
        
        # Write all clauses
        for clause in all_dimacs_clauses:
            file.write(clause + "\n")
    
    # Write mapping file
    mapping_file = file_path.replace('.cnf', '_mapping.txt')
    with open(mapping_file, 'w', encoding='utf-8') as file:
        file.write("Variable Mapping:\n")
        file.write("=" * 50 + "\n")
        for var_name, var_num in sorted(var_mapping.items(), key=lambda x: x[1]):
            file.write(f"{var_num}: {var_name}\n")
    
    print(f"\nDIMACS format saved to {file_path}")
    print(f"Variable mapping saved to {mapping_file}")
    print(f"Total variables: {len(var_mapping)}")
    print(f"Total clauses: {len(all_dimacs_clauses)}")


def generate_clues():
    puzzle = PuzzleConstraints(num_houses=4)
    property_classes = [Color, Nationality, Animal, Sport]
    
    # === BASE CONSTRAINTS ===
    base_constraints = puzzle.generate_base_constraints(property_classes)
    
    # === PUZZLE CLUES ===
    
    # Rule 1: There are two houses between the person who likes Bowling and the person who likes Swimming.
    constraint1 = puzzle.two_between(Sport.bowling, Sport.swimming)
    cnf_constraint1 = constraint1.to_forbidden_implications(cnf_form=True)
    
    # Rule 2: There is one house between the Irish and the person who likes Handball on the left.
    constraint2 = puzzle.one_between(Nationality.irish, Sport.handball).left_of(Sport.handball, Nationality.irish)
    cnf_constraint2 = constraint2.to_forbidden_implications(cnf_form=True)
    
    # Rule 3: The black house is in the second position.
    constraint3 = puzzle.found_at(Color.black, 2)
    
    # Rule 4: There is one house between the person who likes Horses and the Red house on the right.
    constraint4 = puzzle.one_between(Animal.horses, Color.red).right_of(Color.red, Animal.horses)
    cnf_constraint4 = constraint4.to_forbidden_implications(cnf_form=True)
    
    # Rule 5: The American lives directly to the left of the person who likes Turtles.
    constraint5 = puzzle.consecutive(Nationality.american, Animal.turtles).left_of(Nationality.american, Animal.turtles)
    cnf_constraint5 = constraint5.to_forbidden_implications(cnf_form=True)
    
    # Rule 6: There are two houses between the person who likes Horses and the person who likes Butterflies on the right.
    constraint6 = puzzle.two_between(Animal.horses, Animal.butterflies).right_of(Animal.butterflies, Animal.horses)
    cnf_constraint6 = constraint6.to_forbidden_implications(cnf_form=True)
    
    # Rule 7: The person who likes Bowling lives somewhere to the right of the person who likes Tennis.
    constraint7 = puzzle.right_of(Sport.bowling, Sport.tennis)
    cnf_constraint7 = constraint7.to_forbidden_implications(cnf_form=True)
    
    # Rule 8: There is one house between the person who likes Handball and the White house on the right.
    constraint8 = puzzle.one_between(Sport.handball, Color.white).right_of(Color.white, Sport.handball)
    cnf_constraint8 = constraint8.to_forbidden_implications(cnf_form=True)
    
    # Rule 9: The British person lives in the first house.
    constraint9 = puzzle.found_at(Nationality.british, 1)

    # Collect all clues
    clues = base_constraints + [
        cnf_constraint1,
        cnf_constraint2,
        constraint3,
        cnf_constraint4,
        cnf_constraint5,
        cnf_constraint6,
        cnf_constraint7,
        cnf_constraint8,
        constraint9
    ]
    
    return clues
    

def main(file_path: str = "puzzle_clues.txt", 
         use_dimacs: bool = False,
         show_clues: bool = False,
         show_stats: bool = False): 
    # Generate clues
    clues = generate_clues()
    
    # Display clues if requested
    if show_clues:
        display_generated_clues(clues)
    
    # Display statistics if requested
    if show_stats:
        display_lengths_of_clauses(clues)
    
    # Save to file
    if use_dimacs:
        dimacs_path = file_path.replace('.txt', '.cnf')
        save_clues_to_dimacs(clues, file_path=dimacs_path)
    else:
        save_clues_to_file(clues, file_path=file_path)


if __name__ == "__main__":
    """
    Usage: 
        # Save clues to default file
        python generate_clues.py

        # Save clues + show clues
        python generate_clues.py --show-clues

        # Save clues + show stats
        python generate_clues.py --show-stats

        # Save clues + show all
        python generate_clues.py --show-clues --show-stats

        # DIMACS format + show all
        python generate_clues.py --dimacs --show-clues --show-stats

        # Custom file name + all options
        python generate_clues.py my_puzzle.txt --show-clues --show-stats --dimacs
    """
    # Parse command line arguments
    args = sys.argv[1:]
    
    use_dimacs = "--dimacs" in args
    show_clues = "--show-clues" in args
    show_stats = "--show-stats" in args
    
    # Remove flags from args to get file path
    file_args = [arg for arg in args if not arg.startswith("--")]
    
    # Determine file path
    if file_args:
        file_path = file_args[0]
    else:
        file_path = "puzzle_clues.txt"
        
    # Print usage information
    print("Usage: python generate_clues.py [<file_path>] [--dimacs] [--show-clues] [--show-stats]")

    # Run main function
    main(file_path=file_path, 
         use_dimacs=use_dimacs, 
         show_clues=show_clues, 
         show_stats=show_stats)
    
    # Print completion message
    if use_dimacs:
        output_path = file_path.replace('.txt', '.cnf')
        print(f"\nClues generated and saved to {output_path} (DIMACS format)")
    else:
        print(f"\nClues generated and saved to {file_path}")