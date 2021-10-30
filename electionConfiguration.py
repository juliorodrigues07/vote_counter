import os
from datetime import datetime

# Diretório
saida = '/Cargas/'

# Nome dos arquivos de configuração da eleição
now = datetime.now()
out_file_name = 'Configuracao da Eleicao' + ' - Data ' + (str(now.date()) + ' ' + str(now.hour) + '_' +
                                                        str(now.minute) + '_' + str(now.second) + '.txt')

def configElection():
    
    cargos = []

    while True:
        try:
            qtd_cargos = int(input("Digite a quantidade de cargos:"))
            break
        except ValueError:
            print('Insira valores inteiros válidos!')

    i = 0
    while i < qtd_cargos:
        
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
        
        aux.clear
        i = i + 1

    cargos.sort()

    # O diretótio '/Cargas/' é criado caso não exista
    if not os.path.isdir(os.getcwd() + saida):
        os.mkdir(os.getcwd() + saida)

    # Gera o arquivo de configuração da eleição no diretório destino
    with open(os.getcwd() + saida + out_file_name, 'w') as arquivo:
        for item in cargos:
            arquivo.write(str(item[2]) + ' ' + str(item[1]) + '\n')

    return out_file_name, qtd_cargos


def readConfigFile(file_name, qtd_cargos):

    #layout_boleta = []
    cargos, campos = [], []
    linhas = 0

    with open(os.getcwd() + saida + file_name, 'r') as arquivo:
        info = arquivo.readlines()
        info = [x.strip() for x in info]

    for i in range(qtd_cargos):
        
        #layout_boleta.append((info[i][:1], info[i][2:]))
        cargos.append(info[i][2:])
        linhas += int(info[i][:1])

        if i == 0:
            campos.append(int(info[i][:1]))
        else:
            campos.append(campos[i - 1] + int(info[i][:1]))

    # print(layout_boleta)
    return cargos, linhas, campos

    
if __name__ == '__main__':

    file, qtd = configElection()
    cargos, linhas, campos = readConfigFile(file, qtd)

    print(cargos)
    print(linhas)
    print(campos)