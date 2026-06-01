import os
import sys
from stat import filemode


def display_files_info(folder):
    if not os.path.isdir(folder):
        print(f"Invalid directory: {folder}")
        return

    absolute_folder = os.path.realpath(folder)

    print("\n" + "-" * 65)
    print(f"Directory report for: {absolute_folder}")
    print("-" * 65)
    print(f"{'Name':<32} {'Bytes':<12} {'Mode':<12}")
    print("-" * 65)

    try:
        entries = os.scandir(folder)

        found_file = False

        for entry in entries:
            if entry.is_file():
                found_file = True

                details = entry.stat()
                size = details.st_size
                permissions = filemode(details.st_mode)

                print(f"{entry.name:<32} {size:<12} {permissions:<12}")

        if not found_file:
            print("No regular files were found in this directory.")

    except PermissionError:
        print("Access refused: you do not have permission to open this directory.")
    except OSError as error:
        print(f"System error while reading the directory: {error}")

    print("-" * 65)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        directory_to_check = sys.argv[1]
    else:
        directory_to_check = input("Directory to inspect [.]: ").strip() or "."

    display_files_info(directory_to_check)