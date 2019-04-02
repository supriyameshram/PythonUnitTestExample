# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class PositiveTestcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://demo.guru99.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_positive_testcase(self):
        driver = self.driver
        driver.get(self.base_url + "/v4/")
        self.assertEqual("Guru99 Bank Home Page", self.driver.title)
        print("Guru99 Bank Home Page Title is present")
        driver.find_element_by_link_text("Selenium").click()
        print("Selenium Link is present")
        driver.find_element_by_link_text("Insurance Project").click()
        print("Insurance Project Link is present")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Demo Site"))
        print("Demo Site Link is present")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Register"))
        print("Register Link is present")
        driver.find_element_by_link_text("Register").click()
        Select(driver.find_element_by_id("user_title")).select_by_visible_text("Ms")
        Select(driver.find_element_by_id("user_title")).select_by_visible_text("Miss")
        driver.find_element_by_id("user_firstname").clear()
        driver.find_element_by_id("user_firstname").send_keys("Supriya")
        driver.find_element_by_id("user_surname").clear()
        driver.find_element_by_id("user_surname").send_keys("Meshram")
        driver.find_element_by_id("user_phone").clear()
        driver.find_element_by_id("user_phone").send_keys("9130529302")
        Select(driver.find_element_by_id("user_dateofbirth_1i")).select_by_visible_text("1995")
        Select(driver.find_element_by_id("user_dateofbirth_2i")).select_by_visible_text("January")
        Select(driver.find_element_by_id("user_dateofbirth_3i")).select_by_visible_text("17")
        Select(driver.find_element_by_id("user_occupation_id")).select_by_visible_text("Student")
        driver.find_element_by_id("user_address_attributes_street").clear()
        driver.find_element_by_id("user_address_attributes_street").send_keys("Amravati")
        driver.find_element_by_id("user_address_attributes_city").clear()
        driver.find_element_by_id("user_address_attributes_city").send_keys("Amravati")
        driver.find_element_by_id("user_address_attributes_county").clear()
        driver.find_element_by_id("user_address_attributes_county").send_keys("India")
        driver.find_element_by_id("user_address_attributes_postcode").clear()
        driver.find_element_by_id("user_address_attributes_postcode").send_keys("123456")
        driver.find_element_by_id("user_user_detail_attributes_email").clear()
        driver.find_element_by_id("user_user_detail_attributes_email").send_keys("abcdef@gmail.com")
        driver.find_element_by_id("user_user_detail_attributes_password").clear()
        driver.find_element_by_id("user_user_detail_attributes_password").send_keys("abc123")
        driver.find_element_by_id("user_user_detail_attributes_password_confirmation").clear()
        driver.find_element_by_id("user_user_detail_attributes_password_confirmation").send_keys("abc123")
        self.assertTrue(self.is_element_present(By.ID, "resetform"))
        self.assertTrue(self.is_element_present(By.NAME, "submit"))
        driver.find_element_by_name("submit").click()
        self.assertTrue(self.is_element_present(By.ID, "email"))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("abcdef@gmail.com")
        self.assertTrue(self.is_element_present(By.ID, "password"))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        self.assertTrue(self.is_element_present(By.NAME, "submit"))
        driver.find_element_by_name("submit").click()
        driver.find_element_by_id("ui-id-2").click()
        driver.find_element_by_id("ui-id-3").click()
        driver.find_element_by_id("ui-id-1").click()
        self.assertEqual("Insurance Broker System", driver.title)
        self.assertTrue(self.is_element_present(By.ID, "ui-id-1"))
        self.assertTrue(self.is_element_present(By.ID, "ui-id-2"))
        driver.find_element_by_id("ui-id-2").click()
        self.assertTrue(self.is_element_present(By.ID, "ui-id-3"))
        driver.find_element_by_id("ui-id-3").click()
        driver.find_element_by_id("ui-id-4").click()
        driver.find_element_by_id("ui-id-5").click()
        driver.find_element_by_css_selector("input.btn.btn-danger").click()
    
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
