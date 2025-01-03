# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:55:51 2024

@author: hp
"""

# import requests
# import sys
import tmdbsimple as tmdb
from tmdbv3api import TMDb

tmdb = TMDb() # Create class instance

tmdb.api_key = 'f8da1365ead9eb420c108f560ff80670'
tmdb.language = 'en'
tmdb.debug = True

from tmdbv3api import Movie
from tmdbv3api import Person
from tmdbv3api import TV
from tmdbv3api import Discover

tv = TV()
movie = Movie()
discover = Discover()
person = Person()

# recommendations = movie.recommendations(movie_id=111)

# for recommendation in recommendations:
#     print(recommendation.title)
#     print(recommendation.overview)

# popular = tv.popular()

# for p in popular:
#     print(p.id)
#     print(p.name)
#     print(p.overview)
#     print(p.poster_path)
#     print(p.genre_ids)
# print(dir(p))
    
# replace value of with_genres with variable, that variable is the result of
# the first genre id of the tv show

# count = 0
# genreid = 18

# show = discover.discover_tv_shows({
#     'with_genres': genreid,
#     'sort_by': 'popularity.desc',
# })


# for i in show:
#     count += 1
#     print(f"{count}. {i.name}")
      

# movies = discover.discover_movies({
#     'with_genres': 18,
#     'sort_by': 'popularity.desc',
# })

# for i in movies:
#     count += 1
#     print(f"{count}. {i.title}")
    

# DONE AND DUSTED FOR MOVIE SEARCH ENGINE
count = 0

usersearch = str(input("Find your show/actor/movie: "))

search = movie.search(usersearch)

for res in search:
    try: 
        print(res.title)
        print(res.overview)
        print(res.poster_path)
        count += 1
        
    except AttributeError:
        
        print("No Movie Results")
        search = tv.search(usersearch)
        
        for i in search:
            try:
                print(i.name)
                print("results found")
                break
                
            except AttributeError:
                print("No TV Show Results")
                
                search = person.search(usersearch)
                for i in search:
                    try: 
                        print("results found")
                        
                    except AttributeError:
                        print("No Actor Results")
                        break
                break
        break

    # if res.name == None:
    #     print("No Results")
    #     break

    # # print(res.poster_path)
    # # print(res.vote_average)

# print(f"{count} RESULTS AVAILABLE")    

# m = movie.details(1359289)

# print(m.title)
# print(m.popularity)
# print(dir(m))
# print(m.overview)


#DONE AND DUSTED
# person = Person()
# search = person.search("Lou")
# count = 1

# for i in search: 
#     print(count, i.name)
#     count +=1
    
# replace details with variable
# p = person.details(12)

# highestvotecount = 0

# for i in p.images['profiles']:
    
#     if i['vote_count'] > highestvotecount:
#         highestvotecount = i['vote_count']
#         filepath = "https://image.tmdb.org/t/p/w300_and_h450_bestv2" + i['file_path']


# print(p.name)
# print(p.biography)
# print(p.birthday)
# print(p.gender)

# person = Person()
# results = person.popular()
# count = 0

# names1 = []
# names2 = []


# for i in results:
#     print(dir(i))
    
#     if (count % 2) == 0:
#         names1.append(i.name)
#     else:
        
#         names2.append(i.name)
    
        

#     # if i.gender == 2:
#         # print(i.popularity)
#         # print(i.name)
#         # print(i.profile_path)
#     count += 1
# print(count)
# print(names1)
# print("\n")
# print(names2)


#add every 2nd result to a list


    
#     else:
#         pass
    


# print(dir(person))


# print(filepath)



# popular = tv.popular()
# count = 0
# for p in popular:
#     count += 1

# print(count)


# DONE AND PARTIALLY DUSTED
# count = 1

# discover = Discover()
# movie = discover.discover_movies({
#     'primary_release_date.gte': '2024-12-01',
#     'primary_release_date.lte': '2025-01-31'
# })

# for i in movie:
#     print(f"{count}. {i.title}")
#     print(dir(i))
#     count += 1
    


# count = 1

# discover = Discover()
# show = discover.discover_tv_shows({
#     'primary_release_date.gte': '2024-12-01',
#     'primary_release_date.lte': '2025-01-31'
# })

# for i in show:
#     # print(f"{count}. {i.name}")
#     count += 1
#     print(i.genre_ids)



# print(show.results)

    

# test = [{"vote_count" : 1, "answer" : "THE NEXT BEST ALTERNATIVE"}, 
# {"vote_count" : 2, "answer" : "THE SECOND NEXT BEST ALTERNATIVE"},
# {"vote_count" : 1, "answer" : "THE THIRD NEXT BEST ALTERNATIVE"},
# {"vote_count" : 0, "answer" : "THE NEXT WORST ALTERNATIVE"}]

# real_answer = ""
# highestvote = 0

# for i in test:
#     if i['vote_count'] > highestvote:
#         highestvote = i['vote_count']
#         real_answer = i['answer']

# print(highestvote)
# print(real_answer)


     
# use this to add https://image.tmdb.org/t/p/w600_and_h900_bestv2



# tmdb.REQUESTS_TIMEOUT = 5
# movie = tmdb.Movies(609)
# response = movie.info()
# print(response)

# res = searchMovie('A New Hope')
# print(res)
# print(len(res))
# print(res[0])


# Program to Search for TV show Genres

# LIST OF TV SHOW GENRES
# tvshowgenres = { "genres": [
#               {
#                 "id": 10759,
#                 "name": "Action & Adventure"
#               },
#               {
#                 "id": 16,
#                 "name": "Animation"
#               },
#               {
#                 "id": 35,
#                 "name": "Comedy"
#               },
#               {
#                 "id": 80,
#                 "name": "Crime"
#               },
#               {
#                 "id": 99,
#                 "name": "Documentary"
#               },
#               {
#                 "id": 18,
#                 "name": "Drama"
#               },
#               {
#                 "id": 10751,
#                 "name": "Family"
#               },
#               {
#                 "id": 10762,
#                 "name": "Kids"
#               },
#               {
#                 "id": 9648,
#                 "name": "Mystery"
#               },
#               {
#                 "id": 10763,
#                 "name": "News"
#               },
#               {
#                 "id": 10764,
#                 "name": "Reality"
#               },
#               {
#                 "id": 10765,
#                 "name": "Sci-Fi & Fantasy"
#               },
#               {
#                 "id": 10766,
#                 "name": "Soap"
#               },
#               {
#                 "id": 10767,
#                 "name": "Talk"
#               },
#               {
#                 "id": 10768,
#                 "name": "War & Politics"
#               },
#               {
#                 "id": 37,
#                 "name": "Western"
#               }
#             ]
#          }


# DOOONNNE AND DUSTED! (DONT FORGET TO IMPORT DICTIONARY VALUES IN SEPARATE FILES)

# userchoice = int(input("Please enter your ID: "))


# ids = []
# names = []

# # Finding a way to parse through the information 
# for key, val in tvshowgenres.items():
#     for i in val:
#         ids.append(i['id'])
#         names.append(i['name'])
        
#         if userchoice in i.values():
#             print(i['name'])
            

# print(ids)
# print(names)

            
# VERSION 1: ID AND NAME OF GENRE ARE SEPARATE LINES
        # for key2, val2 in i.items():

        #     if userchoice == val2:
        #         print(val2)
            
        #     print("{} : {}".format(key2, val2))

        
#     print("--------------------")
    
# VERSION 2: ID AND NAME ARE IN THE SAME 'VARIABLE'
# for key, val in tvshowgenres.items():
#     for i in val:      
#         for genreinfo in i.items():
            # print(genreinfo["id"])
    #         print("{}".format(genreinfo))
    #         print("\n")
    # print("--------------------")
    
    


# LIST OF MOVIE SHOW GENRES
# {
#   "genres": [
#     {
#       "id": 28,
#       "name": "Action"
#     },
#     {
#       "id": 12,
#       "name": "Adventure"
#     },
#     {
#       "id": 16,
#       "name": "Animation"
#     },
#     {
#       "id": 35,
#       "name": "Comedy"
#     },
#     {
#       "id": 80,
#       "name": "Crime"
#     },
#     {
#       "id": 99,
#       "name": "Documentary"
#     },
#     {
#       "id": 18,
#       "name": "Drama"
#     },
#     {
#       "id": 10751,
#       "name": "Family"
#     },
#     {
#       "id": 14,
#       "name": "Fantasy"
#     },
#     {
#       "id": 36,
#       "name": "History"
#     },
#     {
#       "id": 27,
#       "name": "Horror"
#     },
#     {
#       "id": 10402,
#       "name": "Music"
#     },
#     {
#       "id": 9648,
#       "name": "Mystery"
#     },
#     {
#       "id": 10749,
#       "name": "Romance"
#     },
#     {
#       "id": 878,
#       "name": "Science Fiction"
#     },
#     {
#       "id": 10770,
#       "name": "TV Movie"
#     },
#     {
#       "id": 53,
#       "name": "Thriller"
#     },
#     {
#       "id": 10752,
#       "name": "War"
#     },
#     {
#       "id": 37,
#       "name": "Western"
#     }
#   ]
# }