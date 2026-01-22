import sys
import re
from pathlib import Path


def read_variable_mapping(mapping_file: str) -> dict[str, str]:
    """Reads a file with variables and creates a name->number mapping."""
    with open(mapping_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Each line is a variable, line number is its ordinal number (starting from 1)
    var_to_num = {}
    num_to_var = {}
    
    for idx, line in enumerate(lines, start=1):
        var_name = line.strip()
        if var_name:  # Skip empty lines
            var_to_num[var_name] = str(idx)
            num_to_var[str(idx)] = var_name
    
    return var_to_num, num_to_var


def encode_file(input_file: str, output_file: str, var_to_num: dict[str, str]):
    """Replaces variable names with their ordinal numbers."""
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Sort by name length (longest to shortest) to avoid partial replacements
    sorted_vars = sorted(var_to_num.items(), key=lambda x: len(x[0]), reverse=True)
    
    for var_name, var_num in sorted_vars:
        # Use word boundary for exact replacement (whole words only)
        pattern = r'\b' + re.escape(var_name) + r'\b'
        content = re.sub(pattern, var_num, content)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Encoded: {input_file} -> {output_file}")
    print(f"Replaced {len(sorted_vars)} variables with their numbers")


def decode_file(input_file: str, output_file: str, num_to_var: dict[str, str]):
    """Replaces ordinal numbers with variable names."""
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Sort by number length (longest to shortest)
    sorted_nums = sorted(num_to_var.items(), key=lambda x: len(x[0]), reverse=True)
    
    for var_num, var_name in sorted_nums:
        # Use word boundary for exact replacement (whole numbers only)
        pattern = r'\b' + re.escape(var_num) + r'\b'
        content = re.sub(pattern, var_name, content)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Decoded: {input_file} -> {output_file}")
    print(f"Replaced {len(sorted_nums)} numbers with their variable names")


def main():
    if len(sys.argv) != 5:
        print("Usage: python variable_mapper.py <mapping_file> <input_file> <mode> <output_file>")
        print("  mapping_file: file with variables (each line is a variable)")
        print("  input_file: file to process")
        print("  mode: 'encode' (name->number) or 'decode' (number->name)")
        print("  output_file: new file with results")
        print()
        print("Example:")
        print("  python variable_mapper.py variables.txt data.txt encode data_encoded.txt")
        print("  python variable_mapper.py variables.txt data_encoded.txt decode data_decoded.txt")
        sys.exit(1)
    
    mapping_file = sys.argv[1]
    input_file = sys.argv[2]
    mode = sys.argv[3].lower()
    output_file = sys.argv[4]
    
    # Check file existence
    if not Path(mapping_file).exists():
        print(f"Error: Mapping file '{mapping_file}' not found")
        sys.exit(1)
    
    if not Path(input_file).exists():
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    # Read mapping
    var_to_num, num_to_var = read_variable_mapping(mapping_file)
    print(f"Loaded {len(var_to_num)} variables from {mapping_file}")
    print()
    
    # Perform encoding or decoding
    if mode == 'encode':
        encode_file(input_file, output_file, var_to_num)
    elif mode == 'decode':
        decode_file(input_file, output_file, num_to_var)
    else:
        print(f"Error: Invalid mode '{mode}'. Use 'encode' or 'decode'")
        sys.exit(1)


if __name__ == "__main__":
    main()
