from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

url = "https://www.cnblogs.com/"
driver.get(url)

driver.maximize_window()

sleep(2)

driver.set_window_size(300,200)
driver.set_window_position(300,200)

sleep(2)

driver.maximize_window()

driver.find_element_by_link_text("登录").click()

sleep(2)

driver.back()
sleep(2)

driver.forward()
sleep(2)

driver.close()
sleep(2)

driver.quit()