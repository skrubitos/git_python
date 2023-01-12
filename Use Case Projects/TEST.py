import pandas as pd
import requests
from bs4 import BeautifulSoup
listofjobs= []
def extract (page):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    url= f"https://www.moj-posao.net/Pretraga-Poslova/?searchWord=&keyword=&job_title=&job_title_id=&skill=&skill_id=&area=&category=11&page3=&page={page}"
    r=requests.get(url,headers)
    soup= BeautifulSoup(r.content, "html.parser")
    return soup

def transform (soup):
    divs=soup.find_all("div", class_ = "job-data")
    for items in divs:
        try:
            x=items.find("a")
            job_position = x.find("span", class_="job-position").text.strip()
            print("This is the job position:", job_position)
            job_location=x.find("span", class_ ="job-location").text
            print("Location:",job_location)
            job_date=x.find("time", class_= "deadline").text
            print("This is the deadline:", job_date)
            job_link=x.get("href")
            print(job_link)
            listofjobs.append({
                "Position": job_position,
                "Location": job_location,
                "Deadline": job_date,
                "Link" : job_link
            })
        except AttributeError:
            pass

for x in range (1,50):
    goveda=extract(x)
    transform(goveda)


print("alooo",listofjobs)

jobs_df = pd.DataFrame(listofjobs)
jobs_df.to_csv('jobs.csv', index=False)
