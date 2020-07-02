import requests
from bs4 import BeautifulSoup

user_budget = int(input("What is your budget? Enter a whole number: "))

r = requests.get("https://www.johnlewis.com/john-lewis-partners-wilton-bed-frame-double/natural/p312175")
content = r.content
soup = BeautifulSoup(content)
element = soup.find("p", {"class": "price price--large"})

string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price > user_budget:
  print("This item is over your budget... Sorry!")
else:
  print("Lets buy it!")