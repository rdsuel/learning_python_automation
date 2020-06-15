from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source = driver.find_element_by_xpath(
    '//*[@id="DHTMLgoodies_dragableElement2"]')
destination = driver.find_element_by_xpath('//*[@id="box103"]')
