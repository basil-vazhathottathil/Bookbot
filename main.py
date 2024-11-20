import os

file_path = input('Enter the file path: ')

try:
    with open(file_path) as f:
        file_contents = f.read()

    words = file_contents.split()
    word_count = len(words)

    lower_cased = file_contents.lower()

    char_dict = {}
    for char in lower_cased:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    sorted_char = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

    file_name = os.path.basename(file_path)


    print(f'--- Begin report of {file_name} ---')
    print(f'The number of words in the file: {word_count}\n')

    for char, count in sorted_char:
        print(f"'{char}' appears {count} times")

    print('\n--- End report ---')

except FileNotFoundError:
    print('File not found')