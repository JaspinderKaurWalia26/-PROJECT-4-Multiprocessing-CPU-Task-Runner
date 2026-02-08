# Multiprocessing CPU Task Runner

## Project Overview
Multiprocessing CPU Task Runner is a Python-based system that resizes multiple images using sequential execution and multiprocessing.
The project demonstrates how CPU-intensive tasks, like image resizing, can be speed up by executing tasks in parallel using Python’s multiprocessing module.

---

## What does this project do?
- Resizes multiple images sequentially (normal execution) and in parallel (multiprocessing execution)
- Measures execution time for both modes
- Logs each image’s resizing status and any errors
- Compares performance to show the speedup achieved with multiprocessing

---
## Why Multiprocessing is Used

- Python threads are limited by the Global Interpreter Lock (GIL) for CPU-heavy tasks.
- Multiprocessing allows true parallel execution by creating multiple processes.
- This project shows how multiprocessing reduces execution time for CPU-bound tasks like image resizing.

### Benefits of Multiprocessing
- True parallel execution for CPU-heavy -tasks
- Faster overall execution
- Efficient use of CPU cores
- Scalable for multiple images or other CPU-heavy tasks
---

##  Technologies Used
- Python 3
- os module
- Pillow (PIL) for image processing
- logging module
- time module
---

## 📁 Project Structure
```
MULTIPROCESSING_CPU_TASK/
│
├── data/
│   ├── input_images/ # Folder containing original images  
│   │   ├── img1.jpg
│   │   ├── img2.webp
│   │   └── img3.jpg
│   │
│   └── output_images/ # Folder where resized images will be saved
│       ├── resize1.jpg
│       ├── resize2.webp
│       └── resize3.jpg
│
├── logs/
│   └── app.log # Logging file for program execution
│
├── src/
│   └── Image_Resizer/
│       ├── __init__.py # Allows importing files from this folder as a package
│       ├── image_resize.py #Image resizing logic  
│       ├── logger.py # Sets up logging configuration
│       └── main.py # Program entry point
│
├── README.md # Project documentation
└── requirements.txt # Project dependencies

```
## How to Run
### 1. Clone the repository
```
git clone https://github.com/JaspinderKaurWalia26/-PROJECT-4-Multiprocessing-CPU-Task-Runner.git
cd PROJECT-4-Multiprocessing-CPU-Task-Runner
```
### 2. Create a virtual environment (optional)
```
python -m venv venv
```
### 3. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```
### 4. Install dependencies
```
pip install -r requirements.txt
```
### 5. Run the program
```
python -m src.Image_Resizer.main
```
### 6. Check outputs

- Resized Images: data/output_images

- Logs: logs/app.log



