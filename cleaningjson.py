# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 22:56:46 2026

@author: vishn
"""

import pandas as pd
import re
import matplotlib.pyplot as plt

data=pd.read_json("C:\\Users\\vishn\\.spyder-py3\\laptop_scraper\\laptop.json")
def extract(rating):
    if pd.isnull(rating):
       return None
    
    match=re.search(r"rating-(\d)-(\d)",rating)
    if match:
        output=float(f"{match.group(1)}.{match.group(2)}")
        #print(output)
        return output
   
    
data["rating_clean"]=data["ratings"].apply(extract)
print(data["rating_clean"].head(10))

def clean_price(price):
    if pd.isnull(price):
        return None
    price = price.replace(",", "")
    try:
        return float(price)
    except:
        return None
data["price_clean"] = data["Total price"].apply(clean_price)
print(data['price_clean'].head(10))

print(data['price_clean'].describe())

def extract_brand(name):
    if pd.isnull(name):
        return None
    fullname= name.split()
    if len(fullname)>=2:
        return f"{fullname[0]} {fullname[1]}"
    return fullname
        

data["brand"] = data["name"].apply(extract_brand)
print(data["brand"])

data.plot.scatter(x='price_clean',y='rating_clean')
plt.show()
