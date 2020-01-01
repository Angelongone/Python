from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

url = "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
driver.get(url)
#id选择器
driver.find_element_by_css_selector("#LoginName").send_keys("dfjkdjfkdjf")
#class选择器
#driver.find_element_by_css_selector(".form-control").send_keys("123456")
driver.find_element_by_css_selector("#Password").send_keys("123456")

sleep(3)
driver.quit()

