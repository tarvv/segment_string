# segment_string
segment_string.py was built for a class project. 

Takes input string of characters and outputs the most probable list of segmentations from the input using the Viterbi algorithm

Corpus taken from Google's research found <a href="https://ai.googleblog.com/2006/08/all-our-n-gram-are-belong-to-you.html"> HERE </a>

viterbi_segment is taken (with my own changes made) from AIMA python github found <a href="https://github.com/aimacode/aima-python/blob/master/text.py"> HERE </a>

The following changes:

-variable name changes<br>
-probability is called from a function instead of sent via a parameter<br>
-prints the segments instead of returning<br>
