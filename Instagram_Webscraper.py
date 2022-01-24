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
        self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        self.username = username
        self.password = password

    def openGram(self):
        self.driver.get("http://www.instagram.com")
        sleep(100) 
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]")\
             .click()


def main():
    print("Welcome to instagram webscraper.")
    username = input("Username:")
    password = input("Password:")
    thisScraper = Insta_Scraper(username, password)
    thisScraper.openGram()

main()