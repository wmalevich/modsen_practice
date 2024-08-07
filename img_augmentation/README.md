## Image Augmentation Application

This application is designed to apply various transformations to images, aiming to increase the size of training datasets and improve the generalization capabilities of models.

![Development Status](https://img.shields.io/badge/status-active-brightgreen)

## Features

- Select input and output directories for images
- Set the number of images to create
- Resize and rotate images
- Adjust the brightness, contrast, and saturation of images
- Apply random cropping
- Add noise to images

## Contents
- [Technologies](#technologies)
- [Getting Started](#getting-started)

## Technologies
- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tk.html)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
- [NumPy](https://numpy.org/doc/2.0/)

## Getting Started
To install and use this project, follow these steps:

### Requirements
- Python 3.6 or higher

### Install the required dependencies:
```sh
$ pip install -r requirements.txt
```

### Usage
Run the application:
```sh
$ python main.py
```

## Testing
For testing purposes, the unittest framework in Python was utilized

To execute the unit tests:
```sh
$ python tests/processor_test.py
```
