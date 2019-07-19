#!usr/bin/python3

import time
# 导入 Python 需要使用的 webdriver
from appium import webdriver
# 设备信息
desired_caps = {'platformName': 'Android', 'deviceName': 'a0b021697d13', 'platformVersion': '8.1.0',
                'appPackage': 'com.android.calculator2', 'appActivity': 'com.android.calculator2.Calculator'}
# 初始化设备
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 延时执行，太快的话会导致定位不到控件位置
time.sleep(5)
# 1
driver.find_element_by_id("com.google.android.calculator:id/digit_1").click()
# +
driver.find_element_by_id("com.google.android.calculator:id/op_add").click()
# 8
driver.find_element_by_id("com.google.android.calculator:id/digit_8").click()
# =
driver.find_element_by_id("com.google.android.calculator:id/eq").click()
