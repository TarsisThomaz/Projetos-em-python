from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests
import time

url = 'url aqui'

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get(url)
usuario = driver.find_element_by_xpath('/html/body/form/div/div/div/div[1]/div[1]/div[2]/input')
usuario.click()
usuario.send_keys('email aqui')
time.sleep(3)
senha = driver.find_element_by_xpath('/html/body/form/div/div/div/div[1]/div[1]/div[3]/input')
senha.click()
senha.send_keys('senha aqui')
time.sleep(3)
senha = driver.find_element_by_xpath('/html/body/form/div/div/div/div[1]/div[1]/div[5]/button')
senha.click()
time.sleep(10)
agenda = driver.find_element_by_xpath('/html/body/aside/header/ul[1]/li[1]/a/span/span[1]')
agenda.click()
time.sleep(3)
multipla = driver.find_element_by_xpath('/html/body/aside/header/ul[1]/li[1]/ul/li[4]/a')
multipla.click()
time.sleep(3)
especialidade = driver.find_element_by_xpath(
    '/html/body/aside/section/section/aside/div/div[6]/div/form/div[1]/div[3]/div/button')
especialidade.click()
time.sleep(3)
todas = driver.find_element_by_xpath(
    '/html/body/aside/section/section/aside/div/div[6]/div/form/div[1]/div[3]/div/ul/li[2]/a/label')
todas.click()
time.sleep(3)
buscar = driver.find_element_by_xpath("/html/body/aside/section/section/aside/div/div[6]/div")
buscar.click()
time.sleep(3)