from tkinter import ttk
from tkinter import *
from gtts import gTTS
import os
from phonics import *
from window import *
from word import *
import random

def creating_game_list(word_list, game_list):
    i = 0
    while i < 10:
        j = random.randrange(0, len(word_list))
        game_list.append(Word(word_list[j]))
        i+=1
    return game_list

game_list = []
creating_game_list(year_5_6_words, game_list)

random.shuffle(game_list)

win = CreateWindow(game_list)

win.wait_for_close()




