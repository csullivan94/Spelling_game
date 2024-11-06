
from word_lists import *
from phonics import *

class Word:
    def __init__(self, word):
        self.word = word
        self.split = self.partition_word()[0]
        self.missing_sound = self.missing_sounds()
        self.correct = 0
        self.incorrect = 0

    def missing_sounds(self):
        missing_sound = self.split[0] + '_'+ self.split[2]
        return missing_sound

    def partition_word(self):
        partitioned_words = []
        for sound in phase_5:
            if sound in self.word:
                partitioned_words.append(self.word.partition(sound))
        if len(partitioned_words) < 1:
            for sound in phase_3:
                if sound in self.word:
                    partitioned_words.append(self.word.partition(sound))
        if len(partitioned_words) < 1:
            for sound in phase_2:
                if sound in self.word:
                    partitioned_words.append(self.word.partition(sound))
        return partitioned_words

