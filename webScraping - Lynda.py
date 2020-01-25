import requests
from bs4 import BeautifulSoup
import lxml


# url = 'http://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_ ='author')
# tags = soup.find_all('div', class_ ='tags')
# for i in range (len(quotes)):
#     print (quotes[i].text)
#     print (authors[i].text)
#     quoteTags = tags[i].find_all('a', class_ ='tag')
#     for quoteTag in quoteTags:
#         print quoteTag.text


"""Example from Sraping club for scraping data where items are present in form of pages"""

url2 = 'https://scrapingclub.com/exercise/list_basic/?page=2/'
response2 = requests.get(url2)
soup = BeautifulSoup(response2.text, 'lxml')
items = soup.find_all('div', class_ ='col-lg-4 col-md-6 mb-4')
ctr = 1
for item in items:
    print ('%s) Item name: %s, Price: %s'%(ctr+1, item.find('h4', class_ ='card-title').text.strip('\n'), item.find('h5').text))
    ctr += 1

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_ ='page-link')
ctr = 1
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum!= None:
        x = link.get('href')
        newUrl2 = 'https://scrapingclub.com/exercise/list_basic/?page=2/' + x
        response2 = requests.get(url2)
        soup = BeautifulSoup(response2.text, 'lxml')
        items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

        for item in items:
            print ('%s) Item name: %s, Price: %s' % (
            ctr + 1, item.find('h4', class_='card-title').text.strip('\n'), item.find('h5').text))
            ctr += 1
