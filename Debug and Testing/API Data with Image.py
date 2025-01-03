# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:08:23 2024

@author: hp
"""
import requests
from tkinter import *
from PIL import Image
from io import BytesIO
from PIL import ImageTk

root = Tk()

label = Label(root, text = "")
label.pack()

def getData():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()
    
    # Drink_name = data["drinks"][0]['strDrink']
    
    # label.config(text=Drink_name)
    
    image_url = data['drinks'][0]['strDrinkThumb'] # Access Drink image url
    
    image_response = requests.get(image_url)
    
    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((150,150))
        image = ImageTk.PhotoImage(image)
        image_label = Label(root, image=image)
        image_label.image = image
        image_label.place(x=10, y=10)    
    
    
getData()

root.mainloop()


