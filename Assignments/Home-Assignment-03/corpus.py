import re
import os

folders = os.listdir("content")

print(folders)


def count_word_frequency(file_path):
    print(f"Statistics for file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()


        text = re.sub(r'[^\w\s\u0600-\u06FF]', '', text)
        words = text.split()

        total_tokens = len(words)

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        total_types = len(word_count)


        print(f"{'Word':<30} {'Frequency':<10}\n")
        print('-' * 50 + '\n')
        for word, count in word_count.items():
            print(f"{word:<30} {count:<10}\n")
        print(f"Total Tokens (all words): {total_tokens}\n")
        print(f"Total Types (unique words): {total_types}\n")
        print("\n\n\n")


    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# # Run the function
for file in folders:
    count_word_frequency(f"content/{file}")
