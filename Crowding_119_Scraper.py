#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

url="https://www.njtransit.com/my-bus-to?stopID=30189&form=stopID"

try:
    driver.get(url)
except:
    print("error getting web page")

raw_rows = driver.find_elements(By.XPATH, "//div[@class='media-body']")
split_rows = [row.text.split('\n') for row in raw_rows]
filtered_rows = [b for b in split_rows if len(b)==5]


import datetime as dt
from csv import writer 
with open('NJT119_crowding.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    for row in filtered_rows:
        row.insert(0,'30189')
        row[2]=row[2].split('#')[1]
        row[3]=row[3].split(' ')[2]
        row.insert(0, str(dt.datetime.now()))
        writer_object.writerow(row)
        print (f"Added row: {row}")
    f_object.close()
