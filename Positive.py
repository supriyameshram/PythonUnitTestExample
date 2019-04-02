
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class Positive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\ChromeDriver\chromedriver.exe")
        # self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "https://www.demo.guru99.com/"
        # time.sleep(20)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_positive(self):
        driver = self.driver
        driver.get(self.base_url + "/v4/")
        self.assertEqual("Guru99 Bank Home Page", driver.title)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "form[name=\"frmLogin\"] > table > tbody > tr > td"))
        self.assertTrue(self.is_element_present(By.XPATH, "//tr[2]/td"))
        driver.find_element_by_name("uid").clear()
        driver.find_element_by_name("uid").send_keys("mgr123")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("mgr!23")
        self.assertTrue(self.is_element_present(By.NAME, "btnLogin"))
        self.assertTrue(self.is_element_present(By.NAME, "btnReset"))
        driver.find_element_by_name("btnLogin").click()
        self.assertEqual("Guru99 Bank Manager HomePage", driver.title)
        driver.find_element_by_link_text("New Customer").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Sup Meshram")
        driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        # driver.find_element_by_id("dob").clear()
        driver.find_element_by_id("dob").send_keys("19/08/1990")
        driver.find_element_by_name("addr").clear()
        driver.find_element_by_name("addr").send_keys("Amr")
        driver.find_element_by_name("city").clear()
        driver.find_element_by_name("city").send_keys("Amr")
        driver.find_element_by_name("state").clear()
        driver.find_element_by_name("state").send_keys("Mahara")
        driver.find_element_by_name("pinno").clear()
        driver.find_element_by_name("pinno").send_keys("411333")
        driver.find_element_by_name("telephoneno").clear()
        driver.find_element_by_name("telephoneno").send_keys("9045457351")
        driver.find_element_by_name("emailid").clear()
        driver.find_element_by_name("emailid").send_keys("mnbvcxz@gmail.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("mnbvcxz")
        self.assertTrue(self.is_element_present(By.NAME, "sub"))
        self.assertTrue(self.is_element_present(By.NAME, "res"))
        self.assertEqual("Guru99 Bank New Customer Entry Page", driver.title)
        driver.find_element_by_name("sub").click()
        # driver.find_element_by_link_text("Log out").click()
        """try:
            alert = driver.switch_to.alert()
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")"""


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
