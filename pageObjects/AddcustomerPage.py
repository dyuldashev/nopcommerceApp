import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By


class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    lnkCustomers_menuitem_xpath = "//nav/ul/li[4]/ul/li[1]/a"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtcustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstitemAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    lstitemRegistred_xpath = "//li[contains(text(), 'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(), 'Guests']"
    lstitemVendors_xpath = "//li[contains(text(), 'Vendors']"
    drpmgrOfVendors_xpath = "//*[@id='VendorId']"

    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistred_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_elements(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == "Guests":
            # Here user can be Registered ( or ) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistred_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)

        # self.listitem.click()
        print(self.listitem, "##################################")
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendors_xpath))
        drp.select_by_visible_text(value)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdFemaleGender_id).clic()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, cname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(cname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
