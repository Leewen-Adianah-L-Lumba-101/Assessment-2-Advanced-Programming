# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:14:18 2024

@author: hp
"""

import requests
import json
import tkinter as tk

# cocktail_id = "1107"

# url = f"https://www.thecocktaildb.com/api/json/v1/1/random.php"
# response = requests.get(url)



# with open("jsonEx1.json", "w") as file:
#     json.dump(data,file,indent = 4)
# print(data["drinks"][0])
# print(data["drinks"][0]["idDrink"])


url2 = requests.get(f"https://thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
data = url2.json()

print(data)


# print(data)

# def get_cocktail_details():
#     cocktail_id = "1007"
#     url = f"www.thecocktaildb.com/api/json/v1/1/lookup.php?iid={cocktail_id}"
    
#     response = requests.get(url)
#     if 
#     data = data["drinks"][0]
    

