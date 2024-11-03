from tkinter import Tk, BOTH, Canvas
from tkinter import ttk
from phonics import *
from gtts import gTTS
import pygame
from io import BytesIO
import os

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


        self.label = ttk.Label(self.canvas, text=game_list[0], font = ("arial", 50))
        self.label.pack(pady= 200, padx = 200, )
        ttk.Button(self.canvas, text='quit', command=self.close).pack(side = 'bottom')
        ttk.Button(self.canvas, text='Next', command=lambda: self.update_label()).pack(side= 'bottom')
        ttk.Button(self.canvas, text='speak', command =lambda: self.speak()).pack()
        self.speak_word()
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

        i = game_list.index(self.label['text'])
        if i < len(game_list)-1:
            self.label['text'] = game_list[i+1]
        else:
            self.label['text'] = game_list[0]

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
        word = self.label['text']
        spoken_word = game_dict[word]
        return spoken_word
