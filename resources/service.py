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

    dict_final = {}
    for d in disciplinas:

        dict_turmas = {}
        for t in d['Turmas']:
            dict_turmas[t['CodigoTurma']] = {
                    'prof': t['Professor'],
                    'horarios_str': ", ".join(t['Horario']),
                    #'horarios': [s.split('-')[0] for s in t['Horario']],
                    #'salas': [s.split('-')[1] for s in t['Horario']]
                }

        dict_final[d['CodigoDisciplina']] = {
                #'idcurso': d['IdCurso'],
                'nome': d['NomeDisciplina'],
                'aulas': d['NumAulas'],
                'turmas': dict_turmas
            }

    dict_ordered =  sorted(dict_final.items(), key=lambda x: x[1]['nome'])

    return dict_final


def montar_grades(obj):
    print(obj)
    size = len(obj.items())
    print(size)
    for i in range(size):
        print(obj[i])

def get_grades(data):
    idcurso = data['idCurso']
    dictTurmas = data['dicts']
    listDisc = list(dictTurmas.keys())
    disciplinas = get_turmas_by_curso_and_disc(idcurso, listDisc)

    dict_final = {}
    for d in disciplinas:

        dict_turmas = {}
        turmas_filtradas = [t for t in d['Turmas'] if t['CodigoTurma'] in dictTurmas[d['CodigoDisciplina']]]
        for t in turmas_filtradas:
            dict_turmas[t['CodigoTurma']] = {
                    'prof': t['Professor'],
                    'horarios_str': ", ".join(t['Horario']),
                    #'horarios': [s.split('-')[0] for s in t['Horario']],
                    #'salas': [s.split('-')[1] for s in t['Horario']]
                }

        dict_final[d['CodigoDisciplina']] = {
                #'idcurso': d['IdCurso'],
                'nome': d['NomeDisciplina'],
                'aulas': d['NumAulas'],
                'turmas': dict_turmas
            }

    montar_grades(dict_final)

    return dict_final
