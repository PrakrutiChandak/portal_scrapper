from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from twilio.rest import Client
import time

URL = "https://www.cowin.gov.in/home"
browser = webdriver.Chrome('/home/prakruti/Documents/Tools/chromedriver')
while 1:
    browser.get(URL)
    time.sleep(1)

    pincodes = [342001, 342005, 342003, 342006, 342011, 342024, 342027, 342007, 342002, 342004]

    elem = browser.find_element_by_id("mat-input-0")
    for pincode in pincodes:
        elem.send_keys(pincode)
        elem.send_keys(Keys.ENTER)

        textSet = set()
        xpathvala = elem.find_elements_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div//a")
        for xpaths in xpathvala:
            textSet.add(xpaths.text)
            for element in textSet:
                if element.isdigit():
                    print("send email")
                else:
                    pass
    time.sleep(60)
