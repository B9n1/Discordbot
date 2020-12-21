from selenium import webdriver
import time
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.w2g.tv")
time.sleep(2)

#click coockie button
driver.find_element_by_xpath("//button[@class='sc-ifAKCX dvvOSu']").click()
time.sleep(2)
#Create Room
driver.find_element_by_xpath("//button[@class='ui big primary button loading_button']").click()
#Joins Room
driver.find_element_by_xpath("//div[@class='ui fluid green cancel button']").click()
time.sleep(2)
#Copy Room Inv
driver.find_element_by_xpath("//div[@class='invite-cta w2g-search-hide w2g-users']").click()
time.sleep(2)
link = driver.find_element_by_xpath("//input[@class='invite-url']").get_attribute("value")
print(link)
