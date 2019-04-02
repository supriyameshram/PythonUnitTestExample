from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
driver.get("https://www.guru99.com/")
# assert "Guru99" in driver.title
elem = driver.find_element_by_partial_link_text("Python")
elem.send_keys(Keys.RETURN)
assert "Python Tutorial for Beginners" in driver.title
print("Title present")
assert "No results found." not in driver.page_source
driver.close()