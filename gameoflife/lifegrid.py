from arrays import Array2D

class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    dead_cell = 0
    live_cell = 1
    neighbours = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),
                  (0,1),(-1,1),(-1,0)]

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.

        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())


    def __str__(self):
        """
        Converts lifegrid to string
        :return: str
        """
        s = ""
        for i in range(self._grid.num_rows()):
            for j in range(self._grid.num_cols()):
                if self._grid[(i,j)] == LifeGrid.live_cell:
                    s += '1'
                else:
                    s += '0'

            s += '\n'
        return s


    def num_rows(self):
        """
        Returns the number of rows in the grid.

        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.

        :return:Returns the number of columns in the grid. 
        """
        return self._grid.num_cols()


    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.
        
        :param coord_list: 
        :return: 
        """
        self._grid.clear(LifeGrid.dead_cell)
        for coord in coord_list:
            row,col = coord
            self.set_cell(row,col)


    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?
        
        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return self._grid[(row,col)]

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[(row,col)] = LifeGrid.dead_cell


    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[(row,col)] = LifeGrid.live_cell


    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.

        :param row: row of the cell.
        :param col: column of the cell.
        :return: int
        """
        alive_neibs = 0
        for neib in LifeGrid.neighbours:
            i,j = neib
            new_row = row + i
            new_col = col + j
            try:
                cell_content = self._grid[(new_row,new_col)]
                if cell_content == LifeGrid.live_cell:
                    alive_neibs += 1
            except:
                pass


        return alive_neibs
