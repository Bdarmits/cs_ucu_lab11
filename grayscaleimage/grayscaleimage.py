from arrays import Array2D

class GrayscaleImage():
    """
    Grayscale Image ADT for saving and processing digital images
    """
    def __init__(self,nrows,ncols):
        """
        Creates an Image object with nrows X ncols pixels
        :param nrows: num of rows
        :param ncols: num of cols
        """
        self._nrows = nrows
        self._ncols = ncols

        self._image = Array2D(nrows,ncols)
        self.clear(0)


    def width(self):
        """
        Get image width
        :return: num of cols(width)
        """
        return self._ncols


    def height(self):
        """
        Get image height
        :return: num of rows(height)
        """
        return self._nrows


    @staticmethod
    def check_value(value):
        """
        Checks value for correctness
        :param value: int, value to check
        :return: True if value is correct raises ValueError otherwise
        """
        if 0 <= value <= 255:
            return 1
        else:
            raise ValueError("Value should be in range (0,255)")


    def clear(self,value):
        """
        Sets all the cells to given value
        
        :param value: value to set to
        :return: None
        """
        GrayscaleImage.check_value(value)
        self._image.clear(value)


    def __getitem__(self, row_col):
        """
        Gets the contents of the element at position [i, j]
        
        :param row_col: tuple of coordinates row and col
        :return: value which was set to
        """
        return self._image.__getitem__(row_col)


    def __setitem__(self, row_col, value):
        """
        Sets the contents of the element at position [i,j] to value
        
        :param row_col: coordinates row and col
        :param value: value to set to
        :return: None
        """
        GrayscaleImage.check_value(value)
        self._image.__setitem__(row_col,value)
