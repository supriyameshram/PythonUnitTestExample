# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class Testcase3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case3(self):
        driver = self.driver
        time.sleep(10)
        driver.get(self.base_url + "/")
        self.assertEqual("Google", self.driver.title)
        print("Google Title is present")
        driver.find_element_by_id("lst-ib").clear()
        elem = driver.find_element_by_id("lst-ib")
        elem.send_keys("www.guru99.com")
        elem.send_keys(Keys.ENTER)
        self.assertEqual("www.guru99.com - Google Search", driver.title)
        print("Title is present")
        driver.find_element_by_link_text("Meet Guru99 - Free Training Tutorials & Video for IT Courses").click()
        self.assertEqual("Meet Guru99 - Free Training Tutorials & Video for IT Courses", driver.title)
        driver.find_element_by_css_selector("div.g-content.g-particle > form > input[name=\"q\"]").click()
        driver.find_element_by_css_selector("div.g-content.g-particle > form > input[name=\"q\"]").click()
        driver.find_element_by_css_selector("div.g-content.g-particle > form > input[name=\"q\"]").clear()
        driver.find_element_by_css_selector("div.g-content.g-particle > form > input[name=\"q\"]").send_keys("Python")
        driver.find_element_by_xpath("//section[@id='g-above']/div/div/div/div/div/div/div/div[2]").click()
        driver.find_element_by_css_selector("div.g-content.g-particle > form > input[type=\"submit\"]").click()
        for i in range(60):
            try:
                if "Search" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_name("sa").click()
    
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
