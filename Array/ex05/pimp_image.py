import numpy as np
import matplotlib.pyplot as plt


def lets_desplay(image: np.array):
    """
    Displays the image using matplotlib.
    """
    try:
        if image is None:
            raise ValueError("Invalid image")
        plt.imshow(image, cmap="gray" if image.ndim == 2 else None)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Zoomed Image")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


def ft_invert(array) -> np.ndarray:
    """
        Take an image array, and return a new array
        with colors inverted
    """
    invTransform = np.vectorize(lambda x: 255 - x)
    invert = invTransform(array)
    lets_desplay(invert)
    return invert


def ft_red(array) -> np.ndarray:
    """
        Take an image array, and return a new array
        with a red color filter
    """
    red = array.copy()
    for i in range(len(red)):
        for j in range(len(red[i])):
            red[i][j][1] = 0
            red[i][j][2] = 0
    lets_desplay(red)
    return red


def ft_green(array) -> np.ndarray:
    """
        Take an image array, and return a new array
        with a green color filter
    """
    green = array.copy()
    for i in range(len(green)):
        for j in range(len(green[i])):
            green[i][j][0] = 0
            green[i][j][2] = 0
    lets_desplay(green)
    return green


def ft_blue(array) -> np.ndarray:
    """
        Take an image array, and return a new array
        with a blue color filter
    """
    blue = array.copy()
    for i in range(len(blue)):
        for j in range(len(blue[i])):
            blue[i][j][0] = 0
            blue[i][j][1] = 0
    lets_desplay(blue)
    return blue


def add(a, b):
    """
        Add two numbers using bitwise operators
    """
    a = int(a)
    b = int(b)
    while (b != 0):
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


def ft_grey(array) -> np.ndarray:
    """
        Take an image array, and return a new array
        with a grayscale
    """
    grey = array.copy()
    for i in range(len(grey)):
        for j in range(len(grey[i])):
            val = 0
            if (grey[i][j][2] > 0):
                val = add(val, 0.2989 / (1 / grey[i][j][2]))
            if (grey[i][j][1] > 0):
                val = add(val, 0.5870 / (1 / grey[i][j][1]))
            if (grey[i][j][0] > 0):
                val = add(val, 0.1140 / (1 / grey[i][j][0]))
            grey[i][j][0] = grey[i][j][1] = grey[i][j][2] = val
    lets_desplay(grey)
    return grey
