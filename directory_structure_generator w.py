import os

# Set the root directory to map
root_dir = os.path.abspath(os.path.dirname(__file__))
output_file = os.path.join(root_dir, "project_structure.txt")

def walk_directory(path, prefix=""):
    lines = []
    items = sorted(os.listdir(path), key=str.lower)
    for index, name in enumerate(items):
        full_path = os.path.join(path, name)
        connector = "├── " if index < len(items) - 1 else "└── "
        lines.append(prefix + connector + name)
        if os.path.isdir(full_path):
            extension = "│   " if index < len(items) - 1 else "    "
            lines.extend(walk_directory(full_path, prefix + extension))
    return lines

if __name__ == "__main__":
    print(f"Mapping project structure for: {root_dir}")
    structure_lines = [os.path.basename(root_dir) + "/"]
    structure_lines += walk_directory(root_dir)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(structure_lines))

    print(f"File structure written to: {output_file}")
