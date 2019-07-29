from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import logging
logging.basicConfig(filename="mylog.txt", format='%(asctime)s %(levelname)s%(message)s', level=logging.INFO)

class VM:
    def __init__(self, driver=None):
        self.driver = driver
        # self.user_name = driver.find_element_by_id("inputUsername")
        # self.password = driver.find_element_by_id("inputPassword")
        # self.login_submit = driver.find_element_by_class_name("loginSubmit")

    def browser(self):

        # Browser initiation
        self.driver = webdriver.Chrome(executable_path=r'C:\Python\chromedriver.exe')
        self.driver.maximize_window()

    def open_PC_URL(self):

        # Opens Prism Central
        self.driver.get("http://10.5.214.40/")
        time.sleep(5)
        # Logging in
        logging.info(" Entering Prism central credentials")
        self.user_name = self.driver.find_element_by_id("inputUsername")
        self.user_name.send_keys("admin")
        self.password = self.driver.find_element_by_id("inputPassword")
        self.password.send_keys("Nutanix.123")
        self.login_submit = self.driver.find_element_by_class_name("loginSubmit")
        self.login_submit.click()
        logging.info(" Authentication is in progress")
        time.sleep(10)

        # Clicking explore link in Prism Central
        logging.info(" Switching to VM view")
        self.explore = self.driver.find_element_by_link_text("Explore")
        self.explore.click()
        time.sleep(5)

    def create_vlan(self):

        # Creating network config
        logging.info(" Navigating to Network configuration")
        self.network_config_link = self.driver.find_element_by_xpath("//*[contains(text(),'Network Config')]")
        self.network_config_link.click()
        time.sleep(10)
        self.vir_nw_link = self.driver.find_element_by_xpath("//*[contains(text(),'Virtual Networks')]")
        self.vir_nw_link.click()
        time.sleep(5)
        logging.info(" Creating Network")
        self.create_network_link = self.driver.find_element_by_link_text("Create Network").click()
        time.sleep(3)
        logging.info(" Entering inputs to create VLAN")
        self.vlan_name = self.driver.find_element_by_xpath("//*[@id=\"acropolisNetworkForm\"]/section[1]/input")
        self.vlan_name.send_keys("Sam_VLAN")
        self.vlan_id = self.driver.find_element_by_class_name("vlanID")
        self.vlan_id.send_keys("1")
        self.save_btn = self.driver.find_element_by_xpath("//*[@id=\"popupNetworkConfig\"]/div[2]/footer/button[4]")
        self.save_btn.click()
        time.sleep(5)
        self.close_btn = self.driver.find_element_by_xpath("//*[@id=\"popupNetworkConfig\"]/div[2]/footer/button[3]/span")
        self.close_btn.click()
        time.sleep(8)

    def create_vm(self):

        # Clicking VM popup
        logging.info(" Navigating to VM creation link")
        self.vm = self.driver.find_element_by_xpath("//*[contains(text(),'Create VM')]").click()
        time.sleep(5)
        logging.info(" Entering valid details for VM")
        self.VM_name = self.driver.find_element_by_class_name("inputName").send_keys("Sam_VM")
        self.VM_CPU = self.driver.find_element_by_class_name("inputVcpus").send_keys(1)
        self.VM_Mem = self.driver.find_element_by_class_name("inputMemory").send_keys(1)
        time.sleep(2)
        self.edit_btn = self.driver.find_element_by_xpath("//*[@id=\"storageList\"]/tbody/tr/td[5]/i[1]")
        self.edit_btn.click()
        time.sleep(4)

        # OS Source selection
        logging.info(" Mounting OS from image repository")
        self.operation_dropdown = self.driver.find_element_by_xpath("//*[@id=\"vmStorageForm\"]/div[2]/div[2]/div/div")
        self.image_service = self.driver.find_element_by_xpath("//*[@id=\"vmStorageForm\"]/div[2]/div[2]/div/ul/li[2]")
        actions = ActionChains(self.driver)
        actions.move_to_element(self.operation_dropdown)
        actions.click()
        actions.move_to_element(self.image_service)
        actions.click()
        actions.perform()
        time.sleep(2)

        #image selection from drop down
        logging.info(" Locating Operating System")
        self.image_dropdown = self.driver.find_element_by_xpath("//*[@id=\"vmStorageForm\"]/div[6]/div[2]/div/div")
        self.reqd_image = self.driver.find_element_by_xpath("//*[@id=\"vmStorageForm\"]/div[6]/div[2]/div/ul/li[6]")
        actions = ActionChains(self.driver)
        actions.move_to_element(self.image_dropdown)
        actions.click()
        actions.move_to_element(self.reqd_image)
        actions.click()
        actions.perform()
        time.sleep(2)
        self.update_btn = self.driver.find_element_by_xpath("//*[@id=\"popupVm\"]/div[2]/div[2]/button[3]")
        self.update_btn.click()
        time.sleep(4)

        # Attaching NIC to VM while creation
        logging.info(" Attaching created  NIC to VM")
        self.Add_NIC_btn = self.driver.find_element_by_xpath("//*[@id=\"vmPopupForm\"]/section[6]/div/div/div[2]/button")
        self.Add_NIC_btn.click()
        time.sleep(5)
        logging.info(" Listing out the available VLAN's")
        self.vlan_drop_down = self.driver.find_element_by_xpath("//*[@id=\"vmNetworkForm\"]/div[1]/div/div/div")
        self.reqd_vlan = self.driver.find_element_by_xpath("//*[@id=\"vmNetworkForm\"]/div[1]/div/div/ul/li[2]")
        actions = ActionChains(self.driver)
        actions.move_to_element(self.vlan_drop_down)
        actions.click()
        logging.info(" Selecting required VLAN")
        actions.move_to_element(self.reqd_vlan)
        actions.click()
        actions.perform()
        time.sleep(3)
        self.NIC_submit_btn = self.driver.find_element_by_xpath("//*[@id=\"popupVm\"]/div[2]/div[2]/button[3]")
        self.NIC_submit_btn.click()
        time.sleep(3)

        # Exiting VM popup
        self.VM_popup_submit = self.driver.find_element_by_xpath("//*[@id=\"popupVm\"]/div[2]/div[2]/button[3]")
        self.VM_popup_submit.click()
        time.sleep(5)

    def vm_cloning(self):

        # Searching for created VM and cloning
        #driver.refresh()
        time.sleep(10)
        logging.info(" Navigating to VM cloning page")

        logging.info(" Searching for a VM to get cloned")
        self.search = self.driver.find_element_by_link_text("Sample_VM")
        self.search.click()
        time.sleep(4)
        self.clone_btn1 = self.driver.find_element_by_xpath("//*[@id=\"containerDetails\"]/header[1]/section[2]/div[1]/div/button[3]/span")
        self.clone_btn1.click()
        time.sleep(4)
        logging.info(" Prompts input for the number of clones")
        self.count = self.driver.find_element_by_class_name("inputCloneCount")
        self.count.clear()
        self.count.send_keys(3)
        time.sleep(2)
        logging.info(" Accepting the clone request")
        self.clonne_save = self.driver.find_element_by_xpath("//*[@id=\"popupVm\"]/div[2]/div[2]/button[3]")
        self.clonne_save.click()
        time.sleep(4)
        logging.info(" Navigating to main page")
        self.clone_close = self.driver.find_element_by_xpath("//*[@id=\"containerDetails\"]/header[1]/section[2]/i")
        self.clone_close.click()
        self.driver.close()

    def power_on_vms(self):
        time.sleep(4)
        self.search_field = self.driver.find_element_by_class_name("search-box")
        # self.search_field = self.driver.find_element_by_css_selector(".search-input")
        # self.search_field.send_keys("Sam")
        # time.sleep(3)
        # self.search_field.send_keys("Keys.ENTER")
        actions = ActionChains(self.driver)
        actions.move_to_element(self.search_field)
        actions.send_keys("Sam_VM")
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(5)
        # self.sel_all = self.driver.find_element_by_xpath("//*[@id=\"DataTables_Table_12\"]/thead/tr/th[1]/div/label/svg")

        self.sel_all = self.driver.find_element_by_css_selector(".svg-input")
        self.sel_all.click()

        # self.search_field = self.driver.find_element_by_class_name("search-input")
        # self.search_field.send_keys("Sam_VM")
        # time.sleep(3)
        # self.search_field.send_keys(Keys.ENTER)
        # time.sleep(5)
        # self.sel_all = self.driver.find_element_by_css_selector("input[data-test=checkbox-select-all])")
        # self.sel_all.click()



# if __name__ == "__main__":
#     # print("Prasanna")
#     v = VM()
#     v.browser()

