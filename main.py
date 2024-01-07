# importing required libraries
from bs4 import BeautifulSoup
import requests

# beautiful soup can pull data out of HTML and XML files
# it needs the request library to make requests and requires the use of an external parser

# it has 3 steps
# 1. Fetch the page
# 2. Get page content
# 3. Create the soup

# finding stuff in from the soup
# id:    soup.find("specific-id")
# class: soup.find('tag', class_="specific-class")
# tag:   soup.find('tag')    OR    soup.find_all('tag')

# find() returns an element, find_all() returns a list

# --------------------------------------------------------------------------------------------------
# scraping the website url "https://subslikescript.com/movie/Titanic-120338"

# 1. Fetch the page
website = "https://subslikescript.com/movie/Titanic-120338"
result = requests.get(website)

# 2. Get page content
content = result.text

# 3. Create the soup
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# --------------------------------------------------------------------------------------------------
# how to scrape a single page

# finding a single element
# getting the first h1 tag content from the article tag having the classname 'main-article'
box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()
# print(title)

print("--------------------------------------------------------------------")

# getting the transcript from a div with classname 'full-script'
# strip removes leading and trailing spaces
# separator=' ' replaces end line character with ' '(space)
transcript = soup.find('div', class_='full-script').get_text(strip=True, separator=' ')
# print(transcript)

# --------------------------------------------------------------------------------------------------
# writing data to a txt file

# python's version of String Literal (called f-string)
with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)
