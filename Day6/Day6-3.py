text = input("Enter some sentence: ")
words = text.split()

reversed_word_list = [words[::-1] for words in words]
# print(reversed_word_list)
reversed_sentence = ' '.join(reversed_word_list).capitalize()

print("This was your sentence:", text)
print("This is reversed sentence:", reversed_sentence)