#!/usr/bin/env python3
# Import the required modules
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import os


def compress(self):
        '''Main compressar method'''
        if file_path:
            ext = image_name.split('.')[-1]
            if to_jpg_var.get() and ext not in ['.jpg', '.jpeg']:
                img = Image.open(file_path)
                img = img.convert("RGB")
                img_name = image_name
                image_name = image_name.split(".")[0] + "_comp" + \
                    ".jpg"
                if not folder_path:
                    user_desktop = os.path.expanduser("~/Desktop")
                    folder_path = user_desktop
                img.save(f'{folder_path}/{image_name}',
                         "JPEG", optimize=True, quality=slider_value)
            else:
                img = Image.open(file_path)
                img_width, img_height = img.size
                new_height = (slider_value / 100) * img_height
                new_width = (slider_value / 100) * img_width
                img = img.resize((round(new_width), round(new_height)))
                img_name = image_name
                image_name = image_name.split(".")[0] + "_comp." + \
                    ext
                if not folder_path:
                    user_desktop = os.path.expanduser("~/Desktop")
                    folder_path = user_desktop
                img.save(f'{folder_path}/{image_name}',
                         optimize=True,
                         quality=slider_value)

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
