```python
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
```

- `urlopen` retrieves the html. To actually be able to read its content you need the `read()` method. Otherwise you get an HTTPResponse object like `<http.client.HTTPResponse object at 0x10d9e8670>`

- `BeautifulSoup()`takes the content to be parsed (file type or whatever) and then a parser (there are other parsers available, for example, an xml parser). It returns a BeautifulSoup object, which is a tree like object. 

- `lxml` is another parser, `html5lib` another one. They're both a little more forgiving with messy html, but they depend on external C librairies.

## Error handling

### Http errors
There are really two types of errors you can get while requesting a url (there are more, obviously, but we'll deal with more specific cases later): 400 page not found, 500 server error

So you need `try except` blocks to catch errors. With `urllib`, you have to import `HTTPError` and `URLError` from `urllib.error`

### Html errors
Then you can also encounter errors due to unexisting tag retrieval, or due difficulty retrieving the content of a tag (in which case BS would return a `None` object).
For unexisting tags, it's just a matter a catching the `AttributeError`, since you're trying to access some undefined property. 
For the `None` object, well, you just have to check for it. 

If code follows your `try-except` block, the program will carry on running, since Python was just told to handle the error. 