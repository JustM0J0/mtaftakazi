# A Simple Program to find Jobs in Zoom Tanzania (Created on 11/4/2021)

from bs4 import BeautifulSoup
import requests

#Get the website information

html_text = requests.get("https://www.zoomtanzania.com/jobs").text
soup = BeautifulSoup(html_text, 'lxml')

#Get a list of all available Jobs

jobs = soup.find('div', class_ = 'listings-cards__list')

#Split the Jobs according to title, location, deadline of application and a link to a more detailed information

for job in jobs:
    try:
        job_title = job.find('div', class_ = 'listing-card__header__title')
        locations = job.find('div', class_ = "listing-card__header__location")
        deadlines = job.find('span', class_ = "listing-card__price__value")
        details = job.find('a', class_ = 'listing-card__inner', href = True)
        link_to_job = details['href']
        if None in (job_title, locations, deadlines, details):
            continue
        print(f'''
Job Title: {job_title.text.strip()}
Location: {locations.text.strip()}
Deadline: {deadlines.text.strip()}
Link: {link_to_job}''')
    except: #Throws an error thus an except block to avoid crashing the program
        pass
    
    
