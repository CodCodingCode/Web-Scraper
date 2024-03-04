from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

typeOfSearch = input("Enter what category you want: ")
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/search/" + typeOfSearch + "/@43.6139333,-79.6633887")

time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

#Store Company Name and links to the maps we need
links = []
company = []

for link in soup.find_all("a", class_ = "hfpxzc"):
    links.append(link.get("href"))
    company.append(link.get("aria-label"))
numbers = []

print(company)
print(links)
for i in range(3):
    driver.get(links[i])
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    potentialNumbers = []
    for num in soup.find_all("div", class_ = "Io6YTe fontBodyMedium kR99db", limit=5):
        potentialNumbers.append(num.get_text())
    print(potentialNumbers)
    for k in range (len(potentialNumbers)):
        if potentialNumbers[k][0] == "(":
            numbers.append(potentialNumbers[k])
    if len(numbers) < i + 1:
        numbers.append("N/A")

print(numbers)

driver.quit()
        


