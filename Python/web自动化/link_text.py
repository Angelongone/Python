from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = "https://www.cnblogs.com/"
driver.get(url)
driver.find_element_by_link_text("编程语言(65)").click()

sleep(3)

driver.quit()