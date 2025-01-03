"""
Created on Sat Dec  7 14:52:49 2024
@author: Leewen Lumba
"""
# Libraries needed for program
import webbrowser
import customtkinter
from tkinter import *
import requests
from PIL import Image
from io import BytesIO
from PIL import ImageTk
from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import Person
from tmdbv3api import TV
from tmdbv3api import Discover

from dotenv import load_dotenv
import os

# Python files from local directory (developed by student)
import MovieTVGenres as mtv

# Obtain environment variables from computer and add them to program
load_dotenv()
tvgenres = mtv.tvshowgenres
moviegenres = mtv.moviegenres

# Creating the window for the application and special customtkinter variables
app = customtkinter.CTk()
searchrequest = customtkinter.StringVar()
decider = ""
count = customtkinter.IntVar()
count.set(0)

# Accessing API_KEY variable from environment path
api_key = os.getenv("API_KEY")

# Creating a class object instance for tmdb class, neccessary to implement api_key
tmdb = TMDb()
tmdb.api_key = api_key
tmdb.language = 'en'

# Making class object instances from the tmdbv3api library
movie = Movie()
tv = TV()
discover = Discover()
person = Person()

# Font Styles
buttonstyle = customtkinter.CTkFont(family = "Montserrat", size = 20)
headerstyle = customtkinter.CTkFont(family = "Montserrat", size = 32)
bodystyle = customtkinter.CTkFont(family = "Cabin", size = 20)
linkstyle = customtkinter.CTkFont(family = "Cabin", underline = True, size = 20)
resultstyle = customtkinter.CTkFont(family = "Cabin", size = 36)
movietitlestyle = customtkinter.CTkFont(family = "Montserrat", size = 25)

# Function to remove every item from a window
def resetWindow():
    for item in app.winfo_children():
        item.destroy()

# Main menu to introduce the user to application and provide credits for the libraries and information used
def mainMenu():
    
    resetWindow()
    app.configure(fg_color = "#071320")
    
    space = customtkinter.CTkLabel(app, text = "")
    space.pack(pady = 10)
    
    my_image = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\hp\\Desktop\\Advanced Programming\\Assessment 2\\Assets\\The Movie Database Logo.png"),
                                      dark_image = None, size=(550, 46.2))
    image_label = customtkinter.CTkLabel(master = app, image=my_image, text="")
    image_label.pack(padx = 10, pady = (60, 10))

    header = customtkinter.CTkLabel(app, text = "APPLICATION", font = headerstyle, text_color = "white")
    header.pack()
    
    frame = customtkinter.CTkFrame(app, width = 596, fg_color = "#071320")
    frame.pack(pady = 50)
    frame.pack_propagate(0)
    
    about = customtkinter.CTkLabel(frame, text = """
Developed by Leewen Lumba. 

Access TMDB’s large, open-source, community built database for 
movies, TV shows, actors and genres with the TMDB site’s dedicated 
API.

Press begin to navigate the app’s features.""",
    text_color = "white", justify = "left", font = bodystyle)
    about.grid(row = 0, column = 0, sticky = "we")
    
    startbtn = customtkinter.CTkButton(app, font = buttonstyle, text = "BEGIN",
                                       fg_color = "#9B1D20", 
                                       hover_color = "#99353A", 
                                       height = 40, width = 229, command = lambda: homeMenu())
    
    startbtn.pack(padx=10, pady=20)
    
    creditsbtn = customtkinter.CTkButton(app, font = buttonstyle, text = "CREDITS",
                                         text_color = "#0A121A",
                                         fg_color = "#90CEA1",
                                         hover_color = "#5CA18A",
                                         height = 40, width = 229, command = lambda: creditsMenu())
    creditsbtn.pack()
    
# Credits menu that include clickable links, opens browser to the sites binded to the label widget
def creditsMenu():
    
    resetWindow()
    app.configure(fg_color = "#9B1D20")
    
    space = customtkinter.CTkLabel(app, text = "")
    space.pack(pady = 10)
    
    my_image = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\hp\\Desktop\\Advanced Programming\\Assessment 2\\Assets\\The Movie Database Logo.png"),
                                      dark_image = None, size=(550, 46.2))
    image_label = customtkinter.CTkLabel(master = app, image=my_image, text="")
    image_label.pack(pady = (60, 10))

    header = customtkinter.CTkLabel(app, text = "CREDITS", font = headerstyle,text_color = "white")
    header.pack()
    
    frame1 = customtkinter.CTkFrame(master = app, height = 300, fg_color = "#9B1D20")
    frame1.pack(pady = 30)
    
    frameleft = customtkinter.CTkFrame(frame1, fg_color = "#9B1D20",
                                       width = 295, height = 300)
    frameleft.pack(side = "left", fill = "x", expand = False)
    frameleft.pack_propagate(0) # _propagate(0) is to ensure the frames follow the width/height set in CTkFrames
    
    frameright = customtkinter.CTkFrame(frame1, fg_color = "#9B1D20",
                                       width = 295, height = 300)
    frameright.pack(side = "left", fill = "x", expand = False)
    frameright.pack_propagate(0)

    
    sentence = customtkinter.CTkLabel(frameleft, text = """CustomTkinter python library 
(modern GUI Tkinter)""", font = linkstyle, text_color = "white", justify = "left", cursor = "hand2")
    sentence.grid(sticky = "w", pady = 20)
    
    sentence.bind("<Button-1>", 
        lambda e: webbrowser.open_new("https://customtkinter.tomschimansky.com"))
    
    
    sentence2 = customtkinter.CTkLabel(frameleft, text = """API and Database""", font = linkstyle, text_color = "white", 
    justify = "left", cursor = "hand2")
    sentence2.grid(sticky = "w", pady = 20)
    
    sentence2.bind("<Button-1>", 
        lambda e: webbrowser.open_new("https://developer.themoviedb.org/docs/getting-started"))
    
    
    sentence3 = customtkinter.CTkLabel(frameleft, text = """tmdbv3api Wrapper for 
querying data""", font = linkstyle, text_color = "white",
    justify = "left", cursor = "hand2")
    sentence3.grid(sticky = "w", pady = 20)
    
    sentence3.bind("<Button-1>", 
        lambda e: webbrowser.open_new("https://pypi.org/project/tmdbv3api/"))
    
    
    sentence_5 = customtkinter.CTkLabel(frameright, text = """by Tom Schimansky""", font = bodystyle, text_color = "white")
    sentence_5.grid(sticky = "e", pady = 25, padx = 10)
    
    sentence_6 = customtkinter.CTkLabel(frameright, text = """by TMDB""", font = bodystyle, text_color = "white")
    sentence_6.grid(sticky = "e", pady = 25, padx = 10)
    
    sentence_7 = customtkinter.CTkLabel(frameright, text = """by Anthony Bloomer""", font = bodystyle, text_color = "white")
    sentence_7.grid(sticky = "e", pady = 20, padx = 10)
    
    gobackbtn = customtkinter.CTkButton(app,font = buttonstyle, text = "BACK",
                                       text_color = "#0A121A",
                                       fg_color = "#90CEA1",
                                       hover_color = "#5CA18A",
                                       height = 40, width = 229, command = lambda: mainMenu())
    gobackbtn.pack(padx = 10, pady = 20)

# Function that shows all the possible ways user can query data, a side panel for navigating information
# and a search function
def homeMenu():
    
    resetWindow()
    global resultscount, contentcontainer, combobox, combobox2, combobox3, panelofcontent
    
    app.configure(fg_color = "#9B1D20")
    count.set(0)
    
    panelframe = customtkinter.CTkFrame(app, width = 223, height = 700,
                                        fg_color = "#071320", corner_radius = 0)
    panelframe.pack(side = "left", fill = "both")
    panelframe.pack_propagate(0)
    
    mainstuff = customtkinter.CTkFrame(app, fg_color = "#FFFAFF", 
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
    searchbar.grid(row = 0, column = 0, padx = (40,20), pady = 10)
    
    searchbtn = customtkinter.CTkButton(searchpanel, width = 98, height = 23,
                                       text = "SEARCH", fg_color = "#00B3E5",
                                       text_color = "#071320", command = searchTerm)
    searchbtn.grid(row = 0, column = 1, padx = 10, pady = 10)

    contentcontainer = customtkinter.CTkScrollableFrame(mainstuff, fg_color = "#FFFAFF")
    contentcontainer.pack(side = "bottom", fill = "both", expand = True)
    
    panelofcontent = customtkinter.CTkFrame(contentcontainer, fg_color = "white",
                                          width = 637, height = 432)

    resultscount = customtkinter.CTkLabel(contentcontainer, text = f"{str(count.get())} RESULTS AVAILABLE",
                                          font = resultstyle)
    resultscount.grid(row = 0, column = 0, padx = 30, pady = 20, sticky = "W")
    
    # The first option on the list of the combobox is a string value 'Movies' by default
    # When the Trending button is run for example, it will display the movies first
    combobox_option = customtkinter.StringVar(value = "Movies")
    combobox = customtkinter.CTkComboBox(contentcontainer, values=["Movies", "TV Shows"], 
                                             variable = combobox_option, command = comboboxswitch)
    combobox_option.set("Movies")
    
    # Pressing the other values in the 'dropdown menu' will run the command 'comboswitch', 
    # this is the same procedure for the two other comboboxes, but with their different values/options
    combobox2_option = customtkinter.StringVar(value = "Action")
    mgenres = mtv.returnAllGenres(mtv.moviegenres)
    combobox2 = customtkinter.CTkComboBox(contentcontainer, values = mgenres,
                                          variable = combobox2_option, command = comboboxswitch2)
    combobox2_option.set(mgenres[0])
    
    combobox3_option = customtkinter.StringVar(value = "Action & Adventure")
    tvgenres = mtv.returnAllGenres(mtv.tvshowgenres)
    combobox3 = customtkinter.CTkComboBox(contentcontainer, values = tvgenres,
                                          variable = combobox3_option, command = comboboxswitch3)
    combobox3_option.set(tvgenres[0])
    
    trendingbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320",
                                          text_color = "#FFFAFF", text = "TRENDING",
                                          font = buttonstyle, command = lambda: findChoice(choice = "Trending", widget = combobox))
    trendingbtn.grid(row = 0, column = 0, padx = 20, pady = (100,25), sticky = "W")
    
    newestreleasesbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320",
                                          text_color = "#FFFAFF", text = """NEWEST 
RELEASES""", font = buttonstyle, command = lambda: findChoice(choice = "NewReleases", widget = combobox))
    newestreleasesbtn.grid(row = 1, column = 0, padx = 20, pady = 25, sticky = "W")
    
    moviesbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320", 
                                         text_color = "#FFFAFF", text = "MOVIES",
                                         font = buttonstyle, command = lambda: findChoice(choice = "Movies", widget = combobox))
    moviesbtn.grid(row = 2, column = 0, padx = 20, pady = 25, sticky = "W")
    
    tvshowsbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320", text_color = "#FFFAFF", 
                                        text = "TV SHOWS", font = buttonstyle,
                                        command = lambda: findChoice(choice = "TVShows", widget = combobox))
    tvshowsbtn.grid(row = 3, column =  0, padx = 20, pady = 25, sticky = "W")
    
    actorbtn = customtkinter.CTkButton(panelframe, fg_color = "#071320", text_color = "#FFFAFF", 
                                        text = "ACTORS", font = buttonstyle,
                                        command = lambda: findChoice(choice = "Actors", widget = combobox))
    actorbtn.grid(row = 4, column = 0, padx = 20, pady = 25, sticky = "W")
    
    # Logo at the bottom of the side panel
    shortlogo = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\hp\\Desktop\\Advanced Programming\\Assessment 2\\Assets\\The Movie Database Logo (SHORT).png"),
                                      dark_image = None, size=(150, 66))
    image_label = customtkinter.CTkLabel(master = panelframe, image=shortlogo, text="")
    image_label.grid(row = 5, column = 0, pady = (60, 10), padx = 20)
    
# Gets user input from search bar and displays a result, most likely the first thing that will 
# show up is a movie search, if not a tv show then an actor
def searchTerm():
    searchoption = searchrequest.get()
    
    # rowno1 is here because the actors page doesnt have any combobox functions
    rowno = 1
    
    search = movie.search(searchoption)
    homeMenu()
    
    for i in search:
        
        try:
            movietitle = i.title
            releasedate = i.release_date
            overview = i.overview
            imagepath = i.poster_path
            idnames = i.genre_ids
            decider = "Movies"

            trendingResults(contentcontainer, rowno, movietitle, releasedate, overview, imagepath, idnames, decider)
            rowno += 1
            countResults()
        
        # If one of the variables is a NoneType (no value) or has no attributes, it will pass
        # The search to the next function
        except AttributeError or TypeError:
            search = tv.search(searchoption)
            
            for i in search:
                
                try:
                    showtitle = i.name
                    releasedate = i.first_air_date
                    overview = i.overview
                    imagepath = i.poster_path
                    idnames = i.genre_ids
                    decider = "TV Shows"
                    
                    trendingResults(contentcontainer, rowno, showtitle, releasedate, overview, imagepath, idnames, decider)
                    rowno += 1
                    countResults()
                    
                except AttributeError or TypeError:
                    search = person.search(str(searchoption))
                    setrange = 0
                    
                    for i in search:

                        try:
                            namesleft = []
                            namesright = []
                            
                            popularitysleft = []
                            popularitysright = []

                            posterpathsleft = []
                            posterpathsright = []

                            setrange += 1
                            countResults()
                            
                            # It doesn't matter what value setrange will have,
                            # if there is no result, it will not show anything,
                            # if there is only one result only one portrait will show
                            # and vice versa
                            
                            if (setrange % 2) == 0:
                                namesleft.append(i.name)
                                popularitysleft.append(i.popularity)
                                posterpathsleft.append(i.profile_path)
                                
                            else:
                                namesright.append(i.name)
                                popularitysright.append(i.popularity)
                                posterpathsright.append(i.profile_path)
                            
                            # if the setrange is either a 0 or 1, this
                            # block of code will be run, displaying the single result immediately
                            # instead of the usual for loop, which makes no sense given that theres only one item
                            if setrange >= 0:
                                panelofcontent = customtkinter.CTkFrame(contentcontainer, fg_color = "white", width = 637, height = 432)
                                
                                panelofcontent.grid(row = rowno, column = 0, pady = 5)
                                panelofcontent.grid_propagate(0)

                                panelforcolumnl = customtkinter.CTkFrame(panelofcontent, fg_color = "white", width = 320, height = 300)
                                panelforcolumnl.pack(side = "left", fill = "both")
                                panelforcolumnl.pack_propagate(0)
                                
                                
                                loadImage2(panelforcolumnl, i.profile_path)
                                
                                names = customtkinter.CTkLabel(panelforcolumnl, text = f"{i.name}", font = bodystyle,
                                                               text_color = "black")
                                names.pack(side = "top")
                                
                                    
                                popularity = customtkinter.CTkLabel(panelforcolumnl, text = f"{i.popularity}%", font = movietitlestyle,
                                                               text_color = "#071320")
                                popularity.pack(side = "top")
                                
                                panelforcolumnr= customtkinter.CTkFrame(contentcontainer, fg_color = "white", width = 320, height = 300)
                                panelforcolumnr.pack(side = "left", fill = "both")
                                panelforcolumnr.pack_propagate(0)
                                
                                break

                            # if setrange is not an even number, the setrange will be given a modus operandi
                            # answer, ensuring that the variable can still be used to run the display functions
                            if (setrange % 2) == 0:
                                setrange /= 2
                                
                            else:
                                setrange %= 2
                            
                            if setrange > 1:
                                setrange = int(setrange)
                                
                                lengthleft = 0
                                lengthright = 0
                            
                                for i in range(setrange):
        
                                    actorResultsLeft(contentcontainer, rowno, namesleft, namesright, popularitysleft, 
                                                     popularitysright, posterpathsleft, posterpathsright, lengthleft,
                                                     lengthright)
                                    rowno += 1
                                    lengthleft += 1
                                    lengthright += 1
                        
                        # If nothing is found the results are stated as 0
                        except AttributeError or TypeError:
                            resultscount.configure(text = f"{(str(0))} RESULTS AVAILABLE")
                            
                            break
                    break
            break
        

# To toggle off the different combobox options available
def removeWidget(widget):
    widget.grid_remove()

# To toggle on the different combobox options available, by packing them to the contentcontainer again
def addWidget(widget):
    widget.grid(row = 1, column = 0, padx = 30, pady = 10, sticky = 'w')

# To always update the number of available search results
def countResults():
    
    # obtains the existing variable 'count' to replace it with the incremented value
    curr_count_value = count.get()
    updated_integer_value = curr_count_value + 1
    count.set(updated_integer_value)
    
    if count.get() == 1:
        resultscount.configure(text = f"{str(count.get())} RESULT AVAILABLE")
        
    else:
        resultscount.configure(text = f"{str(count.get())} RESULTS AVAILABLE")
    
# Function to switch between popular tv shows or movies, trending or newly released
def comboboxswitch(useroption):
    
    # 'movie' and 'popular' are classes instantiated outside of this function
    # to access the wrapper library, but are not acknowledged here for some reason
    # so they are made into global variables
    global decider, chosen, movie, popular, poster_path
    
    decider = useroption
    # This variable is useful when packing the frames into rows, its 2 because
    # the 0, 1 rows are taken by the resultscount widget and the comboboxes
    rowno = 2
    
    count.set(0)

    # The decider is the value given to the parameter 'useroption' when one of the options of the combobox
    # are pressed, chosen is the 'filter' assigned when pressing one of the buttons on the side panel
    if decider == "Movies" and chosen == "Trending":
        
        popular = movie.popular()
                
        for p in popular:
            
            poster_path = p.poster_path
            title = p.title
            release_date = p.release_date
            overview_info = p.overview
            id_names = p.genre_ids

            trendingResults(contentcontainer, rowno, title, release_date, overview_info, poster_path, id_names, decider)
            rowno += 1
            countResults()
            
    elif decider == "TV Shows" and chosen == "Trending":

        popular = tv.popular()
        
        for p in popular:
            
            poster_path = p.poster_path
            title = p.name
            release_date = p.first_air_date
            overview_info = p.overview
            id_names = p.genre_ids
            
            trendingResults(contentcontainer, rowno, title, release_date, overview_info, poster_path, id_names, decider)
            rowno += 1
            countResults()
    
    
    elif decider == "Movies" and chosen == "NewReleases":
        movie = discover.discover_movies({
            'primary_release_date.gte': '2024-01-01',
            'primary_release_date.lte': '2025-01-31'})
        
        for i in movie:
            
            poster_path = i.poster_path
            title = i.title
            release_date = i.release_date
            overview_info = i.overview
            id_names = i.genre_ids

            trendingResults(contentcontainer, rowno, title, release_date, overview_info, poster_path, id_names, decider)
            rowno += 1
            countResults()
        
    elif decider == "TV Shows" and chosen == "NewReleases":
        show = discover.discover_tv_shows({
            'primary_release_date.gte': '2024-01-01',
            'primary_release_date.lte': '2025-01-31'})
        
        for i in show:
            
            poster_path = i.poster_path
            title = i.name
            release_date = i.first_air_date
            overview_info = i.overview
            id_names = i.genre_ids
           
            trendingResults(contentcontainer, rowno, title, release_date, overview_info, poster_path, id_names, decider)
            rowno += 1
            countResults()
        
    return decider, count

# Function that switches genres between movies, it has different genres from tv so it is a separate function
def comboboxswitch2(useroption):
    # Functions available from an external python file called 'MovieTVGenres'
    genreid = mtv.returnGenreID(useroption, mtv.moviegenres)
    rowno = 2
    decider = "Movies"
    
    count.set(0)
    
    
    movies = discover.discover_movies({
        'with_genres': genreid,
        'sort_by': 'popularity.desc',
    })
    
    for i in movies:
        
        poster_path = i.poster_path
        title = i.title
        release_date = i.release_date
        overview_info = i.overview
        moviegenres = i.genre_ids
        
        trendingResults(contentcontainer, rowno, title, release_date, overview_info, poster_path, moviegenres, decider)
        rowno +=1
        countResults()
        
# Function that switches genres between tv shows, it has different genres from movie so it is a separate function
def comboboxswitch3(useroption):
    
    genreid = mtv.returnGenreID(useroption, mtv.tvshowgenres)
    rowno = 2

    decider = "TV Shows"
    
    count.set(0)
    
    
    show = discover.discover_tv_shows({
        'with_genres': genreid,
        'sort_by': 'popularity.desc',
    })
    
    for i in show:
        
        poster_path = i.poster_path
        title = i.name
        release_date = i.first_air_date
        overview_info = i.overview
        tvgenres = i.genre_ids
 
        trendingResults(contentcontainer, rowno, title, release_date, overview_info, poster_path, tvgenres, decider)
        rowno += 1
        countResults()
        
# Function to display the left column of actors
def actorResultsLeft(frame, rowno, namesl, namesr, popularityl, popularityr, postpathl, postpathr, ll, lr):

    panelofcontent = customtkinter.CTkFrame(frame, fg_color = "white", width = 637, height = 432)
    
    panelofcontent.grid(row = rowno, column = 0, pady = 5)
    panelofcontent.grid_propagate(0)

    panelforcolumnl = customtkinter.CTkFrame(panelofcontent, fg_color = "white", width = 320, height = 300)
    panelforcolumnl.pack(side = "left", fill = "both")
    panelforcolumnl.pack_propagate(0)
    
    
    loadImage2(panelforcolumnl, postpathl[ll])
    
    names = customtkinter.CTkLabel(panelforcolumnl, text = f"{namesl[ll]}", font = bodystyle,
                                   text_color = "black")
    names.pack(side = "top")
    
        
    popularity = customtkinter.CTkLabel(panelforcolumnl, text = f"{popularityl[ll]}%", font = movietitlestyle,
                                   text_color = "#071320")
    popularity.pack(side = "top")
    
    actorResultsRight(panelofcontent, rowno, namesr, popularityr, postpathr, lr)

# Function to display the right column of actors, runs alongside the actorResultsLeft function
def actorResultsRight(frame, rowno, namesr, popularityr, postpathr, lr):

    panelforcolumnr = customtkinter.CTkFrame(frame, fg_color = "white", width = 320, height = 300)
    panelforcolumnr.pack(side = "left", fill = "both")
    panelforcolumnr.pack_propagate(0)
    
    loadImage2(panelforcolumnr, postpathr[lr])
    
    names = customtkinter.CTkLabel(panelforcolumnr, text = f"{namesr[lr]}", font = bodystyle,
                                   text_color = "black")
    names.pack(side = "top")
    
        
    popularity = customtkinter.CTkLabel(panelforcolumnr, text = f"{popularityr[lr]}%", font = movietitlestyle,
                                   text_color = "#071320")
    popularity.pack(side = "top")

# Function focused on loading images by obtaining a base url then the unique paths
# of each movie or show
def loadImage(frame, imagepath):

    
    # change the url constantly, instantiate the image_url by adding the url widths/heights, then
    # add it with the variable image
    image_url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/" + imagepath
    
    # image response uses the requests.get() function to obtain data provided by the link
    image_response = requests.get(image_url)
    
    # the number 200 means that the response from the online site being accessed was a success
    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((280,420))
        image = ImageTk.PhotoImage(image)
        image_label = Label(frame, image=image)
        image_label.image = image
        image_label.pack(side = "top", pady = (28,24), padx = (14,0))


# This repeated function focuses on providing images that are for the actor portraits.
# There are changes like the image_url link, padding and resizing so its faster to repeat some code
def loadImage2(frame, imagepath):
    
    image_url = "https://image.tmdb.org/t/p/w235_and_h235_bestv2/" + imagepath
    
    image_response = requests.get(image_url)
    
    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((235,245))
        image = ImageTk.PhotoImage(image)
        image_label = Label(frame, image=image)
        image_label.image = image
        image_label.pack(side = "top", pady = (10,24))


# trendingResults is more or less showing the most popular movie/tv show and displaying them
# in the contentcontainer. This function has been called a lot because it has very reusable functionality
def trendingResults(frame, rowno, title, releasedate, overview, imagepath, idnames, decider):
    
    imagetoload = imagepath

    panelofcontent = customtkinter.CTkFrame(frame, fg_color = "white",
                                          width = 637, height = 432)
    
    panelofcontent.grid(row = rowno, column = 0, padx = (10,5), pady = 5)
    panelofcontent.grid_propagate(0) 
    
    panelfortext = customtkinter.CTkFrame(panelofcontent, fg_color = "white", width = 322, height = 330,
                                          corner_radius = 0)
    panelfortext.pack(side = "right", fill = "both", pady = 24, padx = (0, 20))
    panelfortext.pack_propagate(0)

    loadImage(panelofcontent, imagetoload)
    
    title = customtkinter.CTkLabel(panelofcontent, text = f"{title} ({releasedate})", font = movietitlestyle,
                                   wraplength = 150)
    title.pack(side = "top", padx = (14,0))
    
    overviewtitle = customtkinter.CTkLabel(panelfortext, text = "Overview", font = movietitlestyle)
    overviewtitle.pack(side = "top")
    
    genres = ""

    if decider == "Movies":
        for i in idnames:
            genres = genres + ", " + (mtv.returnGenre(i, mtv.moviegenres))
    
    elif decider == "TV Shows":
        for i in idnames:
            genres = genres + ", " + (mtv.returnGenre(i, mtv.tvshowgenres))

    genres = genres[2:]
    
    details = customtkinter.CTkLabel(panelfortext, text = f"{genres}").pack(side = "top")
    overview = customtkinter.CTkLabel(panelfortext, text = f"""{overview}""", 
                                      font = ("Montserrat", 16), 
                                      justify = "left", wraplength= 300)
    overview.pack(padx = 10, pady = 10, anchor = "ne")
    
    return rowno


# findChoice acts as a sort of manager for directing functions that are specific to their purpose.
# When the user presses a button like "Trending", there are certain functions that are only allowed to run
# for the 'Trending' choice
def findChoice(choice,widget):
    
    global decider, chosen
    
    chosen = choice
    setrange = 0
    count.set(0)
    
    if chosen == "Trending":
        homeMenu()
        removeWidget(widget = combobox2)
        removeWidget(widget = combobox3)
        addWidget(widget = combobox) 
        comboboxswitch(useroption = "Movies")
        
    elif chosen == "NewReleases":
        homeMenu()
        removeWidget(widget = combobox2)
        removeWidget(widget = combobox3)
        addWidget(widget = combobox) 
        comboboxswitch(useroption = "Movies")
    
    elif chosen == "Movies":
        homeMenu()
        removeWidget(widget = combobox)
        removeWidget(widget = combobox3)
        addWidget(widget = combobox2)
        comboboxswitch2(useroption = "Action")
    
    elif chosen == "TVShows":
        homeMenu()
        removeWidget(widget = combobox)
        removeWidget(widget = combobox2)
        addWidget(widget = combobox3)
        comboboxswitch3(useroption = "Action & Adventure")

    elif chosen == "Actors":
    # Actor details are split into two lists consecutively because the layout
    # is special, requiring data to be displayed in two columns
        homeMenu()
        
        rowno = 2

        results = person.popular()
        namesleft = []
        namesright = []
        
        popularitysleft = []
        popularitysright = []

        posterpathsleft = []
        posterpathsright = []
        
        # For every even index in a loop, the person's details attached to it
        # are added to the left lists, the rest are in the right lists
        for i in results:

            setrange += 1
            countResults()
            
            if (setrange % 2) == 0:
                namesleft.append(i.name)
                popularitysleft.append(i.popularity)
                posterpathsleft.append(i.profile_path)
                
            else:
                namesright.append(i.name)
                popularitysright.append(i.popularity)
                posterpathsright.append(i.profile_path)
        
        if (setrange % 2) == 0:
            setrange /= 2
        
        else:
            setrange %= 2
        setrange = int(setrange)
        
        lengthleft = 0
        lengthright = 0

        for i in range(setrange):
            actorResultsLeft(contentcontainer, rowno, namesleft, namesright, popularitysleft, 
                             popularitysright, posterpathsleft, posterpathsright, lengthleft,
                             lengthright)
            # increment rowno for grid placement and index numbers to parse through the lists
            rowno += 1
            lengthleft += 1
            lengthright += 1
        
# Main Window
app.geometry("860x700")
app.title("The Movie Database Application")
app.configure(fg_color = "#071320")
app.resizable(0,0)

mainMenu()

app.mainloop()
