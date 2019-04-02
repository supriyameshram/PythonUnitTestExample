# -*- coding: utf-8 -*-
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Abc(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://demo.guru99.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_abc(self):
        driver = self.driver
        driver.get(self.base_url + "/v4/")
        driver.find_element_by_name("uid").clear()
        driver.find_element_by_name("uid").send_keys("mgr123")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("mgr!23")
        driver.find_element_by_name("btnLogin").click()
        self.assertEqual("Guru99 Bank Manager HomePage", driver.title)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
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
