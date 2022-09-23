# Learnings

## BeatifulSoup

### Parse html data

```python
from bs4 import BeautifulSoup

with open("./website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# Print title tag
print(soup.title)
# Print tag name i.e. title
print(soup.title.name)
# Prints text enclosed by the title tax
print(soup.title.string)
# Print all parsed HTML
print(soup)
# Print all parsed HTML in a prettier format
print(soup.prettify())
```

### Parse links

```python
all_anchor_tags = soup.find_all("a")
for tag in all_anchor_tags:
    print(f"{tag.getText()} - {tag.get('href')}")
```

### Parse paragraphs

```python
all_paragrafs = soup.find_all("p")
```

### Parse by tag name and tag id

```python
heading = soup.find(name="h1", id="name")
print(heading)
```

### Parse by tag name and class

```python
section_heading = soup.find(name="h3", class_="heading")  # class_ just because class is reserved in python
```

### Parse by css selectors

```python
company_url = soup.select_one(selector="p a")  # CSS selector. p a {}
```

### Parse by id

```python
name = soup.select_one("#name")
print(name)
```

### Parse by class

```python
headings = soup.select(".heading")
print(heading)
```

### Parse live data from URL

```python
response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(name="h3", class_="title")
```
