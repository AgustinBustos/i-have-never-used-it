import undetected_chromedriver as uc
from selenium import webdriver
from config import PASS,NOCOMPANY
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import By
dt=3

if __name__=='__main__':
    #options=webdriver.ChromeOptions()
   
        
        options = uc.ChromeOptions()

        
        options.add_argument(r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
        
        options.add_argument('--profile-directory=Default') #e.g. Profile 3

        # options.add_argument("--start-maximized")
        # options.add_argument("--ignore-certificate-errors")
        # options.add_argument('--no-sandbox')
        # options.add_argument("--disable-extensions")
        # # Disable webdriver flags or you will be easily detectable
        # options.add_argument("--disable-blink-features")
        # options.add_argument("--disable-blink-features=AutomationControlled")
        
        driver=uc.Chrome(options=options)
        # driver=uc.Chrome()
        # driver=webdriver.Chrome(options=options)
        # print('here2')
        # PATH='C:\Program Files (x86)\chromedriver.exe'
        # driver=webdriver.Chrome(PATH)
        
        driver.get('https://gateway.utdt.edu/Login.aspx?backto=%2f')
        # 
        # 'https://gateway.utdt.edu/Login?backto=%2f'
        time.sleep(10000)