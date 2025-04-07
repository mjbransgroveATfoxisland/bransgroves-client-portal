import os

# Get path where the script/executable is located
root_dir = os.path.abspath(os.path.dirname(__file__))
output_file = os.path.join(root_dir, "project_structure.txt")

def walk_directory(path, prefix=""):
    lines = []
    try:
        items = sorted(os.listdir(path), key=str.lower)
        for index, name in enumerate(items):
            full_path = os.path.join(path, name)
            connector = "├── " if index < len(items) - 1 else "└── "
            lines.append(prefix + connector + name)
            if os.path.isdir(full_path):
                extension = "│   " if index < len(items) - 1 else "    "
                lines.extend(walk_directory(full_path, prefix + extension))
    except Exception as e:
        lines.append(prefix + f"[Error reading directory: {e}]")
    return lines

if __name__ == "__main__":
    try:
        structure_lines = [os.path.basename(root_dir) + "/"]
        structure_lines += walk_directory(root_dir)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(structure_lines))

        print(f"File structure written to: {output_file}")
        os.startfile(output_file)  # Open in Notepad or default .txt editor

    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")
