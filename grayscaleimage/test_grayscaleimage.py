from grayscaleimage import GrayscaleImage

def test():
    """
    Test Graysclaleimage class
    :return: 
    """
    im = GrayscaleImage(720,480)
    print(im.height())
    print(im.width())
    for i in range(720):
        im[(i,0)] = 255

    print(im[(34,0)])

if __name__ == "__main__":
    test()