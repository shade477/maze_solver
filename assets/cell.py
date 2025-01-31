from assets.line import Line
from assets.point import Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win


    def draw(self, x1, y1, x2, y2, fill='black'):
        if not self._win:
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        lines = {
            'top': Line(Point(x1, y1), Point(x2, y1)),
            'left': Line(Point(x1, y1), Point(x1, y2)),
            'right': Line(Point(x2, y1), Point(x2, y2)),
            'bottom': Line(Point(x1, y2), Point(x2, y2)),
        }
        
        if self.has_top_wall:
            self._win.draw_line(lines['top'], fill)

        if self.has_left_wall:
            self._win.draw_line(lines['left'], fill)

        if self.has_bottom_wall:
            self._win.draw_line(lines['bottom'], fill)

        if self.has_right_wall:
            self._win.draw_line(lines['right'], fill)

    
    @property
    def x1(self):
        return self._x1
    

    @property
    def x2(self):
        return self._x2
    
    
    @property
    def y1(self):
        return self._y1
    

    @property
    def y2(self):
        return self._y2
    

    @property
    def has_bottom_wall(self):
        return self.has_bottom_wall
    
    @property
    def has_top_wall(self):
        return self.has_top_wall
    

    @property
    def has_left_wall(self):
        return self.has_left_wall
    

    @property
    def has_right_wall(self):
        return self.has_right_wall
    

    @x1.setter
    def x1(self, x):
        self._x1 = x


    @x2.setter
    def x2(self, x):
        self._x2 = x


    @y1.setter
    def y1(self, y):
        self._y1 = y


    @y2.setter
    def y2(self, y):
        self._y2 = y

    
    @has_bottom_wall.setter
    def has_bottom_wall(self, value):
        self.has_bottom_wall = value

     
    @has_top_wall.setter
    def has_top_wall(self, value):
        self.has_top_wall = value

   
    @has_left_wall.setter
    def has_left_wall(self, value):
        self.has_left_wall = value


    @has_right_wall.setter
    def has_right_wall(self, value):
        self.has_right_wall = value


    def get_center(self):
        xh = abs(self._x2 - self._x1)/2
        yh = abs(self._y2 - self._y1)/2

        center = Point(self._x1 + xh, self._y1 + yh)
        return center
        

    def draw_move(self, to_cell, undo=False):
        fill = 'grey' if undo else 'red'
        line = Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line, fill)