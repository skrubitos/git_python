import urllib.request as urreq
import urllib.parse as urparse # provides functions for parsing and manipulating URLs
import re  #regular expressions

url='https://pythonprogramming.net/'
values={'s': 'basics',
        'submit':'search'}

#It is used to encode a set of query parameters as a URL query string.
data=urparse.urlencode(values)

# utf-8 is character encoding for the Web
data=data.encode('utf-8')

#we send request to the page
req=urreq.Request(url,data)

#if the request is succesfull we open page
resp=urreq.urlopen(req)
#program reads the page
respData=resp.read()

# reg express, raw material trazimo od paragrafa do kraja paragrafa,
#.= sve osin \n, *=match 0 or more, ?= mtch 0 or 1
paragraphs=re.findall(r'<p>(.*?)</p>', str(respData))
print(paragraphs)

