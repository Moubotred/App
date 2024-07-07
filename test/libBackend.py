# como subir modulo a pypip
# https://www.youtube.com/watch?app=desktop&v=4fX8H5EFOXw 

import os
import socket
import telebot
import flet as ft
import threading
import asyncio

import assets.GoogleEyes as Gy

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


import cv2
import numpy as np
from PIL import Image
import io

from quart import Quart, request, jsonify
import os
import asyncio

global NameFile
app = Quart(__name__)

def main(page: ft.Page):
    page.title = "Cámara en tiempo real con Flet"

    # Crear un contenedor para la imagen
    img_container = ft.Image(width=640, height=480)
    page.add(img_container)

    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    def update_frame():
        ret, frame = cap.read()
        if ret:
            # Convertir el frame de BGR (OpenCV) a RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convertir el frame a una imagen PIL
            pil_img = Image.fromarray(rgb_frame)
            
            # Convertir la imagen PIL a bytes
            img_byte_arr = io.BytesIO()
            pil_img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            # Actualizar la imagen en el contenedor
            img_container.src_base64 = img_byte_arr
            page.update()
        
        page.after(1/30, update_frame)  # Actualizar aproximadamente 30 FPS

    update_frame()

def Iplocal():
    ip = socket.gethostname()
    direccion_ip = socket.gethostbyname(ip)
    return direccion_ip

def cliente():
    import socket

    # Reemplaza "192.168.1.100" con la dirección IP real a la que deseas conectarte
    direccion_IP = "192.168.1.100"

    # Define el puerto que deseas usar. Comprueba la documentación del servicio al que te conectas para conocer el puerto correcto
    puerto = 9095

    try:
        # Crea un socket TCP
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta el socket al servidor
        socket_cliente.connect((direccion_IP, puerto))

        # Envía un mensaje al servidor
        mensaje = "Hola, servidor!"
        socket_cliente.sendall(mensaje.encode())

        # Recibe la respuesta del servidor
        respuesta = socket_cliente.recv(1024)

        # Imprime la respuesta del servidor
        print(f"Respuesta del servidor: {respuesta.decode()}")

        # Cierra el socket
        socket_cliente.close()

    except Exception as error:
        # Maneja cualquier error que ocurra durante la conexión
        print(f"Error al conectar al servidor: {error}")

def bot():
    bot = telebot.TeleBot("6714586142:AAHfLLy7MbjzyfXCHAYOle9DjvgUHq-CZrQ")
    # @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Obteniendo IP Pc")

        text = message.text
        Ip = Iplocal()
        if text.startswith("ip"):
            bot.send_message(message.chat.id,Ip)
            
    bot.polling()

def server():
    # app = Flask(__name__)

    # Configura la carpeta donde se guardarán las fotos
    UPLOAD_FOLDER = r'C:\Users\nimun\Documents\scripts\leer_barras\my-app\upload'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Asegúrate de que la carpeta de uploads exista
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    @app.route('/upload', methods=['POST'])
    async def upload_file():
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected for uploading'}), 400
        
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

            # NameFile = file.filename

            await file.save(filename)
            data = await suministro(filename)

            return jsonify({'message': 'File successfully uploaded'}), 200

    # app.run(host='0.0.0.0', port=5000, debug=True)

async def run_server():
    await app.run_task(host='0.0.0.0', port=5000, debug=False)

async def suministro(filename):
    run = Gy.GoogleEyes()
    run.Servicio()
    data = run.Upload(filename)
    print(data)

# async def main():
#     await asyncio.gather(
#         run_server(),
#         suministro('null'),
#     )

# if __name__ == '__main__':
#     asyncio.run(main())

