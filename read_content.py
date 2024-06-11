filename = "hello.txt"  # Replace with your actual file name
try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
