import os
import asyncio
import datetime
import platform
import warnings
import subprocess
import time as tmp
from pyngrok import ngrok
from selenium import webdriver
from multiprocessing.pool import ThreadPool
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException, NoSuchElementException

so = platform.system() 
python = 'python3'if so == 'Linux'else 'python'
ngrok_tunnel = None

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
    global ngrok_tunnel
    if ngrok_tunnel is None:
        PUERTO = 9090
        ngrok.set_auth_token("1nwcV7atojVGXfYqOyKfMaCDHfQ_6hrzGHH9DBQ2yZeVYEZAf")
        ngrok_tunnel = ngrok.connect(PUERTO)
        # print(ngrok_tunnel)
    return ngrok_tunnel

def end_ngrok():
    global ngrok_tunnel
    if ngrok_tunnel:
        ngrok.disconnect(ngrok_tunnel.public_url)
        ngrok_tunnel = None

class GoogleEyes:
    def __init__(self) -> None:
        self._path_ = r'C:\Users\nimun\AppData\Roaming\Mozilla\Firefox\Profiles\tped0zt5.automata'
        self._options_ = Options()
        self._options_.add_argument("-profile")
        self._options_.add_argument(self._path_)
        self._driver_ = webdriver.Firefox(options=self._options_)
        self.time = WebDriverWait(self._driver_, 50)
        self.url = 'https://www.google.com/search?client=firefox-b-d&q=ll'
        self.UrlDinamicaNgrok = str
        self.Fecha = "2024-07-09 04:01:21 -0600"
        self.Formato = "%Y-%m-%d %H:%M:%S %z"
        self.Tiempo = datetime.datetime.strptime(self.Fecha, self.Formato)

    async def Servicio(self):
        def start_services():
            pool = ThreadPool(2)
            pool.apply_async(start_http_server('completo'))
            pool.apply_async(start_ngrok())
            tunnels = ngrok.get_tunnels()
            return str(tunnels).split('"')[1]

        self.UrlDinamicaNgrok = await asyncio.to_thread(start_services)

    async def ConversionImgText(self, enlace, fichero):
        
        print(f'[{self.Tiempo}] [File UPLOAD]',f'{self.UrlDinamicaNgrok}{fichero}')

        await asyncio.to_thread(enlace.send_keys,f'{self.UrlDinamicaNgrok}{fichero}')

        await asyncio.sleep(10)
        await asyncio.to_thread(enlace.send_keys, Keys.RETURN)
        await asyncio.sleep(4)
        
        traducir = await asyncio.to_thread(self._driver_.find_element, By.ID, 'ucj-3')

        await asyncio.to_thread(traducir.click)
        await asyncio.sleep(4)

        lista_informacion = []

        try:
            observaciones = self.time.until(EC.presence_of_element_located((By.XPATH,'//div[@class="GgrNRc"]'))).text
            lista = observaciones.split(' ')
            orden = lista[0].replace("\n",",").split(',')
            return f"[{self.Tiempo}] [ RESPUESTA ] {orden}"
        
        except TimeoutException:
            return f"[{self.Tiempo}] [ RESPUESTA ] La imagen no contiene información "

    async def Upload(self, fichero):
        try:
            await asyncio.to_thread(self._driver_.get, self.url)
            await asyncio.sleep(6)
            lents = await asyncio.to_thread(self._driver_.find_element, By.CLASS_NAME, 'nDcEnd')
            await asyncio.to_thread(lents.click)
            await asyncio.sleep(4)
            enlace = await asyncio.to_thread(self.time.until, EC.presence_of_element_located((By.CSS_SELECTOR, '.cB9M7[jsname="W7hAGe"]')))
            extensiones = ['.png', '.jpeg', '.jpg']
            try:
                if any(fichero.endswith(ext) for ext in extensiones):
                    data = await self.ConversionImgText(enlace, fichero)
                    # await asyncio.to_thread(self._driver_.quit)
                    return data

                else:
                    await asyncio.sleep(1)
                    await self.Upload(fichero)
                    print('Usando recusividad 2')

            except AttributeError:
                await asyncio.sleep(1)
                await self.Upload(fichero)
                print('Usando recusividad 3')
        except TimeoutException:
            # await asyncio.to_thread(self._driver_.quit)
            return f"[{self.Tiempo}] [0000] [INFO] Se agotó el tiempo de espera "      
        except NoSuchWindowException:
            # await asyncio.to_thread(self._driver_.quit)
            return f"[{self.Tiempo}] [0000] [INFO] No se encontró ventana esperada "
        except NoSuchElementException:
            # await asyncio.to_thread(self._driver_.quit)
            return f"[{self.Tiempo}] [0000] [INFO] Elemento No Encontrado "
        except FileNotFoundError:
            # await asyncio.to_thread(self._driver_.quit)
            return f"[{self.Tiempo}] [0000] [INFO] Fichero No Encontrado "
        except IndexError:
            return f"[{self.Tiempo}] [0000] [INFO] IndexError"
        