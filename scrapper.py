import os
import time, datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import string

url = 'https://covid.saude.gov.br/'

# set up option to do not open the browser
def open_browser():
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--no-sandbox")
    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#
    #driver.get(url)
    
    option = Options()
    option.headless = True

    driver = webdriver.Firefox(options=option)
    driver.get(url)
    time.sleep(5)
    return driver


def get_data(driver):

    # Findind the elements and scrapping data
    e = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[2]')
    list_text = e.text.split('\n')

    e = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[3]')
    v = e.text.split('\n')

    for i in range(len(v)):
        if v[i] == 'Casos novos':
            v[i] = 'Obitos novos'

    list_text = list_text + v
    
    # Organize the wanted data in a dict
    cases = {}
    flag, key = False, 'None'

    for item in reversed(list_text):
        #print(flag, key)
        if flag:
            cases[key] = [item]

        (flag, key) = (True, item) if item == 'Casos novos' or item == 'Acumulado' or item == 'Óbitos acumulados' or item == 'Obitos novos' else (False, 'None')


    driver.quit()

    return cases    


def build_text(cases): 
    text = 'Esta é uma atualização automática\nNúmeros diários do COVID-19 no Brasil.\nCasos novos das últimas 24h: {}\nAcumulado de casos: {}\nNovas mortes das últimas 24h: {}\nAcumulado de mortes: {}'.format(cases['Casos novos'][0], cases['Acumulado'][0], cases['Obitos novos'][0], cases['Óbitos acumulados'][0])
    
    return text
