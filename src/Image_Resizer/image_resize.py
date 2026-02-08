from PIL import Image
import os
import logging
from .logger import setup_logger

# setting logging configuration
setup_logger()
# resizing an image to the given size
def resize_image(image_path, output_path, size=(7000,7000)):
    try:
        img = Image.open(image_path)
        img = img.resize(size)
        img.save(output_path)
        logging.info(f"{os.path.basename(image_path)} resized")
    except FileNotFoundError:
        logging.error(f"File not found: {image_path}")
    except Exception as e:
        logging.error(f"Unexpected error for {image_path}: {e}")
        


