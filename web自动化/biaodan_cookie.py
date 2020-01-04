from selenium import webdriver
#导入select模块的方法
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
#注册页链接网址
#url = "http://angelong.top/HTML/mywebs/meitancuiya/HTML/zc.html"
#Angelong首页地址
url = "http://angelong.top/"
#baidu.com
url = "https://www.baidu.com/"
driver.get(url)
#css定位方法
'''
sleep(3)
#定位上海
driver.find_element_by_css_selector("[value = 'sh']").click()
sleep(3)
#定位贵州
driver.find_element_by_css_selector("[value = 'sz']").click()
'''
'''
#Select类方法
sleep(3)

em = driver.find_element_by_css_selector("#cs")
#下标定位
Select(em).select_by_index(2)
sleep(2)

#通过value值定位
Select(em).select_by_value("sh") sleep(2)

#通过文本值定位
Select(em).select_by_visible_text("贵州")
'''
'''
#操作提醒框
driver.find_element_by_css_selector("#djzc").click()
sleep(2)
alert = driver.switch_to_alert()
alert.dismiss()
sleep(2)
driver.find_element_by_css_selector("#sjh").send_keys("12345678901")
'''
'''
#frame表单切换
#注册页操作
driver.find_element_by_css_selector("#sjh").send_keys("Angelong")
driver.find_element_by_css_selector("#mima").send_keys("Angelong")
#切换到注册页a
driver.switch_to.frame("zcaa")
#操作注册页a
driver.find_element_by_css_selector("#sjha").send_keys("Angelong")
driver.find_element_by_css_selector("#mimaa").send_keys("Angelong")
#回退到注册页
driver.switch_to.default_content()
#进入到注册页b
driver.switch_to.frame("zcba")
#操作注册页b
driver.find_element_by_css_selector("#sjhb").send_keys("Angelong")
driver.find_element_by_css_selector("#mimab").send_keys("Angelong")
'''
'''
#滚动条操作
sleep(3)
js = "window.scrollTo(0,1000)"
driver.execute_script(js)
'''
#窗口切换
'''
#点击进入新窗口
driver.find_element_by_css_selector(".fontAdd").click()
#获取当前窗口的句柄
temp = driver.current_window_handle
print("当前网页的句柄为：" , temp)

t = driver.window_handles
print("打印全部的句柄：" , t)
for h in t:
    if h != temp:
        driver.switch_to.window(h)
'''
#屏幕截图
'''
#调用截图方法
driver.get_screenshot_as_file("./Angelong.png")
'''

#cookie
'''
driver.add_cookie({"name":"BDUSS","value":"khwfkQ5allBS1BYNGNqMjFzNzdnUmJ6aE1MeTBEMnZZYXQ2S3RJMW8yOHhJemhlRUFBQUFBJCQAAAAAAAAAAAEAAAAyL8KsQW5nZWxvbmc0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADGWEF4xlhBeb"})
sleep(3)
driver.refresh()
'''

sleep(3)
driver.quit()