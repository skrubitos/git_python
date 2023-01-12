import pandas as pd
import requests
from bs4 import BeautifulSoup
listofjobs= []
def ime_kompanije(url): #ulazimo u link kompanije te kopiramo ime te firme
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
#url ce biti procesuiran kroz funkciju
    r=requests.get(url,headers)
    soup= BeautifulSoup(r.content, "html.parser")
    job_company = soup.find('li', class_='job-company')
    company_name = job_company.text
    return (company_name)

def extract (page):     #ulazimo u stranicu moj-posao.net
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    url= f"https://www.moj-posao.net/Pretraga-Poslova/?searchWord=&keyword=&job_title=&job_title_id=&skill=&skill_id=&area=&category=11&page3=&page={page}"
    r=requests.get(url,headers)
    soup= BeautifulSoup(r.content, "html.parser")
    return soup

def transform (soup): #trazimo podatke
    divs=soup.find_all("div", class_ = "job-data")
    for items in divs:
        try:
            x=items.find("a")
            job_position = x.find("span", class_="job-position").text.strip()
            job_position = job_position.replace(" (m/ž)", "").replace(" (m/f)", "").replace("(f/m)", "").replace("(w/m/x)","").replace("(d/m/f)","")
            trans_table = str.maketrans("ČŠĆĐŽčšćđž", "CSCDZcscdz")
            job_position = job_position.translate(trans_table)


            print("Job position:", job_position)
            job_link=x.get("href")

            print("Company :",ime_kompanije(job_link))
            job_location=x.find("span", class_ ="job-location").text
            print("Location: ",job_location)

            job_date=x.find("time", class_= "deadline").text
            print("This is the deadline:", job_date)


            print("Link: ", job_link,"\n")

            listofjobs.append({
                "Position": job_position,
                "Company":ime_kompanije(job_link),
                "Location": job_location,
                "Deadline": job_date,
                "Link" : job_link
            })
        except AttributeError:
            pass

for x in range (1,50):
    goveda=extract(x)
    transform(goveda)

print(listofjobs)

#creating csv file
jobs_df = pd.DataFrame(listofjobs)
jobs_df.to_csv('jobss.csv', index=False)
