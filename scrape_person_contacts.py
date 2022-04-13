import os
from linkedin_scraper import Person, actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver", options=chrome_options)

email = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASSWORD")
linkedin_id = os.getenv("LINKEDIN_ID")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/"+ linkedin_id, contacts=[], driver=driver)

print("Person: " + person.name)
print("Person contacts: ")

for contact in person.contacts:
	print("Contact: " + contact.name + " - " + contact.occupation + " -> " + contact.url)

