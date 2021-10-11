from flask import request
from flask_restful import Resource
from common.utils import converte_data
from models.models import Dispositivos


class Device(Resource):
    def get(self, id):
        device = Dispositivos.query.filter_by(id=id).first()
        try:
            response = {
                'id': device.id,
                'nome': device.nome,
                'idade': device.latitude,
                'longitude': device.longitude,
                'data_hora': converte_data(device.data_hora)
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Dispositivo não encontrado!'
            }
        return response

    def delete(self, id):
        device = Dispositivos.query.filter_by(id=id).first()
        try:
            device.delete()
            response = {
                'status': 'sucess',
                'mensagem': 'Dispositivo {} excluído com sucesso!'.format(device.id)
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Dispositivo não encontrado!'
            }
        return response


class InsereDevice(Resource):
    def post(self):
        dados = request.json
        device = Dispositivos(nome=dados['nome'], latitude=dados['latitude'], longitude=dados['longitude'])
        device.save()
        response = {
            'id': device.id,
            'nome': device.nome,
            'idade': device.latitude,
            'longitude': device.longitude
        }
        return response


class ListaDevices(Resource):
    def get(self):
        device = Dispositivos.query.all()
        response = [
            {'id': i.id, 'nome': i.nome, 'latitude': i.latitude, 'longitude': i.longitude,
             'data_hora': converte_data(i.data_hora)} for i in device]
        return response
