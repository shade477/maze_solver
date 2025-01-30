from tkinter import Tk, BOTH, Canvas
import tkinter as tk
from assets.line import Line

class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas(master=self.__root, bg='white', height=height, width=width)
        self.__canvas.pack(anchor=tk.CENTER, fill=BOTH, expand=True)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")


    def close(self):
        self.__running = False


    def draw_line(self, line: Line, fill_color='black'):
        line.draw(self.__canvas, fill_color)