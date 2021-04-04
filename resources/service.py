from resources.repository import *

def get_all_cursos():
    cursos = get_cursos()
    listResult = []
    for c in cursos:
        obj = {'guid': str(c['_id']), 'Id': c['Id'], 'NomeCurso':c['NomeCurso']}
        listResult.append(obj)
    return listResult

def get_all_disciplinas_by_curso(id):
    disciplinas = get_disciplinas_by_curso(id)
    listResult = []
    for d in disciplinas:
        obj = {
            'guid': str(d['_id']), 
            'IdCurso': d['IdCurso'],
            'NomeDisciplina': d['NomeDisciplina'],
            'CodigoDisciplina': d['CodigoDisciplina'],
            'NumAulas': d['NumAulas'],
            'Turmas': d['Turmas']
        }
        listResult.append(obj)
    return listResult

def get_grades(data):
    idcurso = data['idCurso']
    dictTurmas = data['dicts']
    listDisc = list(dictTurmas.keys())
    print(listDisc)
    disciplinas = get_turmas_by_curso_and_disc(idcurso, listDisc)

    listFinal = []
    for d in disciplinas:
        obj = {
            'guid': str(d['_id']), 
            'IdCurso': d['IdCurso'],
            'NomeDisciplina': d['NomeDisciplina'],
            'CodigoDisciplina': d['CodigoDisciplina'],
            'NumAulas': d['NumAulas'],
            'Turmas': [t for t in d['Turmas'] if t['CodigoTurma'] in dictTurmas[d['CodigoDisciplina']]]  #d['Turmas']
        }
        listFinal.append(obj)

    return listFinal
