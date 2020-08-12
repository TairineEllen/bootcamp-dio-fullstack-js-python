from flask_restful import Resource

habilidades = ['Python', 'Java', 'Django']

class Habilidades(Resource):
    def get(self):
        return habilidades
