from time import sleep
from selenium import webdriver

#实例化浏览器
dirver = webdriver.Firefox()
url = "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
dirver.get(url)

#定位使用class属性
dirver.find_element_by_class_name("form-control").send.keys("3454765765")
dirver.find_element_by_class_name("form-control").send.keys("fjsdkf")

sleep(3)

dirver.quit()