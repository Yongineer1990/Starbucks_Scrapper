from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome("/Users/yong_macbook/devtool/chromedriver")
driver.implicitly_wait(3)

url = "https://www.starbucks.co.kr/menu/drink_list.do"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
drink_list = soup.find_all("li", {"class": "menuDataSet"})

for list in drink_list:
    get_menu = list.find("dd").text
    get_img = list.find("a", {"class": "goDrinkView"}).find("img")["src"]
