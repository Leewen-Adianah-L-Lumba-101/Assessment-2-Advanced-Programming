"""
Created on Sat Dec 28 19:36:12 2024

@author: Leewen Lumba
"""
import customtkinter
from tkinter import *
import requests
from PIL import Image
from io import BytesIO
from PIL import ImageTk
import tmdbsimple as tmdb
from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import Person
from tmdbv3api import TV
from tmdbv3api import Discover
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

# Create class object instances
tv = TV()
movie = Movie()
discover = Discover()
person = Person()
tmdb = TMDb() 

tmdb.api_key = api_key
tmdb.language = 'en'
tmdb.debug = True

app = customtkinter.CTk()
count = 0
app.geometry("300x300")

movie = Movie()

m = movie.details(1359289)

print(m.title)
print(m.popularity)
print(dir(m))
print(m.overview)

word = m.title

# frame = customtkinter.CTkScrollableFrame(app, fg_color = "black").grid(
#     row = 0, column = 0, pady = (40,10))

label = customtkinter.CTkLabel(app, text = f"{word}").grid(row = 1, column = 0)

button = customtkinter.CTkButton(app, fg_color = "blue", text = "Delete frame contents",
                                  command = lambda: addframe(frame,count)
                                  ).grid(row = 2, column = 0, pady = 5)





# maybe consistently add numbers to the frame for loop, frames can be *generated* or packed by 
# having them in a list. There are a total of 20 results

# def addframe(frame,count):
#     frame2 = customtkinter.CTkFrame(frame, fg_color = "red")
#     frame2.grid(row = count, column = 0, padx = 10)
#     label = customtkinter.CTkLabel(frame2, text = "FRAME ADDED")
#     label.grid(row = count, column = 0)
#     count += 1

app.mainloop()


# From https://python-forum.io/thread-17418.html
# from tkinter import *
# import random
  
# def randomColor ():
#     randomRed = ("00" + hex(random.randint(0, 255))[2:])[-2]
#     randomGreen = ("00" + hex(random.randint(0, 255))[2:])[-2]
#     randomBlue = ("00" + hex(random.randint(0, 255))[2:])[-2]
#     return "#{}{}{}".format(randomRed, randomGreen, randomBlue)
  
# class RandomColorNestedFramesApp:
  
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry("500x500+50+50")
#         self.bgFrame = Frame(self.master, bg = randomColor())
#         self.bgFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
#         self.addFrameButton = Button(self.bgFrame, text = "add sub-frame", 
#                                      bg = "#FF00CC", fg = "black", font = "Times 11",
#                                      command = self.addDaughterFrame)
#         self.addFrameButton.place(relx = 0.5, rely = 0.8, relwidth = 0.25, 
#                                   relheight = 0.07, anchor = "center")
#         self.frameList = []
#         self.count = 0
  
#     def addDaughterFrame (self):
#         if len(self.frameList) < 1:
#             # if the length of the list is less than one, add a frame to the end of the list
#             # with a random background colour?
#             self.frameList.append(Frame(self.bgFrame, bg = randomColor()))
            
  
#         else:
#             # if the length of the list is more than one, add a frame at minus
#             self.frameList.append(Frame(self.frameList[-1], bg = randomColor()))
        
#         self.frameList[-1].place(anchor = "center", relx = 0.5, rely = 0.5, relwidth = 1, relheight = 0.95)
        
#         # YOU ADD FRAME WIDGETS IN A LIST THATS WHAT IT DOES
#         self.addFrameButton.lift()
  
# if __name__ == "__main__":
#     root = Tk()
#     theApp = RandomColorNestedFramesApp(root)
#     root.mainloop()
    
    
# import tkinter as tk
# myfont = "Helvitica 30"
# mybg = "lightskyblue"
 
 
# class Main:
 
#     def __init__(self, root):
#         self.root = tk.Tk()
#         self.root.geometry("500x500")
#         self.createfstframe()
 
#     def createfstframe(self):
#         fstframe = tk.Frame(root)
#         fstframe.pack(padx=100, pady=100)
#         self.Hellobn=tk.Button(fstframe,text = "Hello", bg = mybg, font = myfont)
#         self.Hellobn.pack(fill = tk.BOTH, expand = 1)
#         self.Howyoubn = tk.Button(fstframe, text="How are you? ",bg = mybg ,font = myfont)
#         self.Howyoubn.pack(fill = tk.BOTH, expand = 1)
#         self.clickherebn = tk.Button(fstframe, text = "Click here to start", bg = "deepskyblue",font = myfont)
#         self.clickherebn.pack(fill = tk.BOTH, expand = 1)
#         self.quitbn = tk.Button(fstframe,text = "Quit", font = myfont, bg = "red", command = fstframe.quit)
#         self.quitbn.pack(fill = tk.BOTH, expand = 1)
 
 
# root = tk.Tk()
# b=Main(root)
# root.mainloop()
