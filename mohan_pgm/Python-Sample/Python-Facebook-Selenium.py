from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
#dirvar = os.get_dir

# create a new Firefox session
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://twitter.com/login")
time.sleep(5)
driver.find_element_by_class_name("js-username-field").send_keys("face_ragu@yahoo.com")
driver.find_element_by_class_name("js-password-field").send_keys("Allah@786")
driver.find_element_by_class_name("EdgeButtom--medium").click()
time.sleep(5)
print("login Successful")
driver.find_element_by_class_name("js-nav js-tooltip js-dynamic-tooltip").click()
driver.find_element_by_id('tweet-box-home-timeline').send_keys("CGI CGI")
driver.find_element_by_css_selector('button.tweet-action').click()
driver.save_screenshot("i-am-on-twitter.png")

img = Image.open("i-am-on-twitter.png")
# absolute filepath is needed
cropped_filename = "/home/susi/pgm/besant python tutorial/mohan_pgm/Python-Sample"
img.crop((0, 0, img.size[0], 400)).save(cropped_filename)
# Upload the image
driver.find_element_by_css_selector('input.file-input').send_keys(cropped_filename)

time.sleep(10)
0
