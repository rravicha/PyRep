from selenium import webdriver

from selenium.webdriver import ActionChains

import time

import logging

 

logging.basicConfig(level=logging.INFO)

loc_of_file = "C:\Python\calid.xlsx"

Full_Status = []

driver = webdriver.Chrome(executable_path=r'C:\Python\chromedriver.exe')

driver.maximize_window()

driver.get("https://validator.nutanix.com/")

time.sleep(10)

user_name = driver.find_element_by_name("username").send_keys("shajeer.karuthodathu@nutanix.com")

password = driver.find_element_by_name("password").send_keys("Welcome@123")

Submit_btn = driver.find_element_by_class_name("icon-continue").click()

time.sleep(5)

radio_button = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[2]/div[1]/div/label[1]/span[1]/input").click()

next_btn = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[2]/div[2]/button/a").click()

upload_btn = driver.find_element_by_class_name("form-control").send_keys(loc_of_file)

#driver.find_element_by_class_name("form-control").send_keys("C:\Python\cisco.xls")

time.sleep(2)

validate_bom = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div[2]/div[2]/div/div[2]/button").click()

time.sleep(3)

generate_pdf = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[2]/div[2]/div/div[2]/button").click()

logging.info("PDF downloaded")

time.sleep(2)

 

 

#response = driver.find_element_by_class_name("report_status-txt").text

#if "BOM validation failed" in response:

#    print("Failure exists")

#else:

#    print("No failure")

#for row in driver.find_element_by_id("bom-report"):

#    row.find_elements_by_xpath("//span[contains(text(),'Failed')]")

#    print(row.text)

 

 

#res = driver.find_element_by_xpath("//*[@id=\"bom-report\"]").text

#print(res)

#if 'Failed' in res:

#    print("Failure exists")

#else:

#    print("All success")

 

#failed_row = driver.find_element_by_class_name("bom-report-table-tooltip-show")

 

main_status = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[2]/div[1]/div[1]/div[1]").text

if 'BOM validation failed' in main_status:

    for failed_rows in driver.find_elements_by_class_name("bom-report-table-tooltip-show"):

 

        if failed_rows.is_displayed():

            hover = ActionChains(driver).move_to_element(failed_rows)

            hover.perform()

            time.sleep(3)

 

            for tip_texts in driver.find_elements_by_class_name("ant-tooltip-inner"):

                print("Failed SKU's")

                #print("-----------------")

                print(tip_texts.text)

                #print("-----------------")

            #print("\n")

 

        else:

            print("All success")

else:

    print("All SKU's Qualified")

 

time.sleep(2)

driver.close()

 
 
