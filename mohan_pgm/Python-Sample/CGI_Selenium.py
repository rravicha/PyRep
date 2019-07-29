from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.utils import keys_to_typing

from tkinter import messagebox

import time

 

#Setting up the chromdriver path

path = r'C:\Python\chromedriver.exe'

driver = webdriver.Chrome(executable_path=path)

 

try:

    #Opens up chrome browser

    driver.maximize_window()

    driver.get("https://facebook.com")

    time.sleep(5)

 

    #login process

    uid = driver.find_element_by_id("txtUserID").send_keys("mohan")

    pwd = driver.find_element_by_id("txtPassword").send_keys("a@2290")

    #dom = driver.find_element_by_id("ddlDomain").send_keys("HCLTECH")

    time.sleep(5)

    submit_btn = driver.find_element_by_id("btnSubmit").click()

    driver.find_element_by_id("btnskipndcontinue").click()

    time.sleep(2)

 

    #searches for iTime app

    driver.find_element_by_id("txtSearch").send_keys("Time")

    time.sleep(4)

    ele = driver.find_element_by_xpath("//*[@id='ui-id-4']/table/tbody/tr/td/a")

    ele.click()

    time.sleep(7)

    btn = driver.find_element_by_id("le_apply")

    btn.click()

    time.sleep(2)

    driver.quit()

except:

    driver.quit()
