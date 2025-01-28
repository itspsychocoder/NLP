import re

class CustomTreebankTokenizer:
    def __init__(self):
        self.rules = [
          (r"n't", " n't"),  # Split contractions like "don't"
            (r"'re", " 're"),  # Split contractions like "they're"
            (r"'ve", " 've"),  # Split contractions like "I've"
            (r"'ll", " 'll"),  # Split contractions like "you'll"
            (r"'d", " 'd"),    # Split contractions like "I'd"
            (r"(?<=[a-zA-Z])(?=[,.!?])", " "),  # Separate punctuation attached to words
            (r"(\$\d+\.\d+)", r" \1 "),         # Match dollar amounts with decimals like "$3.14"
            (r"(\d+\.\d+)", r" \1 "),           # Match standalone decimals like "3.14"
            (r"(\$[0-9]+)", r" \1 "),           # Match dollar amounts without decimals like "$3"
            (r"([()\";:])", r" \1 "),           # Add spaces around specific symbols
        ]

    def tokenize(self, text):
        # Apply each rule sequentially
        for pattern, replacement in self.rules:
            text = re.sub(pattern, replacement, text)
        # Split by whitespace into tokens
        tokens = text.split()
        return tokens


# Example usage
text = "I'm learning NLP. Don't you love it? It's $3.14!"
tokenizer = CustomTreebankTokenizer()
tokens = tokenizer.tokenize(text)

print(tokens)
