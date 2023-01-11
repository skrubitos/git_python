import urllib.request

import requests
from bs4 import BeautifulSoup

def extract ():
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    url= "https://www.moj-posao.net/Pretraga-Poslova/?searchWord=&keyword=&job_title=&job_title_id=&skill=&skill_id=&area=&category=11"
    r=requests.get(url,headers)
    soup= BeautifulSoup(r.content, "html.parser")
    return soup
print(extract())

def extract (soup):
    divs=soup.find_all("div", class="job-position  ")




