import os

def get_paths_and_files(directory):
    paths_and_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Join the root and file to get the full path
            full_path = os.path.join(root, file)
            paths_and_files.append(full_path)

    return paths_and_files

def save_to_file(directory, paths_and_files):
    output_file = os.path.join(directory, 'paths_and_files.txt')
    with open(output_file, 'w') as f:
        for path in paths_and_files:
            f.write(path + '\n')

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python get_paths_and_files.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        sys.exit(1)

    paths_and_files = get_paths_and_files(directory)
    save_to_file(directory, paths_and_files)
    print(f"Paths and files have been saved to {os.path.join(directory, 'paths_and_files.txt')}")
