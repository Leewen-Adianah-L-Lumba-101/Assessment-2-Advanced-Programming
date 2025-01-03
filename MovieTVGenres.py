# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 19:44:46 2024

@author: hp
"""

tvshowgenres = { "genres": [
              {
                "id": 10759,
                "name": "Action & Adventure"
              },
              {
                "id": 16,
                "name": "Animation"
              },
              {
                "id": 35,
                "name": "Comedy"
              },
              {
                "id": 80,
                "name": "Crime"
              },
              {
                "id": 99,
                "name": "Documentary"
              },
              {
                "id": 18,
                "name": "Drama"
              },
              {
                "id": 10751,
                "name": "Family"
              },
              {
                "id": 10762,
                "name": "Kids"
              },
              {
                "id": 9648,
                "name": "Mystery"
              },
              {
                "id": 10763,
                "name": "News"
              },
              {
                "id": 10764,
                "name": "Reality"
              },
              {
                "id": 10765,
                "name": "Sci-Fi & Fantasy"
              },
              {
                "id": 10766,
                "name": "Soap"
              },
              {
                "id": 10767,
                "name": "Talk"
              },
              {
                "id": 10768,
                "name": "War & Politics"
              },
              {
                "id": 37,
                "name": "Western"
              }
            ]
         }


moviegenres = { "genres": [
              {
                "id": 28,
                "name": "Action"
              },
              {
                "id": 12,
                "name": "Adventure"
              },
              {
                "id": 16,
                "name": "Animation"
              },
              {
                "id": 35,
                "name": "Comedy"
              },
              {
                "id": 80,
                "name": "Crime"
              },
              {
                "id": 99,
                "name": "Documentary"
              },
              {
                "id": 18,
                "name": "Drama"
              },
              {
                "id": 10751,
                "name": "Family"
              },
              {
                "id": 14,
                "name": "Fantasy"
              },
              {
                "id": 36,
                "name": "History"
              },
              {
                "id": 27,
                "name": "Horror"
              },
              {
                "id": 10402,
                "name": "Music"
              },
              {
                "id": 9648,
                "name": "Mystery"
              },
              {
                "id": 10749,
                "name": "Romance"
              },
              {
                "id": 878,
                "name": "Science Fiction"
              },
              {
                "id": 10770,
                "name": "TV Movie"
              },
              {
                "id": 53,
                "name": "Thriller"
              },
              {
                "id": 10752,
                "name": "War"
              },
              {
                "id": 37,
                "name": "Western"
              }
            ]
         }

# listofids = [18, 10752, 36]

def returnGenre(idno, typeofmedia):
    # For debugging
    # ids = []
    # names = []

    # Finding a way to parse through the information 
    for key, val in typeofmedia.items():
        for i in val:
            # ids.append(i['id'])
            # names.append(i['name'])
            
            if idno in i.values():
                genrename = (i['name'])

    return genrename


def returnGenreID(name, typeofmedia):

    for key, val in typeofmedia.items():
        for i in val:
            
            if name in i.values():
                genreid = i['id']
                
    return genreid


def returnAllGenres(typeofmedia):
    
    genres = []
    
    for key, val in typeofmedia.items():
        for i in val:
            genres.append(i['name'])
            
    return genres



# mgenres = returnAllGenres(moviegenres)
# print(mgenres[0])

# finalstring = ""

# for i in listofids:
#     finalstring = finalstring + ", " + (returnGenre(i, moviegenres))

# finalstring = finalstring[2:]
# print(finalstring)
                                 
                

    
