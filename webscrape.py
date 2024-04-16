from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
<<<<<<< HEAD
from selenium.webdriver.common.by import By

=======
>>>>>>> 507c24a76cb75307e2c735b14a6fd631ba7d2a86

typeOfSearch = input("Enter what category you want: ")
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/search/" + typeOfSearch + "/@43.6139333,-79.6633887")

time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

<<<<<<< HEAD
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

=======
>>>>>>> 507c24a76cb75307e2c735b14a6fd631ba7d2a86
#Store Company Name and links to the maps we need
links = []
company = []

for link in soup.find_all("a", class_ = "hfpxzc"):
    links.append(link.get("href"))
    company.append(link.get("aria-label"))
<<<<<<< HEAD
    time.sleep(5)
=======
>>>>>>> 507c24a76cb75307e2c735b14a6fd631ba7d2a86
numbers = []

print(company)
print(links)
<<<<<<< HEAD

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

for i in range(10):
=======
for i in range(3):
>>>>>>> 507c24a76cb75307e2c735b14a6fd631ba7d2a86
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
        

<<<<<<< HEAD
=======

>>>>>>> 507c24a76cb75307e2c735b14a6fd631ba7d2a86
