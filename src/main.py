from tkinter import ttk
from tkinter import *
from gtts import gTTS
import os
from phonics import *
from window import *
from word import *


game_list = []
for word in year_5_6_words:
    game_list.append(Word(word))

win = CreateWindow(1300, 700, game_list)

win.wait_for_close()




