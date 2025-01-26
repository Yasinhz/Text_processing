def analyze_file(file_path):
    try:
        file = open(file_path, 'r', encoding='utf-8')
        content = file.read()
        file.close()

        lines = content.splitlines()
        line_count = len(lines)

        words = content.split()
        word_count = len(words)

        char_count = len(content)

        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = input("Enter the file path: ")
analyze_file(file_path)