from Window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(1, 51, 1, 51, win)
    cell2 = Cell(1,51, 51, 101, win)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)
    win.wait_for_close()

if __name__ == '__main__':
    main()