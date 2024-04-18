from selenium import webdriver
import pandas as pd
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


try:
    #=====================For Headless and Others==============================#
    # option = webdriver.ChromeOptions()
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')
    # option.add_argument('--no-sandbox')
    # option.add_argument('--disable-dev-shm-usage')
    # driver = webdriver.Chrome(options=option)

    #======================Chrome Driver Auto Install ================================#

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.gps-coordinates.net/")
    print(driver.title)



except Exception as e:
    print("browser exception", e)




# file_input = driver.find_element_by_xpath('//*[@id="home-cover-content"]/div[2]/a')

data = pd.read_excel(r"/Users/shahriar/OfficeWorks/Testing/Location_Extractor_With_LatLon/Book1.xls", engine='xlrd')

data['roadname'] = ''
time.sleep(5)

try:

    for i in range(len(data)):
        print("entering loop")
        location = str(data['Latitude'].iloc[i])
        location2 = str(data['Longitude'].iloc[i])
        # area = location+","+location2
        print(location)
        print(location2)
        # driver.find_element_by_xpath(
        # '/html/body/div[2]/div[2]/div[3]/div[1]/form[2]/div[1]/div/input').sendKeys(location)
        # driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/form[2]/div[2]/div/input').sendKeys(location2)

        time.sleep(2)
        # driver.find_element("xpath", '/html/body/div[2]/div[2]/div[3]/div[1]/form[2]/div[1]/div/input').clear()
        driver.find_element("xpath", '/html/body/div[1]/div[2]/div[3]/div[1]/form[2]/div[1]/div/input').clear()
        driver.find_element("xpath",'/html/body/div[1]/div[2]/div[3]/div[1]/form[2]/div[1]/div/input').send_keys(location)
        driver.find_element("xpath", '/html/body/div[1]/div[2]/div[3]/div[1]/form[2]/div[2]/div/input').clear()
        driver.find_element("xpath", '/html/body/div[1]/div[2]/div[3]/div[1]/form[2]/div[2]/div/input').send_keys(location2)
        driver.find_element("xpath",'/html/body/div[1]/div[2]/div[3]/div[1]/form[2]/div[3]/div/button').click()
        time.sleep(5)

        road = driver.find_element("xpath", '/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div[2]/h1').text

        print(road)
        print("Initiating to create Combine Output")
        data.loc[i, 'roadname'] = road

    data.to_excel(r"/Users/shahriar/OfficeWorks/Testing/Location_Extractor_With_LatLon/Road2.xlsx")

    print("Done")

except Exception as e:
    print("exception occurred", e)