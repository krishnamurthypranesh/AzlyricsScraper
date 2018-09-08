# import modules-----------
import urllib
import bs4
import re
# open and get site------------------

# get url
url = input("Please input azlyrics from which to scrape: ")
# getting site
try:
    contentSite = urllib.request.urlopen(url) #get site
except urllib.error.HTTPError as urlHttpErr:
    print("Error retrieving page! Error Code: " + str(urlHttpErr))
except urllib.error.URLError as urlErr:
    print("Ran into a problem while retrieving page! Error Code: " +
            str(urlErr))
except:
    print("Error!")
# parse site
contentSoup = bs4.BeautifulSoup(contentSite, "html.parser")

# scrape lyrics------------------

# Lyrics in div element without class
contentLyrics = contentSoup.find_all("div", attrs = {"class":None})

# extract text from lyrics=============
unformattedLyrics = []
for i in contentLyrics[1]:
    if "<" or ">" not in i:
        unformattedLyrics.append(i)
    elif "<" or ">" in i:
        continue

# removing the <br/> from the end of the lyrics=============
for i in range(len(unformattedLyrics)):
    if "<br/>" in unformattedLyrics[i]:
        unformattedLyrics[i] = unformattedLyrics[i].replace("<br/>", "")
    else:
        continue
# removing the first line (disclaimer) from the lyrics
unformattedLyrics = unformattedLyrics[2:]

# removing the '<br/>' occurences from the file=============
finalLyrics = [i if not isinstance(i, bs4.element.Tag) else "" for i in unformattedLyrics]

# writing lyrics to a file------------

# get file name from user
fileName = input("To what file would like to the write the lyrics to? ")
try:
    with open(fileName + ".txt", "w") as lyricsFile:
        for i in finalLyrics:
            print(i, file = lyricsFile)
except IOError as ioerr:
    print("Error opening file: " + str(ioerr))
