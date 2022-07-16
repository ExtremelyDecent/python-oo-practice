"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    """ Finding random words from text file

    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    def __init__(self, path):
        """Reads word file from path and reports how many words have been read
        """
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    def parse(self,dict_file):
        """Makes a list of words from dict_file
        """
        return [w.strip() for w in dict_file]

    def random(self):
        """Returns random word
        """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    Specialized WordFinder that excludes blanks and comments

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
def parse(self, dict_file):
        """
        Parse dict_file -> list of words, skipping blanks/comments.
        """

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    
    
    
