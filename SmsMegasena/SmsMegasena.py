
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from twilio.rest import Client

#app only work connected on internet

#get mega sena numbers of wednesday and saturday

navegador = webdriver.Chrome()
navegador.get("https://noticias.uol.com.br/loterias/mega-sena/")

number1 = navegador.find_element(By.XPATH,
    '/html/body/div[5]/section[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]').get_attribute('innerHTML') 

number2 = navegador.find_element(By.XPATH,
    '/html/body/div[5]/section[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]').get_attribute('innerHTML') 

number3 = navegador.find_element(By.XPATH,
    '/html/body/div[5]/section[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[3]').get_attribute('innerHTML') 

number4 = navegador.find_element(By.XPATH,
    '/html/body/div[5]/section[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[4]').get_attribute('innerHTML') 

number5 = navegador.find_element(By.XPATH,
    '/html/body/div[5]/section[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[5]').get_attribute('innerHTML') 

number6 = navegador.find_element(By.XPATH,
    '/html/body/div[5]/section[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[6]').get_attribute('innerHTML') 

acumulado = navegador.find_element(By.XPATH,
    '/html/body/div[5]/section[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]').get_attribute('innerHTML') 

print("\n"+number1+"\n"+number2+"\n"+number3+"\n"+number4+"\n"+number5+"\n"+number6)

print("\nvalor acumulado: "+acumulado)

navegador.quit()

#send to joselita's phone

account_sid = "AC8a4fa90526612b991d5bc571fba0b6e2"
auth_token = "658d5f8562b2766f96ff6e0275b903a6"
client = Client(account_sid, auth_token)

message = client.messages.create(
               from_='+17739852051',  
               body="números da megasena: "+number1+", "+number2+", "+number3+", "+number4+", "+number5+", "+number6+"\n\nvalor acumulado: "+acumulado,      
               to='+5541992826842' 
)

