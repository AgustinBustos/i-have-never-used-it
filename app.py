from selenium import webdriver
from config import PASS,NOCOMPANY
import time
from selenium.webdriver.support.ui import Select

PATH='C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(PATH)

driver.get('https://gateway.utdt.edu/Login.aspx?backto=%2f')

#entro a la pagina principal
input_mail=driver.find_element_by_id('ctl03_ctl01_ctl00_ctl00_txtEmail')
input_pass=driver.find_element_by_id('ctl03_ctl01_ctl00_ctl00_txtPassword')
input_mail.send_keys("poliagustin@yahoo.com.ar")
input_pass.send_keys(PASS)

subBut=driver.find_element_by_id('ctl03_ctl01_ctl00_ctl00_btnIngresar')
subBut.click()
time.sleep(10)
#voy a la busqueda de trabajo

dropdown=driver.find_element_by_xpath('//*[@id="navbar-bottom"]/ul[2]/li/a')
dropdown.click()
time.sleep(10)
busquedas=driver.find_element_by_xpath('//*[@id="navbar-bottom"]/ul[2]/li/ul/li[6]/a')
busquedas.click()
time.sleep(10)


#cambio por fecha
fecha=Select(driver.find_element_by_xpath('//*[@id="ctl03_ctl00_ctl01_ctl00_drpOrder"]'))
fecha.select_by_value('1')
time.sleep(10)
 

#aca deberia poner una funcion iterable
ull=driver.find_element_by_xpath('//*[@id="content"]/div/div/ul')
main_list=ull.find_elements_by_tag_name('li')
time.sleep(10)

for i in range(len(main_list)-1):
    ull=driver.find_element_by_xpath('//*[@id="content"]/div/div/ul')
    main_list=ull.find_elements_by_tag_name('li')
    time.sleep(10)

    company=main_list[i+1].find_element_by_tag_name('p').text
    main_list[i+1].find_element_by_tag_name('a').click()

    time.sleep(10)
    condition=driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[2]/dl/dd[2]').text
    
    print("Licenciatura en Economía" in condition)
    print(company)
    print(company in NOCOMPANY)
    if ("Licenciatura en Economía" not in condition) or (company in NOCOMPANY):
        time.sleep(10)
        driver.back()
    else:
        try:
            print('other thing')
            driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div[2]/div[3]/a').click()
            time.sleep(5)
            driver.find_element_by_id('ctl03_ctl00_ctl00_ctl00_Postulate_ckTelefono').click()
            time.sleep(10)
            driver.find_element_by_id('ctl03_ctl00_ctl00_ctl00_Postulate_btnSiguiente').click()
            time.sleep(10)
            driver.find_element_by_id('ctl03_ctl00_ctl00_ctl00_txtPassword').send_keys(PASS)
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="ctl03_ctl00_ctl00_ctl00_btnPostulate"]').click()
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="navbar-bottom"]/ul[2]/li/a').click()
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="navbar-bottom"]/ul[2]/li/ul/li[6]/a').click()
            time.sleep(10)
            
            
        except:
            driver.back()
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="navbar-bottom"]/ul[2]/li/a').click()
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="navbar-bottom"]/ul[2]/li/ul/li[6]/a').click()
            time.sleep(10)
    time.sleep(2)

