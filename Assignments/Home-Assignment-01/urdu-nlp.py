import re

file_path = 'urdu.txt'

def count_word_frequency(file_path):
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

        # Print results
        print(f"\n{'Word':<30} {'Frequency':<10}")
        print('-' * 50)
     
        with open("urdu-output.txt", 'w', encoding='utf-8') as out:
            out.write(f"{'Word':<30} {'Frequency':<10}\n")
            out.write('-' * 50 + '\n')
            for word, count in word_count.items():
                out.write(f"{word:<30} {count:<10}\n")

            out.write("\nStatistics:\n")
            out.write(f"Total Tokens (all words): {total_tokens}\n")
            out.write(f"Total Types (unique words): {total_types}\n")

        print(f"Results saved to {"urdu-output.txt"}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
count_word_frequency(file_path)
