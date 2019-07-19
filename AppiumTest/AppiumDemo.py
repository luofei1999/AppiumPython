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
# 点击行为
click_actions = ["com.google.android.calculator:id/digit_1", "com.google.android.calculator:id/op_add",
                 "com.google.android.calculator:id/digit_8", "com.google.android.calculator:id/eq"]


# 行为的具体操作函数
def test_action(actions):
    for action in actions:
        driver.find_element_by_id(action).click()


# 调用操作函数，并将动作传入
test_action(click_actions)

# test_action(actions)
# 1
# driver.find_element_by_id("com.google.android.calculator:id/digit_1").click()
# +
# driver.find_element_by_id("com.google.android.calculator:id/op_add").click()
# 8
# driver.find_element_by_id("com.google.android.calculator:id/digit_8").click()
# =
# driver.find_element_by_id("com.google.android.calculator:id/eq").click()
