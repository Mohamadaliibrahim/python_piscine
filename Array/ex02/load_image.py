from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    try:
        img = Image.open(path)
        
        # Print image format
        print(f"The format of the image is: {img.format}")
        
        # # Convert image to RGB and convert to numpy array
        img_rgb = img.convert("RGB")
        img_array = np.array(img_rgb)
        
        # # Print the shape of the image and its content
        print(f"The shape of image is: {img_array.shape}")
        return img_array
        
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

print(ft_load("k.jpg"))