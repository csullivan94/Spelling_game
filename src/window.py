from tkinter import Tk, BOTH, Canvas
from tkinter import ttk
from phonics import *


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


        self.label = ttk.Label(self.canvas, text=game_list[0])
        self.label.pack()
        ttk.Button(self.canvas, text='quit', command=self.close).pack(side = 'bottom')
        ttk.Button(self.canvas, text='Next', command=lambda: self.update_label()).pack(side= 'bottom')
        ttk.Button(self.canvas)

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
