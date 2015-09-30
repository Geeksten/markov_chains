import random
import sys

def open_and_read_file(file_path1, file_path2):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus_text1 = open(file_path1).read().replace("\n", " ")
    corpus_text2 = open(file_path2).read().replace("\n", " ")

    corpus = corpus_text1 + corpus_text2
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
    
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    n = 3
    link = random.choice(chains.keys())
    text = ""
    # add the first link to the master string "text"
    for word in link:
            text = text + " " + word

    # As long as the (current) key is within the dictionary: 
    counter = 0
    while counter < 40:
        # Add the value of that key to the master string 
        next_word = random.choice(chains[link])
        text = text + " " + next_word

        # Set link to a new value
        # From the old link, starting at the second element, add everything 
        # to an empty list call new_link
        # Add next-word as the last element of our new_link
        # Turn the list into a tuple
        new_link = []
        for i in range(1,n):
            new_link.append(link[i])
        new_link.append(next_word)
        link = tuple(new_link)
        counter += 1

    print text    
    return text


        # Set link to link[2], dictionary[link]

#corpus = open_and_read_file("gettysburg.txt")
corpus = open_and_read_file("childpoems.txt", "dickinson.txt")
chains = make_chains(corpus)
make_text(chains)

