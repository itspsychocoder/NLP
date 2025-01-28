import re
# Sample Urdu text
file_path = "urdu-text.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    # Split the text into sentences using Urdu-specific punctuation
    urdu_text = file.read()
    # Remove non-word characters and extra whitespaces
    text = re.sub(r'[^\w\s\u0600-\u06FF]', '', urdu_text)

    sentences = text.split()
    # Remove empty strings and trim sentences
    sentences = [sentence.strip() for sentence in sentences]

    # Calculate the word count for each sentence
    word_counts = [len(sentence) for sentence in sentences]

    # Calculate the average word count
    average_word_count = sum(word_counts) / len(word_counts)


    print(f"Word counts: {word_counts}")
    print(f"Average word count: {average_word_count}")