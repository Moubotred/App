import os
import asyncio
import datetime
import warnings
from asyncio import Queue
import AsyncGoogleEyes as Gs
from AsyncGoogleEyes import end_ngrok
from quart import Quart, request, jsonify

app = Quart(__name__)

warnings.filterwarnings("ignore")

Fecha = "2024-07-09 04:01:21 -0600"
Formato = "%Y-%m-%d %H:%M:%S %z"
TIEMPO = datetime.datetime.strptime(Fecha, Formato)

UPLOAD_FOLDER = r'C:\Users\nimun\Documents\scripts\test\app\lib\upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class State:
    def __init__(self):
        self.inic = None
        self.queue = Queue()

state = State()

@app.route("/")
async def hello():
    return jsonify({'message': 'Index is running!'})

@app.route('/upload', methods=['POST'])
async def cloud():
    if 'file' not in (await request.files):
        return jsonify({'error': 'No file part in the request'}), 400

    file = (await request.files).get('file')

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        await file.save(filename)
        st = filename.split('\\')
        file_path = "/{}/{}".format(st[len(st)-2], st[len(st)-1])
        await state.queue.put(file_path)  # Añadir a la cola
        return jsonify({'message': 'File successfully uploaded', 'filename': file.filename}), 200

async def Suministro():
    Gg = Gs.GoogleEyes()

    while True:
        file = await state.queue.get()  # Obtener archivo de la cola

        if file is None:
            break

        await Gg.Servicio()
        sum = await Gg.Upload(file)
        print(sum)
        end_ngrok()
        
        state.queue.task_done()  # Indicar que la tarea está completa

async def main():
    import hypercorn.asyncio
    import hypercorn.config

    config = hypercorn.config.Config()
    config.bind = ["192.168.1.109:5000"]
    config.debug = True

    server_task = hypercorn.asyncio.serve(app, config)

    # Ejecutar el servidor y otras tareas simultáneamente
    await asyncio.gather(server_task,Suministro())

if __name__ == '__main__':
    # Ejecutar la corutina principal que maneja todas las tareas
    asyncio.run(main())