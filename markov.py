import random


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus = open(file_path).read().replace("\n", " ")

    return corpus




def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    # 
    words = text_string.split()

    chains = {}

    for i in range(len(words)-2):
        bigram = words[i], words[i+1]

        if bigram not in chains:
            chains[bigram] = [words[i+2]]
        else:
            chains[bigram].append(words[i+2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    link = random.choice(chains.keys())
    text = ""
    while link in chains:

        # Add the words to the string
        for word in link:
            text = text + " " + word
        next_word = random.choice(chains[link])
        text = text + " " + next_word

        # Set link to a new value
        link = (link[1], next_word)


    print text

    return text


        # Set link to link[2], dictionary[link]

corpus = open_and_read_file("green-eggs.txt")
chains = make_chains(corpus)
make_text(chains)

# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
