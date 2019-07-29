from selenium import webdriver
var = "/usr/bin/chromedriver"
#driver = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.chrome(var)
driver.get("http://google.com");
driver.close()
