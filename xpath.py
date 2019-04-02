# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys

class Testcase11(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.guru99.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case11(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.assertEqual("Meet Guru99 - Free Training Tutorials & Video for IT Courses", driver.title)
        print("Title Present")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.titreck"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[2]/ul/li[3]/a/span"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[2]/ul/li[4]"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[2]/ul/li[5]/a/span"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[2]/ul/li[6]/a/span"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[2]/ul/li[7]/a/span"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[2]/ul/li[8]/a/span"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[2]/ul/li[9]/a/span"))
        driver.find_element_by_link_text("Testing").click()
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Testing"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[5]/div/div/div/ul/li/a/span"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "SAP"))
        driver.find_element_by_link_text("SAP").click()
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='maximenuck243']/div[5]/div[2]/div/div/ul/li/a/span"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Web"))
        driver.find_element_by_link_text("Web").click()
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Java"))
        driver.find_element_by_xpath("//div[@id='maximenuck243']/div[2]/ul/li[3]/a/span").click()
        driver.find_element_by_css_selector("span.titreck").click()
        driver.find_element_by_xpath("//div[@id='maximenuck243']/div[2]/ul/li[3]/a/span").click()
        driver.find_element_by_link_text("Selenium").click()
        self.assertEqual("Free Selenium Tutorials", driver.find_element_by_css_selector("h1").text)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Software Testing"))
        driver.find_element_by_link_text("Software Testing").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a[title=\"Software Testing - Introduction - Importance\"] > strong"))
    
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
