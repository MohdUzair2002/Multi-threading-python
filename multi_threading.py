from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import threading
count=3
emais=['sarahpena992','barbaracarpenter2639','maria8108turner']
passwors=['N8qcsXQr','Q55xY63','qpY9DDR']
def insta(email,password):
    chrome_options =webdriver.ChromeOptions()
    s=Service(ChromeDriverManager().install())
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=s,options=chrome_options)
    wait=WebDriverWait(driver, 60)
    url='https://www.instagram.com/'
    driver.get(url)
    email1= wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")))
    email1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
    email1.send_keys(email)
    password1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
    password1.send_keys(password)
    login=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
    login.click()
    search_box=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv']")))
    search_box=driver.find_element(By.XPATH,"//div[@class='x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv']")
    search_box.click()
    message_but=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@aria-label='Search input']")))
    message_but=driver.find_element(By.XPATH,"//input[@aria-label='Search input']")
    message_but.send_keys("imrankhan.pti")
    message_but.send_keys(Keys.ENTER)
    message_butto=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _abb0 _ab9s _abcm']")))
    message_butto=driver.find_element(By.XPATH,"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _abb0 _ab9s _abcm']")
    message_butto.click()
    message_butto=wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Message...']")))
    message=driver.find_element(By.XPATH,"//textarea[@placeholder='Message...']")
    message.send_keys("Hi")
    message.send_keys(Keys.ENTER)
for i in range(count):
    browserthread=threading.Thread(target=insta,args=(emais[i],passwors[i]))
    browserthread.start()
