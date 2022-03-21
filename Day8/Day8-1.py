def get_char_count(text):
    result = {}
    for i in text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


user_input =input("Enter some text for character counting: ")
character_dictionary = get_char_count(user_input)
print(user_input, "has the following character counts:",character_dictionary)
