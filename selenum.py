from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wildberries.ru/")

product = driver.find_element(By.ID ,"searchInput")
product.send_kyes('laptop')
product.submit()

assert('laptop') in driver.title

div_element=driver.find_element(By.ID,"my_div")
print(div_element.get_attribute("class"))

