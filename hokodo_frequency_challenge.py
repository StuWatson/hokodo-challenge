def get_word_frequencies(text):

    # Split gives us a list of the individual words
    words = text.split()

    # Sets consist of unique items, by constructing a set from the list, we filter out duplicates
    unique_words = set(words)

    # The requirements specify that the output should be alphanumeric order, sorted() handles this out of the box
    sorted_words = sorted(unique_words)

    # Now we can iterate our set and print how many times each unique word appears in our original list of words
    for word in sorted_words:
        print(f'{word}:{words.count(word)}')


user_input = input('Enter an input string: ')

get_word_frequencies(user_input)
