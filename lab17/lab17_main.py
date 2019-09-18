import sys, os
sys.path.insert(0,os.getcwd())
import lab17 as lab

n = int(input())

cidades = []
for i in range(0, n):
    x, y, inicioCEP, fimCEP, numHabitantes = input().split(' ')
    cidades.append(lab.Cidade(lab.Ponto(float(x), float(y)), int(inicioCEP), int(fimCEP), int(numHabitantes)))

q = int(input())

for i in range(0, q):
    print("Consulta {}:".format(i))

    consulta = tuple(map(int, input().split(' ')))
    if consulta[0] == 0:
        res = lab.consulta_cidade_por_cep(cidades, consulta[1])
        if res is None:
            print("Nao ha uma cidade com o CEP {}".format(consulta[1]))
        else:
            print("Cidade com CEP {}: {}".format(consulta[1], res))
    elif consulta[0] == 1:
        print("Cidades no raio de {:.0f}:".format(consulta[2]))
        for c in lab.consulta_cidades_por_raio(cidades, consulta[1], consulta[2]):
            print(c)
    elif consulta[0] == 2:
        print("Populacao total: {}".format(lab.populacao_total(cidades, consulta[1], consulta[2])))
    else:
        print("Mediana da populacao: {:.1f}".format(lab.mediana_da_populacao(cidades, consulta[1], consulta[2])))
