from bs4 import BeautifulSoup
# import lxml

'''Web scraping in Python involves automatically extracting data from websites using
a combination of libraries tailored for handling HTTP requests, parsing HTML, and 
automating browser interactions. '''

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

'''
print(soup.title)  # Returns the title of the website
print(soup.title.name)  # Returns the tag name of the title in website, i.e, title
print(soup.title.string)  # Returns the string in the title tag
print(soup.prettify())  # Auto Indents the website content
print(soup.a)  # Returns the first anchor tag in the website
print(soup.li)  # Returns the first list item tag in the website
print(soup.p)  # Returns the first paragraph tag in the website
'''

all_anchor_tags = soup.find_all(name="a")  # Finds all the anchor tags
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())  # Returns the text from each anchor tag
    print(tag.get(key="href"))  # Return the href(link) in the anchor tag

heading = soup.find(name="h1", id="name")  # Return the h1 tag which has id=name
print(heading)

section_heading = soup.find(name="h3", class_="heading")  # Return the h3 with class=heading
print(section_heading.getText())  # Returns the text from section_heading
print(section_heading.name)  # Return the name of the tag of section_heading
print(section_heading.get(key="class"))  # Return the value of class from section_heading

company_name = soup.select_one(selector="p a")  # Selects one anchor tag which is inside a paragraph tag
print(company_name)

name = soup.select_one(selector="#name")  # Selects one tag which as id=name
print(name)

headings = soup.select(selector=".heading")  # Selects all tags which has class=heading
print(headings)
