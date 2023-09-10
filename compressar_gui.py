#!/usr/bin/env python3
''' compressar_gui module.
Usage:
    ./compressar_gui.py
Author:
    Abdulsalam Abdulsomad .A. - August/September, 2023.
'''
import tkinter as tk
from tkinter import ttk, Scale, BooleanVar, Checkbutton, messagebox
from tkinter.filedialog import askdirectory, askopenfilename
import random
import os
from PIL import Image


class CompressarGui():
    def __init__(self):
        '''Constructs all the necessary attributes for the compressarGui'''
        # -- main compressar window --
        self.window = tk.Tk()
        self.window.configure(bg="#333333")
        self.window.title("Compressar")
        # self.window.geometry("300x300")

        # Initialize folder path to none
        self.folder_path = None
        self.file_path = None
        self.img_name = None

        # -- select image button --
        self.select_button = tk.Button(self.window,
                                       text="Select Image",
                                       bg='orange',
                                       command=self.select_image)
        self.select_button.grid(row=0, column=0, sticky='w', padx=5, pady=10)

        # -- Property label --
        self.property_label = tk.Label(self.window,
                                       text='New Property:',
                                       bg='orange')
        self.property_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)

        # -- Scale widget to adjust the quality of the image --
        self.quality_scale = Scale(self.window,
                                   from_=1, to=100,
                                   orient='horizontal',
                                   label="Select Quality:",
                                   bg="orange")
        self.quality_scale.set(90)
        self.quality_scale.grid(row=2,
                                sticky='nsew', padx=50,
                                pady=5, columnspan=2)
        # Initialize slider value to its default
        self.slider_value = self.quality_scale.get()

        # -- Destination folder selector --
        self.destination_label = tk.Label(self.window,
                                          text='Destination:',
                                          bg='orange')
        self.destination_label.grid(row=3, column=0, sticky='w',
                                    padx=5, pady=5)

        self.destination_btn = tk.Button(self.window,
                                         text="Select Folder",
                                         command=self.destination_folder,
                                         bg='orange')
        self.destination_btn.grid(row=4,
                                  column=0, sticky='nse',
                                  padx=15, pady=5)

        self.entry_var = tk.StringVar()
        self.destination_entry = tk.Entry(self.window,
                                          textvariable=self.entry_var)
        self.destination_entry.grid(row=4, column=1)

        # -- Format check label --
        self.format_label = tk.Label(self.window, text='Format:', bg='orange')
        self.format_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')

        self.to_jpg_var = BooleanVar()
        self.to_jpg_checkbutton = Checkbutton(self.window,
                                              text="Convert to JPEG",
                                              variable=self.to_jpg_var,
                                              bg='orange')
        self.to_jpg_checkbutton.grid(row=6, sticky='w', padx=30, pady=5)

        # -- Fact button --
        self.facts_btn = tk.Button(self.window,
                                   text='Quick Fact',
                                   command=self.display_facts,
                                   bg='orange')
        self.facts_btn.grid(row=6,
                            column=2, columnspan=2,
                            sticky="swe", padx=5, pady=5)
        # -- Compress button --
        self.compressbtn = tk.Button(self.window,
                                     text='compress',
                                     command=self.compress,
                                     bg='orange')
        self.compressbtn.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

        self.window.grid_columnconfigure(index=0, weight=1)
        self.window.grid_columnconfigure(index=1, weight=1)
        self.window.grid_columnconfigure(index=2, weight=1)
        self.window.resizable(False, False)
        # self.window.grid_rowconfigure(index=2, weight=2)
        self.quality_scale.bind("<Motion>", self.get_slider_value)
        self.window.protocol("WM_DELETE_WINDOW", self.close)

        self.window.mainloop()

    def close(self):
        '''prompts user before closing Gui'''
        if messagebox.askyesno(title="Quit?",
                               message="Do you really wanna quit?"):
            self.window.destroy()

    # -- Display Facts randomly --
    def display_facts(self):
        '''displays facts randomly from facts.txt'''
        try:
            with open("facts.txt", "r") as file:
                # add all lines to a list
                lines = [line.strip() for line in file.readlines()]
                # Ensure list is not empty
                if lines:
                    quick_fact = random.choice(lines)
                    messagebox.showinfo("Did you know?", quick_fact)
        except Exception:
            messagebox.showinfo("Gratitude", "Thank you for choosing Compressar :)")

    # -- Return quality value --
    def get_slider_value(self, event):
        '''Returns slider position'''
        self.slider_value = int(self.quality_scale.get())
        return (self.slider_value)

    def destination_folder(self):
        '''Returns selected save directory'''
        self.folder_path = askdirectory()
        if self.folder_path:
            folder_w_ext = os.path.basename(self.folder_path)
            self.entry_var.set(folder_w_ext)
            return (self.folder_path)

    def select_image(self):
        '''Returns user selected image'''
        self.file_path = askopenfilename(title="Select Image",
                                         filetypes=[
                                             ("Image Files",
                                              "*.jpg *.jpeg\
                                              *.png *.bmp\
                                                *.gif")])
        if self.file_path:
            self.image_name = os.path.basename(self.file_path)
            return (self.file_path)
        else:
            messagebox.showerror("Image Error", "Please Select An Image")

    def to_jpg(self):
        '''Returns true if button is clicked otherwise false'''
        return (self.to_jpg_var.get())

    def compress(self):
        '''Main compressar method'''
        if self.file_path:
            ext = self.image_name.split('.')[-1]
            if self.to_jpg_var.get() and ext not in ['.jpg', '.jpeg']:
                img = Image.open(self.file_path)
                img = img.convert("RGB")
                self.img_name = self.image_name
                self.image_name = self.image_name.split(".")[0] + "_comp" + ".jpg"
                if not self.folder_path:
                    user_desktop = os.path.expanduser("~/Desktop")
                    self.folder_path = user_desktop
                img.save(f'{self.folder_path}/{self.image_name}',
                        "JPEG", optimize=True, quality=self.slider_value)
            else:
                img = Image.open(self.file_path)
                img_width, img_height = img.size
                new_height = (self.slider_value / 100) * img_height
                new_width = (self.slider_value / 100) * img_width
                img = img.resize((round(new_width), round(new_height)))
                self.img_name = self.image_name
                self.image_name = self.image_name.split(".")[0] + "_comp." + ext
                if not self.folder_path:
                    user_desktop = os.path.expanduser("~/Desktop")
                    self.folder_path = user_desktop
                img.save(f'{self.folder_path}/{self.image_name}',
                        optimize=True,
                        quality=self.slider_value)
            # Reset attributes value
            self.file_path = None
            self.quality_scale.set(90)
            self.destination_entry.delete(0, tk.END)
            self.to_jpg_var = False

            messagebox.showinfo('Compressed',
                                f'Compressed {self.img_name} successfully')
        else:
            messagebox.showerror('Image Selection Error',
                                 'Please select an image')


CompressarGui()
