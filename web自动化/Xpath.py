from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()

url = "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
driver.get(url)

#绝对路径
# driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/input").send_keys("dskfjsdkfj")
# driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[2]/input").send_keys("123456")

#相对路径
driver.find_element_by_xpath(".//*[@id='LoginName']").send_keys("kfdjkdsjfksdjf")
driver.find_element_by_xpath(".//*[@id='Password']").send_keys("1234567890")

sleep(3)

driver.quit()
