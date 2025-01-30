
from line import Line
from point import Point


class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        lines = {
            'top': Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
            'left': Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
            'right': Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
            'bottom': Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
        }
        
        if self.has_top_wall:
            self._win.draw_line(lines['top'])

        if self.has_left_wall:
            self._win.draw_line(lines['left'])

        if self.has_bottom_wall:
            self._win.draw_line(lines['bottom'])

        if self.has_right_wall:
            self._win.draw_line(lines['right'])