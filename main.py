import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data_file = response.text
soup = BeautifulSoup(data_file, "html.parser")
articles = soup.find_all(class_ = "title",name="h3")
articles.title =[]
for name in articles:
    titles = name.getText()
    articles.title.append(titles)
print(articles.title)
movies =  articles.title[::-1]

with open("movies.txt", mode ="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")