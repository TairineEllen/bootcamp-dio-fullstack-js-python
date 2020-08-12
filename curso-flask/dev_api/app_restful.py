from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades

import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
        {'nome':'Tairine',
        'habilidades':['Python', 'Django']
        },
        {'nome':'Nilton',
        'habilidades': ['JavaScript', 'React']
        }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido.'
            response = {'status':'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

class Lista_dev(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return {'status':'sucesso', 'mensagem':'Registro inserido com sucesso'}

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_dev, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug = True)
