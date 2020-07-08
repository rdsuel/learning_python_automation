# Open a web page, add text, click a button, etc.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('20')
addButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
addButton.click()
