import os
from datetime import datetime
import json

now = datetime.now()
out_file_name = 'Configuracao da Eleicao' + ' - Data ' + (str(now.date()) + ' ' + str(now.hour) + '_' +
                                                          str(now.minute) + '_' + str(now.second) + '.txt')

stat = '/Static'
saida = '/Cargas/'

if not os.path.isdir(os.getcwd() + stat):
    os.mkdir(os.getcwd() + stat)
if not os.path.isdir(os.getcwd() + stat + saida):
    os.mkdir(os.getcwd() + stat + saida)


def configElection():
    cargos = []
    json_config = {}
    while True:
        try:
            nome_eleicao = str(input("Digite o nome da eleição:"))
            qtd_cargos = int(input("Digite a quantidade de cargos:"))
            break
        except ValueError:
            print('Insira valores inteiros válidos!')

    i = 0
    lis = []
    while i < qtd_cargos:
        dic = {}
        aux = []

        nome = str(input("Digite o nome do cargo: "))

        while True:
            try:
                ordem = int(input('Digite a ordem em que tal cargo deve ser exibido na boleta: '))
                digitos = int(input("Digite a quantidade de digitos do cargo: "))
                break
            except ValueError:
                print('Insira valores inteiros válidos!')
        aux.append(ordem)
        aux.append(nome)
        aux.append(digitos)
        cargos.append(aux)
        dic['Nome'] = nome
        dic['Digitos'] = digitos
        dic['Ordem'] = ordem

        aux.clear
        i = i + 1
        lis.append(dic)
    cargos.sort()
    auxiliar = {}
    print(lis)
    json_config[nome_eleicao]= lis
    nomeEle = nome_eleicao + ' - ' + out_file_name
    # Gera o arquivo de configuração da eleição no diretório destino
    json_object = json.dumps(json_config, indent=4)
    with open(os.getcwd() + stat + saida + nomeEle+'.json', 'w') as arquivo:
            arquivo.write(json_object)

    return nomeEle, qtd_cargos


def readConfigFile(file_name):
    cargos, digito, pos = [], [], []
    linhas = 0

    with open(os.getcwd() + stat + saida + file_name, 'r') as arquivo:
        info = arquivo.readlines()
        info = [x.strip() for x in info]
        for elem in info:
            aux = elem.split(' ')
            cargos.append(aux[0])
            digito.append(aux[1])
            pos.append(aux[2])
    return cargos, digito, pos


if __name__ == '__main__':
    file, qtd = configElection()
    #cargos, linhas, campos = readConfigFile(file)


