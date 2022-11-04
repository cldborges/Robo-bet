from multiprocessing import Process, freeze_support
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
    
    
url = 'https://www.bet365.com/#/AVR/B146/R^1/'
driver = uc.Chrome()
driver.get(url)
driver.maximize_window()

for i in range(5):
    time.sleep(5)
    for i in range (89):
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.2)
        i+=1
    actions.send_keys(Keys.SPACE).perform()
    print('olha')
    #time.sleep(60)
    #print(driver.find_element(By.CLASS_NAME, 'gl-MarketGroupButton_Text').text) #teste
    #time.sleep(2)
    #driver.find_element(By.CLASS_NAME, 'vr-ResultsNavBarButton').click() # Resultado
    #time.sleep(2)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'vr-BettingSuspendedScreen_Message')) # erro
            )
        time.sleep(60)
        print(driver.find_element(By.CLASS_NAME, 'vr-BettingSuspendedScreen_Message').text)
        driver.refresh()
        i += 1
    except:
        print(driver.find_element(By.CLASS_NAME, 'vrr-HTHTeamDetails_TeamOne').text) #time 1
    #erro = driver.find_element(By.CLASS_NAME, 'vr-BettingSuspendedScreen_Message').text()
    #if not erro:
        #
    #else:
    #   print(erro)
#time.sleep(1000)