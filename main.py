import time 
 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

URL  = ""
likeCnt = []
def init():
    # start by defining the options 
    options = webdriver.ChromeOptions() 
    options.headless = True # it's more scalable to work in headless mode 
    # normally, selenium waits for all resources to download 
    # we don't need it as the page also populated with the running javascript code. 
    options.page_load_strategy = 'none' 
    # this returns the path web driver downloaded 
    chrome_path = ChromeDriverManager().install() 
    chrome_service = Service(chrome_path) 
    
    driver = Chrome(options=options, service=chrome_service) 
    driver.implicitly_wait(5)
    print("Please input your directed post")
    URL = input()   
    print("Please input interval per scanning (in second): ")
    interval = input()
    

    driver.get(URL) 
    fileName = driver.find_element(By.CSS_SELECTOR,"a[class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _acan _aiit _acao _aija _acat _acaw _aj1- _a6hd']").text + str((time.time()))+".xlsx"
    f = open(fileName,"a")
    f.close()
    
    
    while(True):
        try:
            content = driver.find_element(By.CSS_SELECTOR,"div[class='_aacl _aaco _aacw _aacx _aada _aade']>span")
            print(content.text)
            curTime = str(time.localtime().tm_hour)+str(time.localtime().tm_min)+str(time.localtime().tm_sec)
            tempLikeStorage=[int(content.text),str(curTime)]
            likeCnt.append(tempLikeStorage)
            df = pd.DataFrame(likeCnt)
            writer = pd.ExcelWriter(fileName, engine='xlsxwriter')
            df.to_excel(writer, sheet_name='welcome', index=False)
            writer.save()
            
            time.sleep(interval)
            driver.get(URL) 
        except:
            print("refresh")
            driver.refresh()
            
    
    
    

def find():
    print(soup)
if __name__ == '__main__':
    init()

