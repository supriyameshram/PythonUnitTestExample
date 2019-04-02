# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


class Radiocheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://demo.guru99.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_radiocheck(self):
        driver = self.driver
        driver.get(self.base_url + "/test/")
        driver.find_element_by_link_text("Selenium").click()
        driver.find_element_by_link_text("Radio & Checkbox Demo").click()
        driver.find_element_by_id("vfb-7-1").click()
        driver.find_element_by_id("vfb-7-2").click()
        driver.find_element_by_id("vfb-7-3").click()
        driver.find_element_by_id("vfb-7-1").click()
        driver.find_element_by_id("vfb-6-0").click()
        driver.find_element_by_id("vfb-6-1").click()
        driver.find_element_by_id("vfb-6-2").click()
        driver.find_element_by_id("vfb-6-2").click()
        driver.find_element_by_id("vfb-6-1").click()
        driver.find_element_by_id("vfb-6-1").click()
    
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
