"""
A simple SAT solver interface using the pycryptosat library.

Requirements: 
    - pycryptosat>=5.11.21
"""
import sys
from typing import List, Optional
from pycryptosat import Solver


def read_dimacs_file(file_path: str) -> List[List[int]]:
    """
    Reads a DIMACS CNF file and returns the number of variables and clauses.
    
    Args:
        file_path (str): Path to the DIMACS CNF file.  
    
    Returns:
        List[List[int]]: A list of clauses, where each clause is a list of integers.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            clauses = []
            for line in file:
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('c'):
                    continue
                
                # Skip problem line (p cnf num_vars num_clauses)
                if line.startswith('p cnf'):
                    continue
                
                # Parse clause: "1 -2 3 0" -> [1, -2, 3]
                try:
                    clause = list(map(int, line.split()))
                    # Remove trailing 0
                    if clause and clause[-1] == 0:
                        clause = clause[:-1]
                    if clause:  # Only add non-empty clauses
                        clauses.append(clause)
                except ValueError:
                    print(f"Warning: Skipping invalid line: {line}")
                    continue
            
            return clauses
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    
def output_format(assignment: List[bool]) -> str:
    """
    Formats the assignment list into a string representation.
    
    Args:
        assignment (List[bool]): The satisfying assignment.
    
    Returns:
        str: Formatted string of the assignment.
    """
    result = []
    for idx, val in enumerate(assignment):
        if idx == 0 and not val:
            continue  # Skip variable 0, because it 'None' in pycryptosat
        if val:
            result.append(str(idx))
        else:
            result.append(str(-idx))
    return ' '.join(result)


def write_sat_result(file_path: str, is_satisfiable: bool, assignment: List[bool]):
    """
    Writes the SAT solver result to a file in DIMACS format.
    
    Args:
        file_path (str): Path to the output file.
        is_satisfiable (bool): Whether the formula is satisfiable.
        assignment (List[bool]): The satisfying assignment if satisfiable.
    """
    with open(file_path, 'w') as file:
        if is_satisfiable:
            file.write("s SATISFIABLE\n")
            file.write("v " + output_format(assignment) + " 0\n")
        else:
            file.write("s UNSATISFIABLE\n")
                

def solve_cnf(clauses: List[List[int]]) -> (bool, List[bool]):
    """
    Solves the CNF formula using a SAT solver.
    
    Args:
        clauses (List[List[int]]): A list of clauses, where each clause is a list of integers.
    
    Returns:
        (bool, List[bool]): A tuple where the first element indicates if the formula is satisfiable,
                           and the second element is the satisfying assignment if it is satisfiable.
    """
    solver = Solver()
    
    for clause in clauses:
        solver.add_clause(clause)
    
    is_satisfiable, solution = solver.solve()
    
    if is_satisfiable:
        return True, solution
    else:
        return False, []
    

def main(input_file: str, output_file: str = None):
    """
    Main function to read a DIMACS CNF file, solve it using a SAT solver, and print the result.
    
    Args:
        input_file (str): Path to the DIMACS CNF file.
        output_file (str): Path to the output file.
    """
    clauses = read_dimacs_file(input_file)
    is_satisfiable, assignment = solve_cnf(clauses)
    print("SATISFIABLE" if is_satisfiable else "UNSATISFIABLE")
    if is_satisfiable:
        print("Assignment:", output_format(assignment) + " 0") 
    if output_file:
        write_sat_result(output_file, is_satisfiable, assignment)
    
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sat_solver.py <path_to_dimacs_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file=input_file, output_file=output_file)
        print("SAT Solver finished execution.")