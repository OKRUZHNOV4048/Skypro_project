import random


def shuffling_letters_words_dict(dict_file_words):
    """
        The function accepts a dictionary from the global scope,
        generated from a text file using the with…as construct.
        Next, the function shuffles each value inside the dictionary
        and forms a new dictionary, where the shuffled words are the value with the same key
        as in the original dictionary.
    """
    dict_jumbled_words = {}
    for k, v in dict_file_words.items():
        v = list(v)
        random.shuffle(v)
        jumbled_word = ''.join(v)
        dict_jumbled_words[k] = jumbled_word

    return dict_jumbled_words


def random_word_assignment(dict_jumbled_words):
    """
    The function takes a dictionary of jumbled words.
    Selects one word as a value with a randomly chosen key.
    Then return this shuffled word and its index
    for later comparison with the index of the original dictionary
    with unshuffled words.
    """
    random_jumbled_word = dict_jumbled_words[random.randint(1, len(dict_jumbled_words))]
    index_random_jumbled_word = None
    for k, v in dict_jumbled_words.items():
        if v == random_jumbled_word:
            index_random_jumbled_word = k

    return [random_jumbled_word, index_random_jumbled_word]
