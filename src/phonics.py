from cmath import phase
from random import *


year_3_4_words = ['accidentally', 'accident',
'actually', 'actual',
'address',
'answer',
'appear',
'arrive',
'believe',
'bicycle',
'breath',
'breathe',
'build',
'busy','business',
'calendar',
'caught',
'centre',
'century',
'certain',
'circle',
'complete',
'consider',
'continue',
'decide',
'describe',
'different',
'difficult',
'disappear',
'early',
'earth',
'eight', 'eighth',
'enough',
'exercise',
'experience',
'experiment',
'extreme',
'famous',
'favourite',
'February',
'forward',
'fruit',
'grammar',
'group',
'guard',
'guide',
'heard',
'heart',
'height',
'history',
'imagine',
'increase',
'important',
'interest',
'island',
'knowledge',
'learn',
'length',
'library',
'material',
'medicine',
'mention',
'minute',
'natural',
'naughty',
'notice',
'occasion', 'occassionally',
'often',
'opposite',
'ordinary',
'particular',
'peculiar',
'perhaps',
'popular',
'position',
'possess', 'possession',
'possible',
'potatoes',
'pressure',
'probably',
'promise',
'purpose',
'quarter',
'question',
'recent',
'regular',
'reign',
'remember',
'sentence',
'separate',
'special',
'straight',
'strange',
'strength',
'suppose',
'surprise',
'therefore',
'though', 'although',
'thought',
'through',
'various',
'weight',
'woman', 'women']

phase_2 = ['i', 'e', 'i', 'o', 'u', 'c', 'ff', 'l', 'll', 'ss']

phase_3 = ['ss', 'pp', 'j', 'v', 'w', 'x', 'y', 'z', 'zz', 'qu', 'ch', 'sh', 'th', 'ng', 'ai', 'ee', 'igh', 'oa', 'oo', 'ar', 'or', 'ur', 'ow', 'oi', 'ear', 'air', 'ure', 'er']

phase_4 = ['ly', 'ui', 'in', 'en', 'ft', 'ion', 'ia', 'tion', 'cious', 'tious', 'cia', 'ant', 'ent', 'able', 'ably', 'ible', 'ibly', 'ing', 'ie', 'ei', 'ough']

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

    if len(missing_sound) > 1:
        i = randint(0, len(missing_sound)-1)
        game_dict[missing_sound[i]] = word
    else:
        if len(new_missing_sound) > 1:
            i = randint(0, len(new_missing_sound)-1)
            game_dict[new_missing_sound[i]] = word
        else:
            game_dict[new_missing_sound[0]] = word
    return game_list

game_list = []
game_dict = {}
for word in year_3_4_words:
    remove_sound(word, phase_5, phase_all, game_list)


print(game_dict)

for item in game_dict:
    game_list.append(item)

print(game_list)





