from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
import cv2


def zoom_image(image: np.ndarray, size: int = 400) -> np.ndarray:
    """
    Extracts the center of the image and zooms it in.
    """
    try:
        if image is None:
            raise ValueError("Invalid image")

        height, width, *channels = image.shape
        center_x, center_y = width // 2, height // 2
        half_size = size // 2

        zoomed = image[center_y - half_size:center_y + half_size,
                       center_x - half_size:center_x + half_size]
        return zoomed
    except Exception as e:
        print(f"Error: {e}")
        return None


def rotate(array):
    """
        Rotate an array
    """
    return np.asarray(list(list(x) for x in zip(*array))[::-1])


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


def rotate_image(image: np.ndarray) -> np.ndarray:
    """
    Rotate the image.
    """
    try:
        if image is None:
            raise ValueError("Invalid image")

        array = image.tolist()
        Rotate = [
            [array[j][i] for j in range(len(array))]
            for i in range(len(array[0]))]
        Rotate_array = np.array(Rotate)
        print(f"New shape after Transpose: {Rotate_array.shape}")
        print(Rotate_array)
        return Rotate_array
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """
    The main function of the code
    """
    image = ft_load("animal.jpeg")
    if image is not None:
        zoomed_image = zoom_image(image)
        grayscale_image = cv2.cvtColor(zoomed_image, cv2.COLOR_BGR2GRAY)
        print(f"The shape of image is: {grayscale_image.shape}")
        print(grayscale_image)
        if zoom_image:
            image = rotate_image(grayscale_image)
            lets_desplay(image)


if __name__ == "__main__":
    main()
