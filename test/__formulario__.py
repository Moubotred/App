import time as tm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class googleform:
    def __init__(self,driver,time,url):
        self.driver = driver
        self.time = time
        self.url = url
        self.usuarios = None

    def fechafoto():
        pass

    def Getusersform(self):
        self.driver.get(self.url)
        usuarios = self.time.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div')))

        lista_usuarios = []

        for user in range(1,len(usuarios)+1):
            usuario = self.time.until(EC.presence_of_element_located((By.XPATH,f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[{user}]/label/div/div[2]/div/span'))).text
            lista_usuarios.append(usuario)
            
        self.usuarios = lista_usuarios
        return lista_usuarios
    
    def Realizarform(self,user):
        Posicionuser = self.usuarios.index(user)+1
        Selectuser = self.time.until(EC.presence_of_element_located((By.XPATH,f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[{Posicionuser}]/label/div/div[2]/div/span'))).click()
        Si = self.time.until(EC.presence_of_element_located((By.ID,'i51'))).click()
        Siguiente = self.time.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))).click()

        Fecha_dd = self.time.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/input'))).send_keys('10')
        Fecha_mm = self.time.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[1]/input'))).send_keys('10')
        Fecha_aa = self.time.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[5]/div/div[2]/div[1]/div/div[1]/input'))).send_keys('2002')

from PIL import Image
from PIL.ExifTags import TAGS

import win32file
import win32con
import pywintypes

# def get_file_dates(file_path):
#     handle = win32file.CreateFile(
#         file_path,
#         win32con.GENERIC_READ,
#         win32con.FILE_SHARE_READ,
#         None,
#         win32con.OPEN_EXISTING,
#         0,
#         None
#     )
    
#     try:
#         creation_time, access_time, write_time = win32file.GetFileTime(handle)
        
#         # Convertir a formato de fecha legible
#         creation_time = pywintypes.Time(creation_time)
#         access_time = pywintypes.Time(access_time)
#         write_time = pywintypes.Time(write_time)
        
#         return {
#             "Creation Time": creation_time.Format("%Y-%m-%d %H:%M:%S"),
#             "Last Access Time": access_time.Format("%Y-%m-%d %H:%M:%S"),
#             "Last Write Time": write_time.Format("%Y-%m-%d %H:%M:%S")
#         }
    
#     finally:
#         win32file.CloseHandle(handle)

# # Uso
# file_path = "data.jpeg"
# dates = get_file_dates(file_path)

# for date_type, date_value in dates.items():
#     print(f"{date_type}: {date_value}")

import re
import subprocess

def get_wifi_ip():
    """Obtiene la dirección IP de la zona wifi del celular."""

    # Activar la zona wifi del celular (requiere interacción manual)
    print("Activa la zona wifi del celular y presiona Enter para continuar...")
    input()

    # Obtener la salida del comando "netsh wlan show hostednetwork"
    output = subprocess.check_output(["netsh", "wlan", "show", "hostednetwork"], encoding="utf-8")

    # Buscar la dirección IP en la salida
    match = re.search(r"IP Address\s*:\s*(\d+\.\d+\.\d+\.\d+)", output)
    if match:
        return match.group(1)
    else:
        return None


if __name__ == "__main__":
    wifi_ip = get_wifi_ip()
    if wifi_ip:
        print(f"Dirección IP de la zona wifi: {wifi_ip}")
    else:
        print("No se pudo obtener la dirección IP de la zona wifi")