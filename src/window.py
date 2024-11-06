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
    def __init__(self, game_list = None):
        self.width = 1500
        self.height = 1000
        self.__root = Tk()
        self.__root.title('Window')

        self.__root.geometry(f'{self.width}x{self.height}')

        self.canvas = Canvas(self.__root, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        self.running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self.i = 0
        self.game_list = game_list
        self.solution_viewed = False

        if game_list is None:
            ttk.Label(self.canvas, text = 'No words available', font = ('arial', 50)).pack()

        else:
            self.missing_sound_1 = ttk.Label(self.canvas, text= self.game_list[self.i].split[0], font = ("arial", 30))
            self.missing_sound_1.pack(pady= 200, side = 'left')
            self.entry = ttk.Entry(self.canvas, width = len(self.game_list[self.i].split[1])+1, font = ('arial', 30))
            self.entry.pack(side = 'left')
            self.missing_sound_2 = ttk.Label(self.canvas, text= self.game_list[self.i].split[2], font = ('arial', 30))
            self.missing_sound_2.pack(side = 'left')
            self.correct_incorrect = ttk.Label(self.canvas, text='', font = ('arial', 20))
            self.solution_label = ttk.Label(self.canvas, text = self.game_list[self.i].word)

            ttk.Button(self.canvas, text='quit', command=self.close).pack(side = 'bottom')
            ttk.Button(self.canvas, text='Next', command=lambda: self.update_label()).pack(side= 'bottom')
            ttk.Button(self.canvas, text='speak', command =lambda: self.speak()).pack()
            ttk.Button(self.canvas, text='solution', command = lambda: self.solution()).pack(side = 'bottom')
            ttk.Button(self.canvas, text='submit', command = lambda: self.submit()).pack()


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
        if self.i < len(self.game_list)-1:
            self.i += 1
            self.missing_sound_1['text'] = self.game_list[self.i].split[0]
            self.missing_sound_2['text'] = self.game_list[self.i].split[2]
        else:
            self.i = 0
            self.missing_sound_1['text'] = self.game_list[self.i].split[0]
            self.missing_sound_2['text'] = self.game_list[self.i].split[2]
        self.solution_label['text'] = self.game_list[self.i].word
        self.solution()
        self.solution_label.pack_forget()
        self.correct_incorrect.pack_forget()
        self.entry.config(state = 'normal')
        self.entry.delete(0, 'end')



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
        self.entry.config(state = 'disabled')

    def submit(self):
        if self.entry.get() == self.game_list[self.i].split[1]:
            self.correct_incorrect['text'] = 'correct'
            self.correct_incorrect.pack()
            self.game_list[self.i].correct += 1
        else:
            self.correct_incorrect['text'] = 'try again'
            self.correct_incorrect.pack()
            self.game_list[self.i].incorrect += 1

