from tkinter import ttk
from tkinter import *
from gtts import gTTS
import os
from phonics import *
from window import *
from word import *
import random


game_list = []
for word in test_list:
    game_list.append(Word(word))

random.shuffle(game_list)

win = CreateWindow(game_list)

win.wait_for_close()




