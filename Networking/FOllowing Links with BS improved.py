import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')  # prompt user for starting URL

count = int(input('Enter count: ')) # prompt user for number of times to repeat
position = int(input('Enter position: ')) # prompt user for position of link to follow
print("Retrieving:",url)
# Loop through the process count number of times
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read() # read HTML from URL
    soup = BeautifulSoup(html, 'html.parser') # parse HTML
    tags = soup('a') # extract anchor tags
    print("tags",tags)
    url = tags[position - 1].get('href', None) # follow link at specified position
    print("Retrieving: ",url)
