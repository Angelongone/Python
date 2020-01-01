from selenium import webdriver
from time import sleep
#实例化浏览器对象
driver = webdriver.Firefox()
url = "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
#打开url
driver.get(url)
#定位用户及操作
driver.find_element_by_name("LoginName").send_keys("23424")
#定位密码及操作
driver.find_element_by_name("Password").send_keys("123456")

sleep(3)

driver.quit()