from basicScraper import getTitle

url = 'http://www.pythonscaping.com/pages/page1.html'

title = getTitle(url)

if title == None:
    print("Title is non existant")
else:
    print(title)

