file_path = 'eng.txt'

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        
        words = text.split()
        total_tokens = len(words)
        
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        total_types = len(word_count)

        print(f"\n{'Word':<20} {'Frequency':<10}")
        print('-' * 30)
        for word, count in word_count.items():
            print(f"{word:<20} {count:<10}")

        print("\n\n")
        print(f"Total Tokens (all words): {total_tokens}")
        print(f"Total Types (unique words): {total_types}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
count_word_frequency(file_path)
