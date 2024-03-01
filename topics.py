from bs4 import BeautifulSoup
import http.client

host = "www.bbc.com"
path = "/news"
topic = "/science_and_environment"
page = 1

connection = http.client.HTTPSConnection(host)
connection.request("GET", path + topic + "?page=" + str(page))
response = connection.getresponse()
print(response.status, response.reason)
data = response.read()
soup = BeautifulSoup(data, 'html.parser')
total_pages = int(str(soup.find_all('li', class_='e1ksme8n1')[-1].text))

print(total_pages)
final_list = []
print("Loading...")
for page_no in range(1, total_pages + 1):
    connection.request("GET", path + topic + "?page=" + str(page_no))
    response = connection.getresponse()
    data = response.read()
    soup = BeautifulSoup(data, 'html.parser')
    try:
        news_List = soup.find_all('a', class_='exn3ah91')
        news_List2 = soup.find_all('a', class_='ej9ium92')
        page_list = [(news['href'], news.find_all('span', class_='ej9ium94')[-1].text, page_no) for news in
                     (news_List + news_List2) if
                     (news is not None) and not news['href'].startswith("https://")]
        final_list.extend(page_list)
    except Exception as e:
        print(e)
print("Done!")
print("Total Links: ", len(final_list))
# for links in final_list:
#     print(links[0], "-->", links[1])

f = open("links.txt", "w", encoding='utf-8')
for links in final_list:
    f.write(links[0] + "-->" + links[1] + "-->" + str(links[2]) + "\n")
f.close()
