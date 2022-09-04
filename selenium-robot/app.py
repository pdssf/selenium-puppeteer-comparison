import logging
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

dataArray = [
    {
        "Phone Number": "40716543298",
        "First Name": "John",
        "Last Name": "Smith",
        "company": "IT Solutions",
        "role": "Analyst",
        "Address": "98 North Road",
        "Email": "jsmith@itsolutions.co.uk",
    },
    {
        "Phone Number": "40791345621",
        "First Name": "Jane",
        "Last Name": "Dorsey",
        "company": "MediCare",
        "role": "Medical Engineer",
        "Address": "11 Crown Street",
        "Email": "jdorsey@mc.com",
    },
    {
        "Phone Number": "40735416854",
        "First Name": "Albert",
        "Last Name": "Kipling",
        "company": "Waterfront",
        "role": "Accountant",
        "Address": "22 Guild Street",
        "Email": "kipling@waterfront.com",
    },
    {
        "Phone Number": "40733652145",
        "First Name": "Michael",
        "Last Name": "Robertson",
        "company": "MediCare",
        "role": "IT Specialist",
        "Address": "17 Farburn Terrace",
        "Email": "mrobertson@mc.com",
    },
    {
        "Phone Number": "40799885412",
        "First Name": "Doug",
        "Last Name": "Derrick",
        "company": "Timepath Inc.",
        "role": "Analyst",
        "Address": "99 Shire Oak Road",
        "Email": "dderrick@timepath.co.uk",
    },
    {
        "Phone Number": "40733154268",
        "First Name": "Jessie",
        "Last Name": "Marlowe",
        "company": "Aperture Inc.",
        "role": "Scientist",
        "Address": "27 Cheshire Street",
        "Email": "jmarlowe@aperture.us",
    },
    {
        "Phone Number": "40712462257",
        "First Name": "Stan",
        "Last Name": "Hamm",
        "company": "Sugarwell",
        "role": "Advisor",
        "Address": "10 Dam Road",
        "Email": "shamm@sugarwell.org",
    },
    {
        "Phone Number": "40731254562",
        "First Name": "Michelle",
        "Last Name": "Norton",
        "company": "Aperture Inc.",
        "role": "Scientist",
        "Address": "13 White Rabbit Street",
        "Email": "mnorton@aperture.us",
    },
    {
        "Phone Number": "40741785214",
        "First Name": "Stacy",
        "Last Name": "Shelby",
        "company": "TechDev",
        "role": "HR Manager",
        "Address": "19 Pineapple Boulevard",
        "Email": "sshelby@techdev.com",
    },
    {
        "Phone Number": "40731653845",
        "First Name": "Lara",
        "Last Name": "Palmer",
        "company": "Timepath Inc.",
        "role": "Programmer",
        "Address": "87 Orange Street",
        "Email": "lpalmer@timepath.co.uk",
    },
]


def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


SEL = By.CSS_SELECTOR

def fillData(driver: webdriver.Chrome, data):
  # Fill data in a form
  input = lambda sel: 'input[ng-reflect-name="{}"]'.format(sel)
  driver.find_element(SEL, 'input[value="Submit"]')
  driver.find_element(SEL,
                  input('labelPhone')).send_keys(data["Phone Number"])
  driver.find_element(SEL,
                  input('labelLastName')).send_keys(data["Last Name"])
  driver.find_element(SEL, input('labelEmail')).send_keys(data["Email"])
  driver.find_element(SEL,
                  input('labelCompanyName')).send_keys(data["company"])
  driver.find_element(SEL, input('labelRole')).send_keys(data["role"])
  driver.find_element(SEL, input('labelAddress')).send_keys(data["Address"])
  driver.find_element(SEL,
                  input('labelFirstName')).send_keys(data["First Name"])
  driver.find_element(SEL, 'input[value="Submit"]').click()


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get('https://www.rpachallenge.com/')
    for i in dataArray:
        fillData(driver, i)
    # driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')


if __name__ == "__main__":
    main()