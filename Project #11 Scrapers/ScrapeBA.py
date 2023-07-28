from bs4 import BeautifulSoup as bs
import requests

r = requests.get("https://www.bproperty.com/en/dhaka/apartments-for-sale-in-mirpur-2/")

soup = bs(r.content, 'html.parser')

contents = soup.prettify()
print(contents)