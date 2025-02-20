import tkinter as tk
from tkinter import ttk
import requests
import os
from PIL import Image, ImageTk
import io

API_KEY = os.environ['THIRDAPIKEY']
WIDTH = 800
HEIGHT = 600
k = 0.7

def place_image():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}&count=1')
    image_pil = Image.open(io.BytesIO(requests.get(response.json()[0]['url']).content))
    image_label.im = ImageTk.PhotoImage(image_pil.resize((int(WIDTH * k), int(HEIGHT * k))))
    image_label.config(image=image_label.im)
    
    window.update()

def check():
    print(image_label.im.height())

window = tk.Tk()
window.geometry(f'{WIDTH}x{HEIGHT}')
window.resizable(False, False)
window.title('NASA APOD')
image_label = tk.Label(window)
image_label.im = None
image_label.place(width=int(WIDTH * k), height=int(HEIGHT * k), x=WIDTH * 0.3 // 2, y=0)
button = tk.Button(text='Change image', command=place_image)
button.place(x=(WIDTH - 150) // 2, y=int(HEIGHT * 0.8), height=50, width=150)


window.mainloop()