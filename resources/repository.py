from pymongo import MongoClient

client = MongoClient('mongodb://momomo:bb2106@gradefacil-shard-00-00.m83gc.mongodb.net:27017,gradefacil-shard-00-01.m83gc.mongodb.net:27017,gradefacil-shard-00-02.m83gc.mongodb.net:27017/gradefacil?ssl=true&replicaSet=atlas-lf4nte-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.gradefacil
tb_cursos = db.Cursos
tb_disciplinas = db.Disciplinas

def get_cursos():
    result = tb_cursos.find()
    return result

def get_disciplinas_by_curso(id):
    result = tb_disciplinas.find({'IdCurso': id})
    return result

def get_turmas_by_curso_and_disc(idcurso, listDisc):
    result = tb_disciplinas.find({'IdCurso':idcurso, 'CodigoDisciplina': { "$in": listDisc}})
    return result