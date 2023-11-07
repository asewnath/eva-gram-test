# eva-gram-test

Extracting div/script from html files using BeautifulSoup:

```
from bs4 import BeautifulSoup

html_file = 'test.html'
with open(html_file, 'r') as f:
    bokeh_html = f.read()

soup = BeautifulSoup(bokeh_html, 'html.parser')
div = soup.find_all('div')[0]
script = soup.find_all('script')[0]
```
