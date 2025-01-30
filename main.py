from Window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(50,100, 50, 100, win)
    cell.draw()
    win.wait_for_close()

if __name__ == '__main__':
    main()