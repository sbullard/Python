import urllib
import re

urls = ["http://google.com","http://nytimes.com","http://cnn.com"]
regex = '<title>(.+?)</title>' #gets the text between title tags
pattern = re.compile(regex)

i=0
while i < len(urls):
    htmlfile = urllib.urlopen(urls[i]) #connects to url
    htmltext = htmlfile.read() #reads the html from the connected url
    titles = re.findall(pattern,htmltext) #scrapes the titles of the sites
    
   
    print titles    
    i+=1


