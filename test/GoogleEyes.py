# import re
# import time
import asyncio
import os
import time
import subprocess
import time as tmp
import platform
from pyngrok import ngrok
from colorama import Fore
from selenium import webdriver
from multiprocessing.pool import ThreadPool 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options

so = platform.system() 
python = 'python3'if so == 'Linux'else 'python'

def start_http_server(complet,*args):
    if complet == 'fracmentos':
        os.chdir(os.getcwd()+f'//{args[0]}')
        subprocess.Popen([f"{python}", "-m", "http.server", "9090"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        # print('[+] Corriendo Servidor')

    elif complet == 'completo':
        os.chdir(os.getcwd())
        subprocess.Popen([f"{python}", "-m", "http.server", "9090"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        # print('[+] Corriendo Servidor')

def start_ngrok():
    PUERTO = 9090
    ngrok.set_auth_token("1nwcV7atojVGXfYqOyKfMaCDHfQ_6hrzGHH9DBQ2yZeVYEZAf")
    url_publica = ngrok.connect(PUERTO)
    # print(url_publica)
    
class GoogleEyes():
    def __init__(self) -> None:
        self._path_= r'C:\Users\nimun\AppData\Roaming\Mozilla\Firefox\Profiles\tped0zt5.automata'
        self._options_= Options()
        self._options_.add_argument("-profile")
        self._options_.add_argument(self._path_)
        self._driver_ = webdriver.Firefox(options=self._options_)
        self.time = WebDriverWait(self._driver_, 50)
        self.url = 'https://www.google.com/search?client=firefox-b-d&q=ll'

    def Servicio(self):
        pool = ThreadPool(2)
        pool.apply_async(start_http_server('completo'))
        pool.apply_async(start_ngrok())
        tunnels = ngrok.get_tunnels()

        global base_ngrok
        base_ngrok = str(tunnels).split('"')[1]

    def ConversionImgText(self,enlace,fichero):

        enlace.send_keys(base_ngrok+'/'+ fichero)
        enlace.send_keys(Keys.RETURN)

        tmp.sleep(4)
        traducir = self._driver_.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/div/c-wiz/div/div[1]/div/div[3]/div/div/span[3]/span')
        traducir.click()
        tmp.sleep(4)

        lista_informacion = []

        try:
            observaciones = self.time.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@dir="ltr"]/div')))

            for item in range(1,len(observaciones)+1):
                observaciones = self.time.until(EC.presence_of_element_located((By.XPATH,f'//div[@class="QeOavc"]/div[{item}]')))
                lista_informacion.append(observaciones.text)

            # print(observaciones[0])
            return lista_informacion
        

        except TimeoutException:
            return "[-] La imagen con contiene informacion "

    def HandlesSecond(self):
        self._driver_.execute_script("window.open('', 'secondtab');")
        self._driver_.switch_to.window("secondtab")
        self._driver_.get(self.url)  

    def Upload(self,fichero):

        window_handles = self._driver_.window_handles

        try:
            self._driver_.get(self.url)

            tmp.sleep(6)
            lents = self._driver_.find_element(By.CLASS_NAME, 'nDcEnd').click()
            tmp.sleep(4)

            enlace = self.time.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cB9M7[jsname="W7hAGe"]')))

            extensiones = ['.png','.jpeg','.jpg']

            if any(fichero.endswith(ext) for ext in extensiones):
                data =  self.ConversionImgText(enlace,fichero)
                self._driver_.quit()
                return data[0]
            
            else:
                self.Upload(fichero)
        
        except TimeoutException:
            self._driver_.quit()
            return "[-] Se agoto el tiempo de espera "
        
        except NoSuchWindowException:
            self._driver_.quit()
            return "[-] No se encontro ventana esperada "

        except NoSuchElementException:
            self._driver_.quit()
            return "[-] Elemento No Encontrado "
        
        except FileNotFoundError:
            self._driver_.quit()
            return "[-] Fichero No Encontrado "

        except IndexError :
            self._driver_.quit()
            return "[-] IndexError"

