from tkinter import Tk, BOTH, Canvas
from tkinter import ttk
from gtts import gTTS
import pygame
from io import BytesIO
import os
from word import *
from word_lists import *
from itertools import cycle

game_list = []
for word in year_5_6_words:
    game_list.append(Word(word))

print(game_list[0].word, game_list[0].split)
print(game_list[0].missing_sound)

class CreateWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title('Window')

        self.__root.geometry(f'{width}x{height}')

        self.canvas = Canvas(self.__root, width=width, height=height, bg='white')
        self.canvas.pack()

        self.running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self.i = 0

        self.label = ttk.Label(self.canvas, text=game_list[self.i].missing_sound, font = ("arial", 50))
        self.label.pack(pady= 200, padx = 200, )
        ttk.Button(self.canvas, text='quit', command=self.close).pack(side = 'bottom')
        ttk.Button(self.canvas, text='Next', command=lambda: self.update_label()).pack(side= 'bottom')
        ttk.Button(self.canvas, text='speak', command =lambda: self.speak()).pack()



    def wait_for_close(self):
        self.running = True
        while self.running is True:
            self.redraw()

    def close(self):
        self.running = False

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def update_label(self):
        if self.i < len(game_list):
            self.i += 1
            self.label['text'] = game_list[self.i].missing_sound
        else:
            self.i = 0
            self.label['text'] = game_list[self.i].missing_sound


    pygame.init()
    pygame.mixer.init()
    def speak(self):
        mp3_fo = BytesIO()
        spoken_word = self.speak_word()
        tts = gTTS(spoken_word, lang='en')
        tts.write_to_fp(mp3_fo)
        mp3_fo.seek(0)
        sound = pygame.mixer.Sound(mp3_fo)
        sound.play()


    def speak_word(self):
        spoken_word = game_list[self.i].word
        return spoken_word
