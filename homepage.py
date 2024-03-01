from bs4 import BeautifulSoup
import http.client

connection = http.client.HTTPSConnection("www.bbc.com")
connection.request("GET", "/")
response = connection.getresponse()
print(response.status, response.reason)
data = response.read()
soup = BeautifulSoup(data, 'html.parser')

# news section
module_news_section = soup.find('section', class_='module--news')
news_list = module_news_section.find_all('li')
for news in news_list:
    print(news.a['href'], news.a.text)

# sport section
module_sport_section = soup.find('section', class_='module--sport')
sport_list = module_sport_section.find_all('li')
for sport in sport_list:
    print(sport.a['href'], sport.a.text)