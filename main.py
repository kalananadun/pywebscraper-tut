from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/p/2AC-011A-009A0?Item=9SIC78TM4P4896"

results = requests.get(url)
# print(results.text)

doc = BeautifulSoup(results.text,"html.parser")

# print(doc.prettify())

# figure out the price of the object using the $ sign and the number after that 

prices = doc.find_all(string="$")
# print(prices)

# parent tag of it 
parent = prices[0].parent
# print(parent)
strong = parent.find("strong")
print(strong.string)