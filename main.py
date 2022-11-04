from multiprocessing import Process, freeze_support
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from funcoes import *

def f():

    url = 'https://www.bet365.com/#/AVR/B146/R^1/'
    driver = uc.Chrome()
    driver.get(url)
    driver.maximize_window()

    usuario, senha = ler_credenciais()

    driver.find_element(By.CLASS_NAME, 'hm-MainHeaderRHSLoggedOutWide_Login').click() 
    time.sleep(3)
    password = driver.find_element(By.CLASS_NAME, 'lms-StandardLogin_Password')
    password.send_keys(senha)
    time.sleep(0.5)
    login = driver.find_element(By.CLASS_NAME, 'lms-StandardLogin_Username')
    #print(login)
    login.send_keys(usuario)
    #driver.find_element(By.CLASS_NAME, 'lms-LoginButton').click()
    time.sleep(7)
    
    div_campeonatos = driver.find_element(By.CLASS_NAME, 'vrl-HorizontalNavBarScroller_ScrollContent')
    lista_campeonatos = div_campeonatos.find_elements(By.CLASS_NAME, 'vrl-MeetingsHeaderButton_Title')

    campeonato_escolhido = 'Mundial'
    mercado_escolhido = 'Resultado final'
    opcao = 'Casa'

    for campeonato in lista_campeonatos:
        if campeonato.text == campeonato_escolhido:
            print(campeonato.text)
            campeonato.click()
            time.sleep(1)

    horarios_div = driver.find_element(By.CLASS_NAME, 'vr-EventTimesNavBar_ButtonContainer')
    #print(horarios_div.text)
    horarios = horarios_div.find_elements(By.CLASS_NAME, 'vr-EventTimesNavBarButton')
    #print(horarios)
    horarios[2].click()

    time.sleep(5) #tempo para carregar as opções e não dar o erro: stale element reference: element is not attached to the page document

    mercados = driver.find_elements(By.CLASS_NAME, 'gl-MarketGroup')
    for mercado in mercados:
        #ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
       # mercado_nome = WebDriverWait(driver, 20,ignored_exceptions=ignored_exceptions)\
        #                .until(EC.presence_of_element_located((By.CLASS_NAME, 'gl-MarketGroupButton_Text')))
        mercado_nome = mercado.find_element(By.CLASS_NAME, 'gl-MarketGroupButton_Text')
        if mercado_nome.text == mercado_escolhido:
            print(mercado_nome.text)
            opcoes = mercado.find_elements(By.CLASS_NAME, 'gl-Participant_General')
            print(len(opcoes))
            time.sleep(5)
            #mercado_nome.click()
            opcoes[0].click()
            #actions = ActionChains(driver)
            #actions.send_keys(Keys.TAB * 10).perform()
            #actions.move_to_element(opcoes[0]).click().perform()
            #if opcao == 'Casa':
           #     mercado.find_elements(By.CLASS_NAME, 'gl-Participant')


    print(len(mercados))

    time.sleep(1000)



if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()