import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def reservation_script1():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')

    driver.get("https://ucsd.libcal.com/r/accessible")
    driver.find_element(By.XPATH, "//*[@id='s-lc-location']/option[2]").click() #select library
    driver.find_element(By.XPATH, "//*[@id='s-lc-zone']/option[2]").click() #select floor/area
    driver.find_element(By.XPATH, "//*[@id='s-lc-type']/option[2]").click() #number of seats
    driver.find_element(By.XPATH, "//*[@id='s-lc-space']/option[23]").click() #select room 724
    driver.find_element(By.XPATH, "//*[@id='s-lc-go']").click() #submit form

    #Date Selection
    date = driver.find_element(By.XPATH, "//*[@id='date']/option[14]") #get date
    date_val = driver.find_element(By.XPATH, "//*[@id='date']/option[14]").get_attribute("value")
    date.click() #click on date
    driver.find_element(By.XPATH, "//*[@id='s-lc-submit-filters']").click() #click on "show availability"

    #click on times that we want
    driver.find_element(By.XPATH, "//*[@data-start = '"+date_val+" 10:30:00']").click()
    driver.find_element(By.XPATH, "//*[@id='s-lc-submit-times']").click() #submit times

    #wait until shibboleth page loads
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ssousername")))
    #enter username and password
    driver.find_element(By.ID, "ssousername").send_keys("vpabba")
    driver.find_element(By.XPATH, "//*[@id='ssopassword']").send_keys("Wagonwheel@080103")
    driver.find_element(By.NAME, "_eventId_proceed").click()
    #send duo push notification
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='duo_iframe']")))
  
    #submit reservation
    driver.switch_to.default_content()
    driver.implicitly_wait(40)
    driver.find_element(By.XPATH, "//*[@id='terms_accept']").click()

    driver.find_element(By.XPATH, "//*[@id='s-lc-eq-bform-submit']").click()

    time.sleep(30)
