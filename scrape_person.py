import os
from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")

email = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASSWORD")
linkedin_id = os.getenv("LINKEDIN_ID")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/"+ linkedin_id, driver=driver)

