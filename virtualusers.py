from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests



for i in range(2):


    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get("https://development.jubi.ai/mahindramf/")
    time.sleep(5)

    e=driver.find_element_by_id('jubi-secCloseview')
    time.sleep(2)
    e.click()
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="pm-buttonlock"]/div[4]/ul/li[1]/a').click()
    time.sleep(6)

    driver.find_element_by_xpath('//*[@id="pm-buttonlock"]/div[7]/ul/li[1]/a').click()
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="jubi-answerBottom"]').send_keys('individual@test.com',Keys.ENTER)
    time.sleep(4)

    driver.find_element_by_xpath('//*[@id="jubi-answerBottom"]').send_keys('test@123',Keys.ENTER)
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="pm-buttonlock"]/div[13]/ul/li[1]/a').click()
    time.sleep(3)

    driver.refresh()




    # driver.close()