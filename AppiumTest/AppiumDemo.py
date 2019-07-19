#!usr/bin/python3
#coding:utf-8
import time
import os

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'a0b021697d13'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = 'com.android.calculator2.Calculator'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)
driver.find_element_by_id("com.google.android.calculator:id/digit_1").click()
driver.find_element_by_id("com.google.android.calculator:id/op_add").click()
driver.find_element_by_id("com.google.android.calculator:id/digit_8").click()
driver.find_element_by_id("com.google.android.calculator:id/eq").click()
