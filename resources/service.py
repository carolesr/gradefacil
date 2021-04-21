from resources.repository import *

def get_all_cursos():
    cursos = get_cursos()
    listResult = []
    for c in cursos:
        obj = {'Id': c['IdCurso'], 'NomeCurso':c['NomeCurso']}
        listResult.append(obj)

    return listResult

def get_all_disciplinas_by_curso(id):
    disciplinas = get_disciplinas_by_curso(id)
    listResult = []
    for d in disciplinas:
        listTurmas = []
        for t in d['Turmas']:
            obj_turma = {
                t['CodigoTurma']: {
                    'prof': t['Professor'],
                    'horarios_str': ", ".join(t['Horario']),
                    'horarios': [s.split('-')[0] for s in t['Horario']],
                    'salas': [s.split('-')[1] for s in t['Horario']]
                }
            }
            listTurmas.append(obj_turma)
        obj_disc = { 
            d['CodigoDisciplina']: {
                'IdCurso': d['IdCurso'],
                'nome': d['NomeDisciplina'],
                'aulas': d['NumAulas'],
                'turmas': listTurmas
            }
        }
        listResult.append(obj_disc)

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
            'IdCurso': d['IdCurso'],
            'NomeDisciplina': d['NomeDisciplina'],
            'CodigoDisciplina': d['CodigoDisciplina'],
            'NumAulas': d['NumAulas'],
            'Turmas': [t for t in d['Turmas'] if t['CodigoTurma'] in dictTurmas[d['CodigoDisciplina']]]  #d['Turmas']
        }
        listFinal.append(obj)

    return listFinal
