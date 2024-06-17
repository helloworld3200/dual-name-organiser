import os
import shutil
import sys

def main():
    if len(sys.argv) < 2:
        print("Error: No path provided")
        print("Usage: python organise.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    os.chdir(path)
    filenames = [f for f in os.listdir() if os.path.isfile(f)]

    filenames_count = len(filenames)
    str_filenames_count = str(filenames_count)
    print(f"Using path: {path} with {str_filenames_count} files")

    iteration = 0
    for filename in filenames:
        print(f"Starting iteration {iteration} for {filename}")
        # Split path into filename and extension
        split_path = os.path.splitext(filename)
        # Seperate filename by spaces
        split_filename = split_path[0].split()

        # Get all parts of the filename except for number and join into string
        # with spaces as the seperator
        prefix = " ".join(split_filename[:-1])
        # Get number of filename
        num = split_filename[-1]
        extension = split_path[1]
        print(f"Prefix: {prefix}, Num: {num}, Extension: {extension}")

        if not os.path.exists(prefix):
            os.mkdir(prefix)
            print(f"Created directory: {prefix}")

        new_file_path = prefix + "/" + num + extension
        shutil.move(filename, new_file_path)
        print(f"Moved to {new_file_path}")
        
        #final_file_path = prefix + "/" + num + extension
        #os.rename(new_file_path, final_file_path)
        #print(f"Renamed to {final_file_path}")

        iteration += 1
        print(f"Iteration {iteration} completed")

if __name__ == "__main__":
    main()
