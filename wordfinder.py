from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path): 
        """ Accepts a file path that contains random words, one word per line, and reads how many words are on the file """

        self.word_list = self.read_file(file_path)
        print(f'{len(self.word_list)} words read')

        
    def read_file(self, file_path):
        file = open(file_path)
        return list(file.read().split('\n')) 

    def random(self):
        return choice(self.word_list)








    


# wp = WordFinder("/Users/zacharythomas/Desktop/words.txt")

wf = WordFinder('/usr/share/dict/words')

print(wf.random())

print(wf.random())

print(wf.random())