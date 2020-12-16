from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://w2g.tv/")

button = driver.find_element_by_id('create_room_button')

button.click()
#driver.close()