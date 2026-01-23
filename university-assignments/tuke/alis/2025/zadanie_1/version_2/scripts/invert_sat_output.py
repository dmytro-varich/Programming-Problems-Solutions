"""
Inverts SAT solver output by negating all literals.
Converts positive literals to negative and vice versa.

Valid SAT-Solver Output Format Example (input_file):
    s SATISFIABLE
    v -1 2 -3 -4 5 -6 -7 -8 -9 -10 11 -12 -13 -14 -15 16 -17 18 -19 -20 -21 -22 -23 
    v 24 -25 -26 27 -28 29 -30 -31 -32 -33 -34 35 -36 -37 -38 -39 40 -41 42 -43 -44 
    v 45 -46 -47 -48 -49 -50 51 -52 -53 -54 -55 56 -57 58 -59 -60 61 -62 -63 -64 0
"""
import sys


def invert_sat_output(input_file: str, output_file: str | None = None) -> None:
    """
    Inverts the SAT solver output by negating all literals.
    
    Args:
        input_file: Path to the input file with SAT solver output
        output_file: Path to the output file (defaults to input_file if not provided)
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove SAT solver metadata
    content = content.replace('s', '').replace('SATISFIABLE', '').replace('v', '').strip()
    
    # Process literals
    literals = content.split()
    inverted = []
    
    for literal in literals:
        if literal == '0':
            continue
        
        if literal.startswith('-'):
            inverted.append(literal[1:])
        else:
            inverted.append('-' + literal)
    
    # Write inverted output
    output_path = output_file if output_file else input_file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(' '.join(inverted) + ' 0')


def main():
    if len(sys.argv) not in [2, 3]:
        print("Usage: python invert_sat_output.py <input_file> [<output_file>]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else None
    
    invert_sat_output(input_file, output_file)
    print(f"Inverted SAT output saved to {output_file if output_file else input_file}")


if __name__ == "__main__":
    main()
