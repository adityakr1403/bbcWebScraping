from bs4 import BeautifulSoup
import http.client
import csv

host = "www.bbc.com"

news_links = []

with open("links.txt", "r") as f:
    for line in f:
        news_links.append(line.split("-->")[0])

news_list = []
connection = http.client.HTTPSConnection(host)
print("Loading...")
for idx, news in enumerate(news_links):
    connection.request("GET", news)
    response = connection.getresponse()
    data = response.read()
    soup = BeautifulSoup(data, 'html.parser')
    try:
        news_article = soup.find('article')
        title = news_article.find('h1').text
        content_divs = news_article.find_all('div', attrs={'data-component': 'text-block'})
        content_text = ""
        for div in content_divs:
            content_text += div.text + "\n"
        news_list.append((title, content_text))
        print("News ", idx, " done!")
    except Exception as e:
        print("News ", idx, " failed!")
        pass
print("Done!")
print("Total News: ", len(news_list))

with open("news_all.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for news in news_list:
        writer.writerow([news[0], news[1]])
