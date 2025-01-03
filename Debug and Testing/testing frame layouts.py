# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:00:11 2024

@author: hp
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

tmdb = TMDb() # Create class instance

tmdb.api_key = 'f8da1365ead9eb420c108f560ff80670'
tmdb.language = 'en'
tmdb.debug = True

# def homeMenu():
    
#     resetWindow()
#     global resultscount, contentcontainer
    
#     app.configure(fg_color = "#9B1D20")
#     count.set(0)
    
#     panelframe = customtkinter.CTkFrame(app, width = 223, height = 700,
#                                         fg_color = "#071320", corner_radius = 0)
#     panelframe.pack(side = "left", fill = "both")
#     panelframe.pack_propagate(0)
    
#     mainstuff = customtkinter.CTkFrame(app, fg_color = "#FFFAFF", 
#                                        width = 637)
#     mainstuff.pack(side = "left", fill = "both", expand = True)
#     mainstuff.pack_propagate(0)
    
#     searchpanel = customtkinter.CTkFrame(mainstuff, fg_color = "#9B1D20",
#                                          width = 637, height = 79,
#                                          corner_radius = 0)
#     searchpanel.pack(side = "top", fill = "both")
#     searchpanel.pack_propagate(0)

    
#     searchbar = customtkinter.CTkEntry(searchpanel, width = 475, height = 23,
#                                        corner_radius = 10, border_color = "white",
#                                        textvariable = searchrequest)
#     searchbar.grid(row = 0, column = 0, padx = (40,20), pady = 10)
    
#     searchbtn = customtkinter.CTkButton(searchpanel, width = 98, height = 23,
#                                        text = "SEARCH", fg_color = "#00B3E5",
#                                        text_color = "#071320")
#     searchbtn.grid(row = 0, column = 1, padx = 10, pady = 10)

#     contentcontainer = customtkinter.CTkScrollableFrame(mainstuff, fg_color = "#FFFAFF")
#     contentcontainer.pack(side = "bottom", fill = "both", expand = True)
    
#     resultscount = customtkinter.CTkLabel(contentcontainer, text = f"{str(count.get())} RESULTS AVAILABLE",
#                                           font = resultstyle)
#     resultscount.grid(row = 0, column = 0, padx = 30, pady = 20, sticky = "W")
    
#     combobox_option = customtkinter.StringVar(value = "Movies")
#     combobox = customtkinter.CTkComboBox(contentcontainer, values=["Movies", "TV Shows"], 
#                                              variable = combobox_option, command = comboboxswitch)
#     combobox_option.set("Movies")
    
#     trendingbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320",
#                                           text_color = "#FFFAFF", text = "TRENDING",
#                                           font = buttonstyle, command = lambda: findChoice(choice = "Trending", widget = combobox))
#     trendingbtn.grid(row = 0, column = 0, padx = 20, pady = (100,25), sticky = "W")
    
   
#     shortlogo = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\hp\\Desktop\\Advanced Programming\\Assessment 2\\Assets\\The Movie Database Logo (SHORT).png"),
#                                       dark_image = None, size=(150, 66))
#     image_label = customtkinter.CTkLabel(master = panelframe, image=shortlogo, text="")
#     image_label.grid(row = 5, column = 0, pady = (60, 10), padx = 20)
    

# def removeWidget(widget):
#     widget.grid_remove()


# def addWidget(widget):
#     widget.grid(row = 1, column = 0, padx = 30, pady = 10, sticky = 'w')

# def countResults():

#     curr_count_value = count.get()
#     updated_integer_value = curr_count_value + 1
#     count.set(updated_integer_value)
    
#     if count.get() == 1:
#         resultscount.configure(text = f"{str(count.get())} RESULT AVAILABLE")
        
#     else:
#         resultscount.configure(text = f"{str(count.get())} RESULTS AVAILABLE")
        
# def comboboxswitch(useroption):    
    
#     global decider, chosen, movie, popular, poster_path
#     decider = useroption

#     no = 0
    
#     count.set(0)
    
#     if decider == "Movies" and chosen == "Trending":     
        
#         popular = movie.popular()
                
#         for p in popular:
#             no += 1
#             poster_path = p.poster_path
#             title = p.title
#             release_date = p.release_date
#             overview_info = p.overview
            
#             displayResults(contentcontainer, no, title, release_date, overview_info, poster_path)
            
#             countResults()

        
#     return decider, count


# def loadImage(frame, imagepath):
    
#     image_path = imagepath
    
#     #change the url constantly, instantiate the image_url by adding the url widths/heights, then
#     # add it with the variable image
#     image_url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/" + image_path
    
#     image_response = requests.get(image_url)
    
#     if image_response.status_code == 200:
#         image = Image.open(BytesIO(image_response.content))
#         image = image.resize((280,420))
#         image = ImageTk.PhotoImage(image)
#         image_label = Label(frame, image=image)
#         image_label.image = image
#         image_label.pack(side = "top", pady = (28,24), padx = (14,0))


# # def trendingResults(count):

# def displayResults(frame, setrange, movietitle, releasedate, overview, imagepath):
    
#     setrange = 5
    
#     for i in range(setrange):
#         imagetoload = imagepath

#         t = i
#         rowno = 2
#         panelofshame = customtkinter.CTkFrame(frame, fg_color = "white",
#                                               width = 637, height = 432)
#         panelofshame.grid_propagate(0)

#         panelofshame.grid(row = rowno, column = 0, padx = 5, pady = 5, 
#                           ipadx = 25, ipady = 30)
        
#         panelfortext = customtkinter.CTkFrame(panelofshame, fg_color = "white", width = 322, height = 330,
#                                               corner_radius = 0)
#         panelfortext.pack(side = "right", fill = "both", pady = 24, padx = (0, 20))
#         panelfortext.pack_propagate(0)

#         loadImage(panelofshame, imagetoload)
        
#         title = customtkinter.CTkLabel(panelofshame, text = f"{movietitle} ({releasedate})", font = movietitlestyle)
#         title.pack(side = "top", padx = (14,0))
        
#         overviewtitle = customtkinter.CTkLabel(panelfortext, text = "Overview", font = movietitlestyle)
#         overviewtitle.pack(side = "top")
        
#         details = customtkinter.CTkLabel(panelfortext, text = "").pack(side = "top")
#         overview = customtkinter.CTkLabel(panelfortext, text = f"""{overview}""", 
#                                           font = ("Montserrat", 16), 
#                                           justify = "left", wraplength= 300)
#         overview.pack(padx = 5, pady = 10, anchor = "ne")
#         t -= 1
#         rowno += 1
    

# def findChoice(choice,widget):
    
#     global decider, chosen
    
#     chosen = choice
#     count.set(0)
    
#     if chosen == "Trending":
#         addWidget(widget)
#         comboboxswitch(useroption = "Movies")
        

#     elif chosen == "NewReleases":
#         addWidget(widget) 
#         comboboxswitch(useroption = "Movies")
        
#         print(choice)
    
    
#     elif chosen == "Movies":
#         removeWidget(widget)
        
        
#         print(choice)
    
#     elif chosen == "TVShows":
#         removeWidget(widget)
        
#         print(choice)
    
#     elif chosen == "Actors":
#         removeWidget(widget)
        
#         print(choice)

root = customtkinter.CTk()
searchrequest = ""
buttonstyle = customtkinter.CTkFont(family = "Montserrat", size = 20)
headerstyle = customtkinter.CTkFont(family = "Montserrat", size = 32)
bodystyle = customtkinter.CTkFont(family = "Cabin", size = 20)
linkstyle = customtkinter.CTkFont(family = "Cabin", underline = True, size = 20)
movietitlestyle = customtkinter.CTkFont(family = "Montserrat", size = 25)

root.title("Test")
root.geometry("860x700")
root.resizable(0,0)
root.configure(fg_color = "#9B1D20")


panelframe = customtkinter.CTkFrame(root, width = 223, height = 700,
                                    fg_color = "#071320", corner_radius = 0)
panelframe.pack(side = "left", fill = "both")
panelframe.pack_propagate(0)

mainstuff = customtkinter.CTkFrame(root, fg_color = "#FFFAFF", 
                                    width = 637)
mainstuff.pack(side = "left", fill = "both", expand = True)
mainstuff.pack_propagate(0)

searchpanel = customtkinter.CTkFrame(mainstuff, fg_color = "#9B1D20",
                                      width = 637, height = 79,
                                      corner_radius = 0)
searchpanel.pack(side = "top", fill = "both")
searchpanel.pack_propagate(0)


searchbar = customtkinter.CTkEntry(searchpanel, width = 475, height = 23,
                                    corner_radius = 10, border_color = "white",
                                    textvariable = searchrequest)
searchbar.grid(row = 0, column = 0, padx = (30,20), pady = 10)

searchbtn = customtkinter.CTkButton(searchpanel, width = 98, height = 23,
                                    text = "SEARCH", fg_color = "#00B3E5",
                                    text_color = "#071320")
searchbtn.grid(row = 0, column = 1, padx = (5,10), pady = 10)

contentcontainer = customtkinter.CTkScrollableFrame(mainstuff, fg_color = "#FFFAFF")
contentcontainer.pack(side = "bottom", fill = "both", expand = True)



markers = ["red", "blue", "green"]
# framesinquestion = []


def loadImage(frame):
    
    #change the url constantly, instantiate the image_url by adding the url widths/heights, then
    # add it with the variable image
    image_url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/2cxhvwyEwRlysAmRH4iodkvo0z5.jpg"
    
    image_response = requests.get(image_url)
    
    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((280,420))
        image = ImageTk.PhotoImage(image)
        image_label = Label(frame, image=image)
        image_label.image = image
        image_label.pack(side = "top", pady = (28,24), padx = (14,0))


# change range to variable, consisting of the count of results
for i in range(3):

    t = i
    
    panelofshame = customtkinter.CTkFrame(contentcontainer, fg_color = "white",
                                          width = 637, height = 432)
    panelofshame.pack_propagate(0)
    panelofshame.pack(side = "top", fill = "both", expand = True, 
                      padx = 5, pady = 5, ipadx = 25, ipady = 30)
    
    panelfortext = customtkinter.CTkFrame(panelofshame, fg_color = "white", width = 322, height = 330,
                                          corner_radius = 0)
    panelfortext.pack(side = "right", fill = "both", pady = 24, padx = (0, 20))
    panelfortext.pack_propagate(0)

    loadImage(frame = panelofshame)
    
    title = customtkinter.CTkLabel(panelofshame, text = "Gladiator 3 (2024)", font = movietitlestyle)
    title.pack(side = "top", padx = (14,0))
    
    overviewtitle = customtkinter.CTkLabel(panelfortext, text = "Overview", font = movietitlestyle)
    overviewtitle.pack(side = "top")
    
    details = customtkinter.CTkLabel(panelfortext, text = "Action, Adventure, Drama").pack(side = "top")
    overview = customtkinter.CTkLabel(panelfortext, text = """Years after witnessing the death of the revered hero Maximus at the hands of his uncle, Lucius is forced to enter the Colosseum after his home is conquered by the tyrannical Emperors who now lead Rome with an iron fist. With rage in his heart and the future of the Empire at stake, Lucius must look to his past to find strength and honor to return the glory of Rome to its people.""", 
                                      font = ("Montserrat", 16), 
                                      justify = "left", wraplength= 300)
    overview.pack(padx = 5, pady = 10, anchor = "ne")
    t -= 1
    
    
root.mainloop()



# trendingbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320",
#                                       text_color = "#FFFAFF", text = "TRENDING",
#                                       font = buttonstyle)
# trendingbtn.grid(row = 0, column = 0, padx = 10, pady = (100,25), sticky = "w")

# newestreleasesbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320",
#                                       text_color = "#FFFAFF", text = """NEWEST 
# RELEASES""", font = buttonstyle)
# newestreleasesbtn.grid(row = 1, column = 0, padx = 10, pady = 25, sticky = "w")

# moviesbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320", 
#                                      text_color = "#FFFAFF", text = "MOVIES",
#                                      font = buttonstyle)
# moviesbtn.grid(row = 2, column = 0, padx = 10, pady = 25, sticky = "w")

# tvshowsbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320", text_color = "#FFFAFF", 
#                                     text = "TV SHOWS", font = buttonstyle)
# tvshowsbtn.grid(row = 3, column =  0, padx = 10, pady = 25, sticky = "w")

# actorbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320", text_color = "#FFFAFF", 
#                                     text = "ACTORS", font = buttonstyle)
# actorbtn.grid(row = 4, column = 0, padx = 10, pady = 25, sticky = "w")



# change font but keep size instance
# my_font.configure(family="Cabin") 

# change font but keep size instance
# my_font.configure(family="Cabin") 


#     class centeredframe(customtkinter.CTkFrame):
#         def __init__(self, app, **kwargs):
#             super().__init__(app, **kwargs)

#             self.shortlogo = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\hp\\Desktop\\Advanced Programming\\Assessment 2\\Assets\\The Movie Database Logo.png"),
#                                       dark_image = None, size=(550, 46.2))
#             self.image_label = customtkinter.CTkLabel(app, image=shortlogo, text="")
#             self.image_label.pack(padx = 10, pady = 50)

#             self.header = customtkinter.CTkLabel(app, text = "APPLICATION", font = headerstyle,text_color = "white")
#             self.header.pack(padx = 10)
    
#             self.about = customtkinter.CTkLabel(app, text = """A program developed by Leewen Lumba. 
# Accessing TMDB’s large, open-source, community built database for movies, TV shows,
# actors and genres with the TMDB site’s dedicated API.""",
#             text_color = "white", justify = "left", font = bodystyle)
#             self.about.pack(pady = 50)
    
#             self.startbtn = customtkinter.CTkButton(app, font = buttonstyle, text = "BEGIN",
#                                         fg_color = "#9B1D20", 
#                                         hover_color = "#99353A", 
#                                         height = 40, width = 240)
    
#             self.startbtn.pack(padx=10, pady=20)
    
#             self.creditsbtn = customtkinter.CTkButton(app, font = buttonstyle, text = "CREDITS",
#                                           text_color = "#0A121A",
#                                           fg_color = "#90CEA1",
#                                           hover_color = "#5CA18A",
#                                           height = 40, width = 240)
#             self.creditsbtn.pack()

# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x200")
#         self.grid_rowconfigure(0, weight=1)  # configure grid system
#         self.grid_columnconfigure(0, weight=1)

#         self.my_frame = MyFrame(master=self)
#         self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
