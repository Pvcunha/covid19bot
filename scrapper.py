import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import string

url = 'https://covid.saude.gov.br/'

def get_data():
    # set up option to do not open the browser
    option = Options()
    option.headless = True

    # Openning the browser and loading page
    driver = webdriver.Firefox(options=option)
    driver.get(url)
    time.sleep(5)

    # Findind the elements and scrapping data
    e = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[2]')
    list_text = e.text.split('\n')

    e = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[3]')
    v = e.text.split('\n')

    for i in range(len(v)):
        if v[i] == 'Casos novos':
            v[i] = 'Obitos novos'

    list_text = list_text + v

    #print(list_text)
    
    # Organize the wanted data in a dict
    cases = {}
    flag, key = False, 'None'

    for item in reversed(list_text):
        #print(flag, key)
        if flag:
            cases[key] = item

        (flag, key) = (True, item) if item == 'Casos novos' or item == 'Acumulado' or item == 'Óbitos acumulados' or item == 'Obitos novos' else (False, 'None')


    #print(cases)    

    driver.quit()

    text = 'Atualização dos números do COVID-19 no Brasil.\nNovos casos: {}\nTotal de casos: {}\nNovas mortes: {}\nTotal de mortes: {}'.format(cases['Casos novos'], cases['Acumulado'], cases['Obitos novos'], cases['Óbitos acumulados'])

    #return dict
    return text
