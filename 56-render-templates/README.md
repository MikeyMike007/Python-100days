# Learnings

## Flask

### Folder structure - Flask project

```python
server.py
templates/[PUT ALL HTML TEMPLATES HERE]
static/icons/[PUT ALL ICONS HERE]
static/images/[PUT ALL IMAGES HERE]
static/stylesheets/[PUT ALL STYLESHEETS HERE]
```

You dont specifically link everything to `templates/index.html` or `static/images/image.png`, instead, flask will handle that for you automatically. The only specification you need to give is `index.html` and `images/image.png`

### Example flask app

#### ./server.py

```python
from flask import Flask, render_template

# Templates need to be inside folder ./templates
# Images and css files need to be in the ./static folder

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") # Function will look in templates folder and render index.html

if __name__ == "__main__":
    app.run(debug=True) # debug=True will automatically update server when there is changes in code
```

### ./templates/index.html

```html
<html>
  <head>
    <meta charset="UTF-8" />
    <title>My page</title>
    <!-- Please note that the stylesheet should be in the /static folder -->
    <!-- Any images need also to be in the static folder -->
    <link rel="stylesheet" href="static/styles.css" />
  </head>
  <body>
    <h1>Hello</h1>
  </body>
</html>
```

### .static/styles.css

```css
body {
  background-color: purple;
}
```

## Other

- Set following in chrome tools and you can edit the site directly in chrome `document.body.editAble = true`

- Good resource for templates: <https://html5up.net/>
