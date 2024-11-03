from random import *


phase_2 = ['s', 'a', 't', 'p', 'i', 'n', 'm', 'd', 'g', 'o', 'c', 'k', 'ck', 'e', 'u', 'r', 'h', 'b', 'f', 'ff', 'l', 'll', 'ss']

phase_3 = ['j', 'v', 'w', 'x', 'y', 'z', 'zz', 'qu', 'ch', 'sh', 'th', 'ng', 'ai', 'ee', 'igh', 'oa', 'oo', 'ar', 'or', 'ur', 'ow', 'oi', 'ear', 'air', 'ure', 'er']

phase_4 = ['ion', 'ia', 'tion']

phase_5 = ['ay', 'ou', 'ie', 'ea', 'oy', 'ir', 'ue', 'aw', 'wh', 'ph', 'ew', 'oe', 'au']

phase_all = []
phase_all.extend(phase_2)
phase_all.extend(phase_3)
phase_all.extend(phase_4)
phase_all.extend(phase_5)
def remove_sound(word, phase_list):
    missing_sound = []
    for sound in phase_list:
        if sound in word:
            missing_sound.append(word.replace(sound, '_'))
    return missing_sound

word_list = ['emotionally', 'musically', 'happily', 'carefully', 'specially']
missing_letters = []
for word in word_list:
    missing_letters.append(remove_sound(word, phase_all))

game_list = []
for words in missing_letters:
    if len(words) > 1:
        i = randint(0, len(words)-1)
        game_list.append(words[i])

print(game_list)




