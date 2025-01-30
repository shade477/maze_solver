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
        win,
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
        x = self._x1 + (i + 1) * self._cell_size_x
        y = self._y1 + (j + 1) * self._cell_size_y

        # Change if num rows and cols mismatch
        cell = self._cells[i][j]
        cell.draw(x, y, x + self._cell_size_x, y + self._cell_size_y)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)