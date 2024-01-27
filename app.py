import undetected_chromedriver as uc
from selenium import webdriver
from config import PASS,NOCOMPANY
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import By
dt=3

if __name__=='__main__':
    #options=webdriver.ChromeOptions()
    try:
        
        options = uc.ChromeOptions()

        
        options.add_argument("--user-data-dir=/home/agus/.config/google-chrome/") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
        
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
        #driver.get('https://www.google.com/')


        #####################entro a la pagina principal
        try:
            input_mail=driver.find_element(By.ID,'ctl02_txtEmail')
            input_pass=driver.find_element(By.ID,'ctl02_txtPassword')
            input_mail.send_keys("poliagustin@yahoo.com.ar")
            input_pass.send_keys(PASS)

            subBut=driver.find_element(By.ID,'ctl02_btnIngresar')
            subBut.click()
            time.sleep(dt)
        except Exception as e:
         print(e)
      


        #voy a la busqueda de trabajo
        time.sleep(10)
        driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul/li[4]').click()    #//*[@id="navbarNavDropdown"]/ul/li[4]
        time.sleep(1)  
        

        driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul/li[4]/ul/li[5]/a').click()
        time.sleep(10)


        # #cambio por fecha
        # fecha=Select(driver.find_element_by_xpath('//*[@id="ctl03_ctl00_ctl01_ctl00_drpOrder"]'))
        # fecha.select_by_value('1')
        # time.sleep(dt)
        # #semisenior
        
        

        #aca deberia poner una funcion iterable
        ull=driver.find_element(By.XPATH,'//*[@id="ctl04_ctl00_upJobSearchList"]/div[2]')
        main_list=ull.find_elements(By.CLASS_NAME,'jobOffer')
        time.sleep(dt)
        
        

        for i in range(len(main_list)-1):

            ull=driver.find_element(By.XPATH,'//*[@id="ctl04_ctl00_upJobSearchList"]/div[2]')
            main_list=ull.find_elements(By.CLASS_NAME,'jobOffer')
            time.sleep(dt)
            print('-------------------------------------------------------------------------------------------')
            print(main_list[i+1].get_attribute("class"))

            company=main_list[i+1].find_element(By.TAG_NAME,'p').text
            
            main_list[i+1].find_element(By.TAG_NAME,'a').click()

            time.sleep(dt)
            condition=driver.find_element(By.XPATH,'//*[@id="WPForm"]/div[3]/div[1]/div[2]/div/div/div/section[1]/div/div[2]/div[2]/p').text
            
            print("Licenciatura en Economía" in condition)
            
            print(company)
            

            companybool=False
            for nocomp in NOCOMPANY:
                companybool=companybool or (nocomp.lower() in company.lower())
            print('is it previous comp?',companybool)
            if ("Licenciatura en Economía" not in condition) or companybool:
                time.sleep(dt)
                driver.back()
            else:
                try:
                    print('lets apply!')   
                    driver.find_element(By.XPATH,'//*[@id="WPForm"]/div[3]/div[1]/div[2]/div/div/div/section[1]/div/div[2]/div[4]/div/a').click()
                    
                    time.sleep(5)
                    driver.switch_to.window(driver.window_handles[0])
                    driver.find_element(By.XPATH,'//*[@id="swTel"]/span').click()
                    time.sleep(dt)
                    driver.find_element(By.XPATH,'//*[@id="swEmailAlt"]/span').click()
                    time.sleep(dt)
                    driver.find_element(By.XPATH,'//*[@id="ctl03_ctl01_ctl00_Postulate_btnSiguiente"]').click()
                    
                    driver.find_element(By.XPATH,'//*[@id="ctl03_ctl00_txtPassword"]').send_keys(PASS)
                    time.sleep(dt)
                    driver.find_element(By.XPATH,'//*[@id="ctl03_ctl00_btnPostulate"]').click()
                    time.sleep(dt)



                    driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul/li[4]').click()
                    time.sleep(10)
                    driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul/li[4]/ul/li[5]/a').click()
                    time.sleep(10)
                    
                    
                except:
                    print('not applied')
                    time.sleep(dt)
                    driver.back()
                    time.sleep(dt)
                    driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul/li[4]').click()
                    time.sleep(10)
                    driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul/li[4]/ul/li[5]/a').click()
                    time.sleep(10)
            time.sleep(2)
    except Exception as e:
        print(e)
        time.sleep(100000)

