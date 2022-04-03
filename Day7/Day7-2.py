def is_palindrome(text):
    text = text.replace(" ", "").lower()
    reversed_text = text[::-1]
    return text == reversed_text

text = input("Write some sentence to know whether it's read equally from both sides: ")
print(is_palindrome(text))