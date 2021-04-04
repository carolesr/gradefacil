{
materias: [
    calculo = {
        'codigo' : 'cs010',
        'turmas' : [
            {
                'turma':'s71',
                'horario': ['t1', 't2', 't3']
            },
            {
                'turma':'s72',
                'horario': ['n1', 'n2', 'n3']
            }
        ]
    },
    prog = {
        'codigo' : 'cs010',
        'turmas' : [
            {
                'turma':'s51',
                'horario': ['t2', 't3', 't4']
            },
            {
                'turma':'s52',
                'horario': ['m1', 'm2', 'm3']
            },
            {
                'turma':'s53',
                'horario': ['m1', 'm2', 'm3']
            }
        ]
    }
]}

list_materias = [calculo, prog]

turmas_calculo = calculo['turmas']
turmas_prog = prog['turmas']

# for n1 in range(len(turmas_calculo)):
#     for n2 in range(len(turmas_prog)):
#         tc = turmas_calculo[n1]['turma']
#         tp = turmas_prog[n2]['turma']
#         print(tc + tp)

num_total = len(turmas_calculo) * len(turmas_prog)
print(num_total)
factor_calculo = num_total / len(turmas_calculo)
print(round(factor_calculo))
factor_prog = num_total / len(turmas_prog)
print(round(factor_prog))

for i in range(1,num_total+1):
    # print(round(int((i/factor_calculo) + 0.5)))
    print(i/factor_prog)
    print(round(i/factor_prog))