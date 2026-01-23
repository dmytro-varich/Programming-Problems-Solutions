"""Script to remove duplicate lines from a text file."""
import sys


def remove_duplicate_lines(file_path: str) -> str:
    """Removes duplicate lines from a file."""
    with open(file_path, 'r') as file:
        lines: list[str] = file.readlines()
    
    seen = set()
    unique_lines = []
    
    for line in lines:
        normalized = line.strip()
        if normalized not in seen:
            seen.add(normalized)
            unique_lines.append(line)
    
    with open(file_path, 'w') as file:
        file.writelines(unique_lines)
        
    stats_text = f"Original line count: {len(lines)}\n"
    stats_text += f"Unique line count: {len(unique_lines)}\n"    
    return stats_text
        
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicates.py <file_path>")
    else:
        stats = remove_duplicate_lines(sys.argv[1])
        print(f"Duplicate lines removed from {sys.argv[1]}")
        print(stats)