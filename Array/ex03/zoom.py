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
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        return zoomed
    except Exception as e:
        print(f"Error: {e}")
        return None


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


def main():
    """
        Open the image, trim it and convert it to grayscale,
        then display it.
    """
    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        exit()

    print('The shape of image is', image.shape)
    print(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = zoom_image(image)

    print(f'New shape after slicing: {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)
    lets_desplay(image)


if __name__ == "__main__":
    main()
