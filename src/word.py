
from word_lists import *
from phonics import *

class Word:
    def __init__(self, word):
        self.word = word
        self.split = split_word(word)[1]
        self.missing_sound = self.missing_sounds()

    def missing_sounds(self):
        missing_sound = self.split[0] + '_'+ self.split[2]
        return missing_sound

