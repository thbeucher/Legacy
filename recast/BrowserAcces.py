#-------------------------------------------------------------------------------
# Name:        BrowserAcces
# Purpose:
#
# Author:      tbeucher
#
# Created:     13/12/2016
# Copyright:   (c) tbeucher 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class Browser:
    def __init__(self):
        self.chrome = os.getcwd() + "/chromedriver.exe"
        #self.driver.implicitly_wait(10)

    def openBrowser(self):
        self.driver = webdriver.Chrome(executable_path=self.chrome)
        self.wait = ui.WebDriverWait(self.driver, 10)
        self.driver.get("https://www.google.fr/maps/")

    def getItineraire(self, departure,  dest):
        self.openBrowser()
        idd = self.driver.find_element_by_id("searchboxinput")
        idd.send_keys(dest)
        time.sleep(2)
        self.driver.find_element_by_id("searchbox-searchbutton").click()
        buttonItineraire = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pane"]/div/div[2]/div/div/div[1]/button[2]')))
        buttonItineraire.click()
        fromAdd = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sb_ifc51"]/input')))
        fromAdd.send_keys(departure)
        fromAdd.send_keys(Keys.RETURN);