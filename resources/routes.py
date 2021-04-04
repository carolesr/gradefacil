from flask import Blueprint, jsonify, request
from resources.service import *

controller = Blueprint('controller', __name__)

@controller.route('/test')
def test():
    return jsonify({'deu': 'certo'})

@controller.route('/getcursos', methods=['GET'])
def get_c():
    print('getcursos')
    result = get_all_cursos()
    return jsonify(result)

@controller.route('/getdisciplinas', methods=['GET'])
def get_d():
    id = request.args.get('id')
    print('/getdisciplinas')
    result = get_all_disciplinas_by_curso(id)
    return jsonify(result)

@controller.route('/getgrades', methods=['GET', 'POST'])
def get_g():
    print('/getgrades')
    data = request.get_json()
    result = get_grades(data)
    return jsonify(result)