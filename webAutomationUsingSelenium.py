from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
# driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
# messageField.send_keys('Hey Shruti')
# showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
# showMessageButton.click()
# add1 = driver.find_element_by_xpath('//*[@id="sum1"]')
# add1.send_keys('33')
# add2 = driver.find_element_by_xpath('//*[@id="sum2"]')
# add2.send_keys('435')
# btnTotal = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
# btnTotal.click()

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
srcDenmark = driver.find_element_by_xpath('//*[@id="box3"]')
print srcDenmark.text
desDenmark = driver.find_element_by_xpath('//*[@id="box103"]')
print desDenmark.text
actionMap = ActionChains(driver)
actionMap.drag_and_drop(srcDenmark, desDenmark)
actionMap.perform()
print ('Action done!')