#!/usr/bin/env python3
# Import the required modules
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import os


# Define a function to compress an image
def compress_image(image_name, quality, to_jpg):
    # Open the image file
    img = Image.open(image_name)
    # If to_jpg is True, convert the image to JPEG format
    if to_jpg:
        img = img.convert("RGB")
        image_name = image_name.rsplit(".", 1)[0] + ".jpg"
    #else:
     #   image_name = 'compressed_' + image_name
    # Save the image with the specified quality
    img.save(image_name, optimize=True, quality=quality)
    # Return the new size of the image
    return (True)


def main():
    print('Please select an image\n')
    file_name = askopenfilename()
    print(f'You selected {file_name} that has a size of {os.path.getsize(file_name)}')
    if file_name:
        qual = input("\nHello there, please input quality(0-100): ")
        qual = int(qual)
        to_jpeg = input("\n\nWould you like to convert to JPEG(Y/N):  ")
        if to_jpeg == 'Y' or to_jpeg == 'y':
            to_jpeg = True
        else:
            to_jpeg = False
        success = compress_image(file_name, qual, to_jpeg)
        if success:
            print(f"\nSuccessfully compressed {file_name}")
            print(f"The file now has a size of {os.path.getsize(file_name)}")


main()
