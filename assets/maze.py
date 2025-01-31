from assets.cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        
    
    def _create_cells(self):
        
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for c in range(self._num_cols):
            for r in range(self._num_rows):
                self._draw_cell(c, r)


    def _draw_cell(self, i, j):
        x = self._x1 + (i) * self._cell_size_x
        y = self._y1 + (j) * self._cell_size_y

        # Change if num rows and cols mismatch
        cell = self._cells[i][j]
        cell.draw(x, y, x + self._cell_size_x, y + self._cell_size_y)
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)

    def __eq__(self, maze):
        return (self._x1 == maze._x1 and
        self._y1 == maze._y1 and
        self._num_rows == maze._num_rows and
        self._num_cols == maze._num_cols and
        self._cell_size_x == maze._cell_size_x and
        self.cell_size_y == maze.cell_size_y and
        self._win == maze._win)

