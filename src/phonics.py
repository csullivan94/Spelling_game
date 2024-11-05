from cmath import phase
from random import *
from word_lists import *


phase_2 = ['i', 'e', 'i', 'o', 'u', 'c', 'ff', 'l', 'll', 'ss']

phase_3 = ['ss', 'pp', 'j', 'v', 'w', 'x', 'y', 'z', 'zz', 'qu', 'ch', 'sh', 'th', 'ng', 'ai', 'ee', 'igh', 'oa', 'oo', 'ar', 'or', 'ur', 'ow', 'oi', 'ear', 'air', 'ure', 'er']

phase_4 = ['ly', 'ui', 'in', 'en', 'ft', 'ion', 'ia', 'tion', 'cious', 'tious', 'cia', 'ant', 'ent', 'able', 'ably', 'ible', 'ibly', 'ing', 'ie', 'ei', 'ough']

phase_5 = ['ion', 'ia', 'tion', 'ous', 'tious', 'cia', 'ant', 'ent', 'able', 'ably', 'ible', 'ibly', 'ing', 'ie', 'ei', 'ough', 'ay', 'ou', 'ie', 'ea', 'oy', 'ir', 'ue', 'aw', 'wh', 'ph', 'ew', 'oe', 'au', 'ence', 'ance', 'ment', 'mant', ]

phase_all = []
phase_all.extend(phase_2)
phase_all.extend(phase_3)
phase_all.extend(phase_4)
phase_all.extend(phase_5)


def split_word(word):
    partitioned_word = []
    for sound in phase_5:
        if sound in word:
            partitioned_word.append(word.partition(sound))
    for sound in phase_3:
        if sound in word:
            partitioned_word.append(word.partition(sound))
    for sound in phase_2:
        if sound in word:
            partitioned_word.append(word.partition(sound))

    return partitioned_word



