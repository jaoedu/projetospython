from re import I
from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element_by_xpath('//*[@id="banner"]/a[1]/img').click()
navegador.find_element_by_xpath('//*[@id="Form1"]/div[7]/a').click()
navegador.find_element_by_xpath('//*[@id="slick-slide10"]/div/div/div/div/div/div/a').click()