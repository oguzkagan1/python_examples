"""Helping your sister add prefixes and suffixes to words for her four-part vocabulary assignment."""

def add_prefix_un(word):
    add_word = "un" + word
    return add_word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    for i in range(1, len(vocab_words)):
        vocab_words[i] = prefix + str(vocab_words[i])
    return " :: ".join(vocab_words)


def remove_suffix_ness(word):
    word = word.replace("ness", "")
    if word[-1] == "i":
        word = word.replace(word[-1], "y")
    return word


def adjective_to_verb(sentence, index):
    sentence = sentence.strip(".")
    list = sentence.split(" ")
    return list[index] + "en"


print("Your sister needs to create negative words by adding the prefix un, meaning not: ", add_prefix_un("happy"), "\n",
        "Students apply prefixes to word lists, creating strings with the prefix added: ", make_word_groups(['en', 'close', 'joy', 'lighten']), "\n",
        "Remove a suffix from a word:", remove_suffix_ness("heaviness"), "\n",
        "Extract and transform a word:", adjective_to_verb('I need to make that bright.', -1 ), "\n",
        "Where an adjective becomes a verb by adding an en suffix: ", adjective_to_verb('I need to make that bright.', -1))
