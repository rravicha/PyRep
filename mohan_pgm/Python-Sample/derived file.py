from main_file import *
import logging
logging.basicConfig(filename="mylog.txt",format='%(asctime)s %(levelname)s%(message)s',level=logging.INFO)

v = VM()

class pc_class:

    def open_browser(self):

        global v
        logging.info(" Initiates Browser session")
        v.browser()
        logging.info(" Chrome browser has opened")

    def open_URL(self):

        URL = "https://10.5.214.40:9440"
        print("URL to be used is ", URL)
        logging.info(" Prism Central URL is getting opened on chrome browser")
        v.open_PC_URL()
        logging.info(" PC interface has opened")

    def vlan_creation(self):

        logging.info(" VLAN creation process has been started")
        v.create_vlan()
        logging.info(" VLAN created successfully")

    def VM_creation(self):

        logging.info(" VM creation is in progress")
        v.create_vm()
        logging.info(" VM has been created with all required parameters")

    def VM_clone(self):

        logging.info(" VM cloning is in progress")
        v.vm_cloning()
        logging.info(" Required clones has been created")

    def power_on(self):

        v.power_on_vms()

if __name__ == "__main__":
    p = pc_class()
    p.open_browser()
    p.open_URL()
    p.vlan_creation()
    p.VM_creation()
    p.VM_clone()
    # p.power_on()

# pc_class.open_browser()
# pc_class.open_URL()