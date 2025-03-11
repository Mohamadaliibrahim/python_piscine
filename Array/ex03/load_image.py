from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """
    Loads an image and prints it's shape, then returns pixel
    content in NumPy array, supports jpeg, jpg
    """
    try:
        img = Image.open(path)
        if img.format not in ['JPEG', 'JPG']:
            raise ValueError(f"Unsupported image format: {img.format}")

        image_array = np.array(img)
        print(f"The shape of image is: {image_array.shape}")
        print(image_array)
        return image_array
    except FileNotFoundError:
        print(f"File not found: {path}")
    except ValueError as e:
        print("ValueError:", e)
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
