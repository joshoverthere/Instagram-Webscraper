from selenium import webdriver
from time import sleep
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import matplotlib.pyplot as plt

class Insta_Scraper:
    def __init__(self, username, password):
        #initiate webdriver even if it means reinstalling it
        self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        #set object's logins
        self.username = username
        self.password = password

    def openGram(self):
        #fetch instagram login page and wait for it to load
        self.driver.get("http://www.instagram.com")

        element_present = EC.presence_of_element_located((By.XPATH, '/html/body'))
        WebDriverWait(self.driver, 10).until(element_present)
        print("Fetched instagram login page.")

        #wait for cookies popup to appear
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/button[1]'))
        WebDriverWait(self.driver, 3).until(element_present)
        sleep(100)


def main():
    print("Welcome to instagram webscraper.")
    username = input("Username:")
    password = input("Password:")
    thisScraper = Insta_Scraper(username, password)
    thisScraper.openGram()

main()