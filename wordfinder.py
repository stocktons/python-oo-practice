from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """Accepts a file path that contains random words, one word per line,
        and returns a string of how many words are on the file """

        file = open(file_path)
        self.word_list = self.read_file(file) # self goes to whichever instance is currently active
        print(f'{len(self.word_list)} words read')

    def read_file(self, file): #consider renaming to be get_words
        """Read file path, open the file, return a list of words in that file."""
        
        return list(file.read().split('\n')) # return file.readlines()


class RandomWordFinder(WordFinder):
    """Finds random words in the list"""

    def __init__(self, file_path): # don't need this, just delete it because it's the same
        super().__init__(file_path)

    def random(self):
        """Returns a random word from the list"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Filters out lines that begin with # and blank lines"""

    def __init__(self, file_path): # delete this
        super().__init__(file_path)

    def read_file(self, file): #consider renaming to be get_words
        """Read file path, open the file, filter out lines that begin with # and blank lines, and return a list of words in that file."""

        file_list = list(file.read().split('\n')) # is this actually a list of files? Nope. Call it "lines" -- also use .readlines()
        print(f"this is line 42 {[word for word in file_list if not word.startswith('#') and len(word) != 0]}") #looking for truthiness or falsiness
        # filter startswith # and empty strings  -- 
        return [word for word in file_list if not word.startswith('#') and word != '']




sw = SpecialWordFinder("/Users/Sarah/Desktop/python-oo-practice/test.txt")





    


# wp = WordFinder("/Users/zacharythomas/Desktop/words.txt")


# wf = WordFinder('/usr/share/dict/words')

# print(wf.random())

# print(wf.random())

# print(wf.random())
