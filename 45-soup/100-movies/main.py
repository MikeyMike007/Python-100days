import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(name="h3", class_="title")

movies = [title.getText() for title in titles]


with open("movies.txt", "w") as file:
    file.write("\n".join(movies[::-1]))  # Reverse the list
