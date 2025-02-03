def get_unicode_of_character():
    isTrue = True
    while isTrue:
        char = input("Enter a character: ")
        if char == "exit":
            isTrue = False
            return
        unicode_value = ord(char)
        print(f"The Unicode of '{char}' is: U+{unicode_value:04X} ({unicode_value})")

if __name__ == "__main__":
    get_unicode_of_character()
