import time
import multiprocessing
import os
import logging
from .image_resize import resize_image
from .logger import setup_logger

# setting logging configuration
setup_logger()
# Input and output
images = ["data/input_images/img1.jpg", "data/input_images/img2.webp", "data/input_images/img3.jpg"]
outputs = ["data/output_images/resize1.jpg", "data/output_images/resize2.webp", "data/output_images/resize3.jpg"]

# ---------------------------
# Normal Execution
# ---------------------------
def normal_resize():
    logging.info(f"--- Normal Execution ---")
    start_time = time.time()
    for index in range(len(images)):
        try:
            resize_image(images[index], outputs[index])
        except Exception as e:
            logging.error(f"Unexpected error in normal execution: {e}")
    
    duration = time.time() - start_time
    logging.info(f"Normal execution time: {duration:.2f} seconds")
    return duration

# ---------------------------
# Multiprocessing Execution
# ---------------------------
def multiprocessing_resize():
    logging.info(f"--- Multiprocessing Execution ---")
    start_time = time.time()

    processes = []
    for index in range(len(images)):
        process = multiprocessing.Process(target=resize_image, args=(images[index], outputs[index]))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    duration = time.time() - start_time
    logging.info(f"Multiprocessing execution time: {duration:.2f} seconds")
    return duration

# ---------------------------
# Main Program
# ---------------------------
if __name__ == "__main__":
    normal_time = normal_resize()
    multiprocessing_time = multiprocessing_resize()
    
    # Performance Comparison
    logging.info(f"--- Performance Comparison ---")
    logging.info(f"Normal execution took: {normal_time:.2f} seconds")
    logging.info(f"Multiprocessing execution took: {multiprocessing_time:.2f} seconds")
    # only if multiprocessing_time > 0 to prevent zero division
    improvement = normal_time / multiprocessing_time if multiprocessing_time > 0 else 0
    logging.info(f"Multiprocessing speedup {improvement:.2f}x faster")
