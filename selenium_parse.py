from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = "https://ua1xbet.com/en/live/Football/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

items = driver.find_element_by_id("games_content")






