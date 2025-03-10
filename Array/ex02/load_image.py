from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a given file path and convert it to a NumPy array.

    Args:
        path (str): The file path of the image to load.

    Returns:
        np.ndarray: A NumPy array representing the image in RGB format.
        
    If an error occurs during image loading, it will return None.
    """
    try:
        # Open the image from the specified path
        img = Image.open(path)
        
        # Print image format (e.g., JPEG, PNG)
        print(f"The format of the image is: {img.format}")
        
        # Convert image to RGB (if it's not in RGB already) and convert to numpy array
        img_rgb = img.convert("RGB")
        img_array = np.array(img_rgb)
        
        # Print the shape of the image and its content
        print(f"The shape of the image is: {img_array.shape}")
        
        return img_array
        
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Test the function with an example image
print(ft_load("k.jpg"))
