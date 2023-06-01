from time import sleep
from random import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver.get("http://fish.leixf.cn/")
driver.maximize_window()
sleep(5)
fish=driver.find_element(by=By.XPATH, value="//*[@id=\"center\"]")

# 敲100次
# for i in range(0, 100):
#     fish.click()
#     sleep(0.2)
#     # 休眠0-1秒随机时间
#     sleep(random())    

# 一直敲
while True:
    fish.click()
    # sleep(0.2)
    # 休眠0-1秒随机时间
    sleep(random())    
