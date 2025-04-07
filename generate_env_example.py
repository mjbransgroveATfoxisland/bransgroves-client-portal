from pathlib import Path

# Correct path to your .env file inside the /env directory
env_path = Path("env/.env")
example_path = Path(".env.example")

# Check if .env file exists
if not env_path.exists():
    print("No .env file found at env/.env.")
    exit(1)

# Read and anonymize .env contents
lines = env_path.read_text().splitlines()
example_lines = []

for line in lines:
    if not line.strip() or line.strip().startswith("#"):
        example_lines.append(line)
    elif "=" in line:
        key, _ = line.split("=", 1)
        example_lines.append(f"{key}=your-{key.lower()}-here")
    else:
        example_lines.append(line)

# Write the example file
example_path.write_text("\n".join(example_lines) + "\n")
print(f".env.example created at: {example_path.resolve()}")
