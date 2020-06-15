from bs4 import BeautifulSoup
import requests


def print_items(html, count):
    items = html.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1
    return count


url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
count = 1
count = print_items(soup, count)

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    newSoup = BeautifulSoup(response.text, 'lxml')
    count = print_items(newSoup, count)
