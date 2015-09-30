import random
import sys

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
    n = 3

    for i in range(len(words)-n):
        ngram = []
        j = i
        while len(ngram) < n:
            ngram.append(words[j])
            j += 1
        ngram = tuple(ngram)

        if ngram not in chains:
            chains[ngram] = [words[i+n]]
        else:
            chains[ngram].append(words[i+n])
    
    print chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    link = random.choice(chains.keys())
    text = ""
    # add the first link to the master string "text"
    for word in link:
            text = text + " " + word

    # As long as the (current) key is within the dictionary: 
    while link in chains:

        # Add the value of that key to the master string 
        next_word = random.choice(chains[link])
        text = text + " " + next_word

        # Set link to a new value
        link = (link[1], next_word)

    print text

    return text


        # Set link to link[2], dictionary[link]

corpus = open_and_read_file("green-eggs.txt")
chains = make_chains(corpus)
# make_text(chains)

# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
