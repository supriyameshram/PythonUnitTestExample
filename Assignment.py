from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
driver.get("https://www.google.com/")
assert "Google" in driver.title
# time.sleep(20)
elem = driver.find_element_by_id("lst-ib")
elem.send_keys("India")
elem1 = driver.find_element_by_name("q")
FirstLink = driver.find_element_by_link_text("www.google.com")
SecondLink = driver.find_element_by_partial_link_text("googl.com")
content = driver.find_element_by_class_name("gsfi")
heading1 = driver.find_element_by_tag_name('div.id=gs_ls0')
elem.send_keys("India")
elem2 = driver.find_element_by_id("gsr").click()
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()





