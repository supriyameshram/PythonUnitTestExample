from selenium import webdriver

driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
driver.get("http://demo.guru99.com/V4")
# assert "Google" in driver.title
print("you are on correct page")
# driver.assertIn("guru99", driver.title)
username = driver.find_element_by_name('uid')
username.send_keys("mgr123")
password = driver.find_element_by_name('password')
password.send_keys("mgr!23")
loginbutton = driver.find_element_by_name('btnLogin')
loginbutton.click()
logout = driver.find_element_by_xpath("html/body/div[3]/div/ul/li[15]/a")
logout.click()
try:
    alert = driver.switch_to_alert()
    alert.accept()
    print("alert accepted")
except:
    print("no alert")

driver.close()

