# import modules-----------
import urllib
import bs4
import re
# open and get site------------------
url = input("Please input azlyrics from which to scrape: ")# get url
contentSite = urllib.request.urlopen(url) #get site
contentSoup = bs4.BeautifulSoup(contentSite, "html.parser") # parse site
# scrape lyrics------------------
# Lyrics in div element without class=============
contentLyrics = contentSoup.find_all("div", attrs = {"class":None})
# extract text from lyrics=============
unformattedLyrics = []
for i in contentLyrics[1]:
    if "<" or ">" not in i:
        unformattedLyrics.append(i)
    elif "<" or ">" in i:
        continue
# removing the <br/> from the end of the lyrics
for i in range(len(unformattedLyrics)):
    if "<br/>" in unformattedLyrics[i]:
        unformattedLyrics[i] = unformattedLyrics[i].replace("<br/>", "")
    else:
        continue
# removing the first line (disclaimer) from the lyrics
unformattedLyrics = unformattedLyrics[2:]
removing the '<br/>' occurences from the file
finalLyrics = []
for i in unformattedLyrics:
    if not isinstance(i, bs4.element.Tag):
        finalLyrics.append(i)
    else:
        continue
# writing lyrics to a file------------
fileName = input("To what file would like to the write the lyrics to? ")
try:
    with open(fileName + ".txt", "w") as lyricsFile:
        for i in finalLyrics:
            print(i, file = lyricsFile)
except IOError as ioerr:
    print("Error opening file: " + str(ioerr))
