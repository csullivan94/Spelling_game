from cmath import phase
from random import *

from babel.util import missing

phase_2 = ['ff', 'l', 'll', 'ss']

phase_3 = ['j', 'v', 'w', 'x', 'y', 'z', 'zz', 'qu', 'ch', 'sh', 'th', 'ng', 'ai', 'ee', 'igh', 'oa', 'oo', 'ar', 'or', 'ur', 'ow', 'oi', 'ear', 'air', 'ure', 'er']

phase_4 = ['ly', 'ion', 'ia', 'tion', 'cious', 'tious', 'cia', 'ant', 'ent', 'able', 'ably', 'ible', 'ibly', 'ing', 'ie', 'ei', 'ough']

phase_5 = ['ion', 'ia', 'tion', 'ous', 'tious', 'cia', 'ant', 'ent', 'able', 'ably', 'ible', 'ibly', 'ing', 'ie', 'ei', 'ough', 'ay', 'ou', 'ie', 'ea', 'oy', 'ir', 'ue', 'aw', 'wh', 'ph', 'ew', 'oe', 'au']

phase_all = []
phase_all.extend(phase_2)
phase_all.extend(phase_3)
phase_all.extend(phase_4)
phase_all.extend(phase_5)
def remove_sound(word, phase_list1, phase_list2, game_list):
    missing_sound = []
    new_missing_sound = []
    for sound in phase_list1:
        if sound in word:
            missing_sound.append(word.replace(sound, '_'))
        else:
            for sound in phase_list2:
                if sound in word:
                    new_missing_sound.append(word.replace(sound, '_'))
    if len(missing_sound) > 0:
        i = randint(0, len(missing_sound)-1)
        game_list.append(missing_sound[i])
    else:
        i = randint(0, len(new_missing_sound))
        game_list.append(new_missing_sound[i])

    return game_list

word_list = ['emotionally', 'musically', 'happily', 'carefully', 'specially']
game_list = []
for word in word_list:
    remove_sound(word, phase_5, phase_all, game_list)


print(game_list)




