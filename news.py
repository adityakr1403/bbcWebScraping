from bs4 import BeautifulSoup
import http.client

host = "www.bbc.com"
path = "/news"

connection = http.client.HTTPSConnection(host)
connection.request("GET", path)
response = connection.getresponse()
print(response.status, response.reason)
data = response.read()
soup = BeautifulSoup(data, 'html.parser')

news_List = soup.find_all('a', class_='exn3ah91')
# result = []
# for news in news_List:
#     result.append((news['href'], news.text))

result = [(news['href'], news.text) for news in news_List]

filtered_result = [item for item in result if not item[0].startswith("https://")]
for links in filtered_result:
    print(links[0], "-->", links[1])
