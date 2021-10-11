from flask import Flask
from flask_restful import Api
from models.models import init_db
from resources.device import Device
from resources.device import InsereDevice
from resources.device import ListaDevices

app = Flask(__name__)
api = Api(app)

api.add_resource(Device, '/device/<int:id>/')
api.add_resource(InsereDevice, '/insereDevice/')
api.add_resource(ListaDevices, '/device/')

if __name__ == '__main__':
    app.run(debug=True)
    init_db()
