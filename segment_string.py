"""segment_string.py is built for a class project
    Takes input string of characters and outputs the most probable list of segmentation from the input using the
    Viterbi algorithm"""

import io

"""viterbi_segment is taken from AIMA python github found here: https://github.com/aimacode/aima-python/blob/master/text.py"""


def viterbi_segment(text):
    """Find and print the best segmentation of the input string of characters, given the probability from google's data.
        Changes from the original include:
            -variable name changes
            -probability is called from a function instead of sent via a parameter
            -prints the segments instead of returning."""
    n = len(text)
    words = [''] + list(text)
    best = [1.0] + [0.0] * n

    for i in range(n + 1):
        for j in range(0, i):
            word_segment = text[j:i]
            curr_score = word_prob(word_segment) * best[i - len(word_segment)]
            if curr_score >= best[i]:
                best[i] = curr_score
                words[i] = word_segment

    sequence = []
    i = len(words) - 1
    while i > 0:
        sequence[0:0] = [words[i]]
        i = i - len(words[i])

    print(sequence)
    return


def word_prob(word_segment):
    """word_prob returns the probability of a word existing based on input data create_dict. Returns 0 if word not in dict
        parameter word_segment: segmentation of input text"""
    if word_segment in dictionary:
        return dictionary[word_segment] / total_count
    else:
        return 0


def create_dict(filename):
    """create_dict reads file and creates dictionary {word : word count}
        parameter filename: name of file to be read"""
    with io.open(filename, encoding='utf-8') as reader:
        lines = (line.split('\t') for line in reader)
        return dict((dict_word.lower(), float(word_count)) for dict_word, word_count in lines)


"""calls dictionary funciton with the name of file containing a subset of google's data found here as a text file: 
    https://github.com/grantjenks/python-wordsegment as words.txt
    google data info found here: https://ai.googleblog.com/2006/08/all-our-n-gram-are-belong-to-you.html
    data consists of one column of most common words and the next column is the word's count from scanned texts"""
dictionary = create_dict("Word Counts.txt")

# adds counts of all words
total_count = sum(dictionary.values())

# calls verterbi_segment, sending the user's input
viterbi_segment(input("Enter text without spaces: "))
