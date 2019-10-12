from selenium import webdriver

#options = webdriver.ChromeOptions()
options = webdriver.Chrome("/usr/bin/chromedriver")
#options.add_argument('--ignore-certificate-errors')
#options.add_argument("--test-type")
#options.binary_location = "/usr/bin/chromium"
options.get('https://python.org')
options.implicitly_wait(10)
options.maximize_window()

time.sleep(5)

driver.save_screenshot("screenshot.png")
driver.close()

#options = webdriver.Chrome(chrome_options=options)

