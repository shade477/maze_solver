from Window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    l1 = Line(Point(525,325), Point(300,200))
    win.draw_line(l1, 'black')
    win.wait_for_close()

if __name__ == '__main__':
    main()