from selenium import webdriver
from time import sleep

dirver = webdriver.Firefox()

url = "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
dirver.get(url)

dirver.find_elements_by_tag_name("input")[1].send_keys("13423534")
sleep(3)
dirver.quit()