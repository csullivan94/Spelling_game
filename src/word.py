

phase_2 = ['i', 'e', 'o', 'u', 'c', 'ff', 'l', 'll', 'ss', 'pp', 'j', 'v', 'w', 'x', 'y', 'z', 'zz', 'qu', ]

phase_3 = ['ch', 'sh', 'th', 'ng', 'ai', 'ee', 'igh', 'oa', 'oo', 'ar', 'or', 'ur', 'ow', 'oi', 'ear', 'air', 'ure', 'er']

phase_4 = ['ly', 'ui', 'in', 'en', 'ft', 'ion', 'ia', 'tion', 'cious', 'tious', 'cia', 'ant', 'ent', 'able', 'ably', 'ible', 'ibly', 'ing', 'ie', 'ei', 'ough']

phonics_5 = ['ion', 'ia', 'tion', 'ous', 'tious', 'cia', 'ant', 'ent', 'able', 'ably', 'ible', 'ibly', 'ing', 'ie', 'ei', 'ough', 'ay', 'ou', 'ie', 'ea', 'oy', 'ir', 'ue', 'aw', 'wh', 'ph', 'ew', 'oe', 'au', 'ence', 'ance', 'ment', 'mant', ]



class Word:
    def __init__(self, word):
        self.word = word
        self.split = self.partition_word()[0]
        self.missing_sound = self.missing_sounds()
        self.correct = 0


    def missing_sounds(self):
        missing_sound = self.split[0] + '_'+ self.split[2]
        return missing_sound

    def partition_word(self):
        partitioned_words = []
        for sound in phonics_5:
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

    def __repr__(self):
        return f'word: {self.word}\n split: {self.split}\n correct: {self.correct}\n'



