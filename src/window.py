from tkinter import Tk, BOTH, Canvas
from tkinter import ttk
from gtts import gTTS
import pygame
from io import BytesIO
import os
from word import *
from word_lists import *

pygame.init()
pygame.mixer.init()

class CreateWindow:
    def __init__(self, width, height, game_list = None):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title('Window')

        self.__root.geometry(f'{width}x{height}')

        self.canvas = Canvas(self.__root, width=width, height=height, bg='white')
        self.canvas.pack()

        self.running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self.i = 80
        self.game_list = game_list
        self.solution_viewed = False

        if game_list is None:
            ttk.Label(self.canvas, text = 'No words available', font = ('arial', 50)).pack()

        else:
            self.missing_sound_label = ttk.Label(self.canvas, text= self.game_list[self.i].missing_sound, font = ("arial", 50))
            self.missing_sound_label.pack(pady= 200, padx = 200, )
            self.solution_label = ttk.Label(self.canvas, text = self.game_list[self.i].word)

            ttk.Button(self.canvas, text='quit', command=self.close).pack(side = 'bottom')
            ttk.Button(self.canvas, text='Next', command=lambda: self.update_label()).pack(side= 'bottom')
            ttk.Button(self.canvas, text='speak', command =lambda: self.speak()).pack()
            ttk.Button(self.canvas, text='solution', command = lambda: self.solution()).pack(side = 'top')



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
        if self.i < len(self.game_list):
            self.i += 1
            self.missing_sound_label['text'] = self.game_list[self.i].missing_sound
        else:
            self.i = 0
            self.missing_sound_label['text'] = self.game_list[self.i].missing_sound
        self.solution_label['text'] = self.game_list[self.i].word
        self.solution_label.pack_forget()

    def speak(self):
        mp3_fo = BytesIO()
        spoken_word = self.speak_word()
        tts = gTTS(spoken_word, lang='en')
        tts.write_to_fp(mp3_fo)
        mp3_fo.seek(0)
        sound = pygame.mixer.Sound(mp3_fo)
        sound.play()


    def speak_word(self):
        spoken_word = self.game_list[self.i].word
        return spoken_word

    def solution(self):
        self.solution_label.pack()

