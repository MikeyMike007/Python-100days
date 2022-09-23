from bs4 import BeautifulSoup

with open("./website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup)
print(soup.prettify())

# Search for links - gets all links in a list
all_anchor_tags = soup.find_all("a")
all_paragrafs = soup.find_all("p")
print(all_anchor_tags)
print(all_paragrafs)


for tag in all_anchor_tags:
    print(tag)  # List of tags

print("-------------")

for tag in all_anchor_tags:
    print(f"{tag.getText()} - {tag.get('href')}")  # Name of website - Link

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(
    name="h3", class_="heading"
)  # class_ just because class is reserved in python

print(section_heading)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")  # CSS selector. p a {}
print(company_url)

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(heading)
