def count_lines(name):
    try:
        with open(name, 'r') as file:
            lines = file.readlines()
        return len(lines)
    except FileNotFoundError:
        return -1


def count_chars(name):
    try:
        with open(name, 'r') as file:
            text = file.read()
        return len(text)
    except FileNotFoundError:
        return -1


def test(name):
    line_count = count_lines(name)
    char_count = count_chars(name)

    if line_count == -1 or char_count == -1:
        print("File not found.")
    else:
        print(f"Number of lines: {line_count}")
        print(f"Number of characters: {char_count}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python mymod.py <filename>")
    else:
        filename = sys.argv[1]
        test(filename)
