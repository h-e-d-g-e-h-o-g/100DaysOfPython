# Now, we are going to learn about web scraping.
# But first, we need to understand why do we need web scraping.
# As, until now, we are learning about APIs. With the help of API, we can work with the data of other websites.
# But what if, website does not have API to work with or The API is not helpful.
# We can scrap that website where our goal is to look through the underlying html code to get hold of the info that we want.
# To get hold of the information, you need html parser.
# That parser is BeautifulSoup, beautiful soup is a library that helps the developers to scrap(extract) the data from html or xml files.
# First step is to parse the html file, (means hold of the information that we want).
# HTML and XML both are structured languages, used to structure data in a file using tags.
from bs4 import BeautifulSoup


with open("website.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
# Here, we are creating soup, an object of BeautifulSoup class, we need to pass the content(information that we want), and
# parser to specify in which structured language, it is in.

# Sometimes, html.parser will not work for some websites in that case, you need to use different parser such as lxml.
# First, you need to import lxml.

# With the help of soup object, you can tap into the different part of html document using python code.
#print(soup.title)
# You can tap into the title tag of html document.
#print(soup.title.name)
# You can tap into the name of the title tag i.e. title
#print(soup.title.string)
# You can tap into the actual text inside the title tag.
# Overall, the soup object represents the html code.
# You can print the soup object and use prettify() on soup to print the html code with correct identation.

# Now, you can see that you can hold only one element at one time such as holding p tag or a tag.
# What if, you want to hold all the p tags or a tags at once.
# In that case, you need to use find_all() of beautiful soup. We can search tags by names.
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# It will return me the list of all the anchor tags.
# Now, what if, I need to hold all the text inside the anchor tags.
# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
# getText() returns the string inside the html element.
# with the help of get(), you can get the value of any of the attributes. Just pass the name of the attribute in paranthesis.

# You can search element, on the basis of attribute, for that use find(), it returs the first element that matches the search query.
heading_element = soup.find(name="h1", id="name")
# print(heading_element)

# Can do the same with the element with class attribute, just replace the id with class_
# When we are using beautiful soup, we can also select element with the help of css selectors.
# Sometimes, html will not work in selecting the tag.

# To select an element with css selecors, we can use select() and select_one()
anchor_tag = soup.select_one(selector="p a")
print(anchor_tag)
# select_one() method will select the first element that matches the query. We need to pass the selector
# select() method will select all the elements that matches the query and returns the list.