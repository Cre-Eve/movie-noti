import requests
from bs4 import BeautifulSoup

# how to use crawling

# CGV 유성노은

url = 'http://www.cgv.co.kr/theaters/?areacode=03%2C205&theaterCode=0206&date=20221116'
html = requests.get(url)

#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

title_list = soup.select('div.info-movie')

for i in title_list:
    print(i.select_one('a > strong').text.strip())