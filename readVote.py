# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np
import sys
import os

FONTE = cv.FONT_HERSHEY_SIMPLEX
PROPORCAO_BARRA = 130.0
# PROPORCAO_BARRA = 213.0


def mostrar(titulo, imagem):
    cv.imshow(titulo, imagem)
    cv.waitKey(0)


def run2(boleta):
    
    posicaoQuadrados = list()
    tam_pincel = int(round(boleta.shape[1] / PROPORCAO_BARRA))
    #print(tam_pincel)

    # Boleta em escala cinza
    boleta_cinza = cv.cvtColor(boleta, cv.COLOR_BGR2GRAY)

    # Boleta em escala cinza borrada
    boleta_blur = cv.GaussianBlur(boleta_cinza, (tam_pincel, tam_pincel), 0)

    # Boleta em escala cinza borrada e binarizada
    ret, boleta_binaria = cv.threshold(
        boleta_blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # mostrar('Binaria', boleta_binaria)
    cont, hier = cv.findContours(
        boleta_binaria, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    for c in cont:
        
        perimetro = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.04 * perimetro, True)
        cv.drawContours(boleta, [c], -1, (0, 255, 0), 1)
        x, y, w, h = cv.boundingRect(c)

        if len(approx) == 3:
            forma = "Triangulo"

        elif len(approx) == 4:
            forma = "Quadrado" if (
                w/h) >= 0.95 and (w/h) <= 1.05 else "Retangulo"

        elif len(approx) == 5:
            forma = "Pentagono"

        else:
            forma = "Circulo"

        if forma == 'Quadrado' or forma == 'Retangulo':
            posicaoQuadrados.append(tuple((x, y, w, h)))
            cv.putText(boleta, str(x) + '-' + str(y) + '-' + forma, (x, y),
                       FONTE, 0.35, (0, 255, 0), 1, cv.LINE_AA)

    cv.imshow('Boleta', boleta)
    cv.waitKey(0)

    posicaoQuadrados.sort(key = lambda x : x[1], reverse = True)
    # print('posicaoQuadrados ', posicaoQuadrados)
    quadradoFinal = list()
    quadradoFinal.append(posicaoQuadrados.pop(0))
    quadradoFinal.append(posicaoQuadrados.pop(0))
    quadradoFinal.sort(key = lambda x : x[0])

    menor_x = quadradoFinal[0][0]
    maior_x = quadradoFinal[1][0]
    maior_y = quadradoFinal[0][1]
    # print(menor_x)

    distanciaTotal = maior_x - menor_x
    distanciaUnitaria_x = distanciaTotal / 11
    erro = int(0.2 * distanciaUnitaria_x)

    i = 0
    while(i < len(posicaoQuadrados)):
        if posicaoQuadrados[i][0] > maior_x:
            del(posicaoQuadrados[i])
        else:
            i = i + 1

    # Identificando os campos de votos
    pos_campo = list()
    colunas = list()

    for i in posicaoQuadrados:
        if len(pos_campo) == 0:
            pos_campo.append(i[1])
        elif(len(pos_campo) != 8):
            if (pos_campo[-1] > i[1] + erro) or (pos_campo[-1] < i[1] - erro):
                pos_campo.append(i[1])
                if len(pos_campo) == 8:
                    colunas.append(i[0])
        else:
            if len(colunas) != 13:
                if (i[1] == pos_campo[-1]):
                    colunas.append(i[0])

    menor_y = pos_campo[-1]
    distanciaTotal_y = maior_y - menor_y
    distanciaUnitaria_y = int(distanciaTotal_y / 12)

    i = 0
    while (i < len(posicaoQuadrados)):
        if (posicaoQuadrados[i][0] < (menor_x + erro)) or (posicaoQuadrados[i][1] < (menor_y + erro)) or (posicaoQuadrados[i][0] > maior_x):  # (50   450)
            del(posicaoQuadrados[i])
        else:
            i = i + 1

    posicaoQuadrados.sort(key = lambda x : x[1])

    matriz = construct_matrix(posicaoQuadrados, distanciaUnitaria_y, distanciaUnitaria_x, menor_x, menor_y, maior_y)
    # print(matriz)
    
    print('Implementação - Paulo')
    imprime_votos1(matriz)

    print('\nImplementação - Julio')
    presidente, deputado = imprime_votos2(matriz)

    return ''.join(presidente), ''.join(deputado)
    

def construct_matrix(posicaoQuadrados, distanciaUnitaria_y, distanciaUnitaria_x, menor_x, menor_y, maior_y):

    matrix = np.zeros((7, 10))

    # Correções para a identificação dos votos nos campos
    salto = distanciaUnitaria_y * 2
    y_atual = menor_y + salto
    erro_y = 0.2 * distanciaUnitaria_y

    i = 0
    # Analisa a boleta de cima para baixo
    while y_atual < maior_y:
        for square in posicaoQuadrados:
            
            # Checagem da existência de retângulos na linha atual
            if square[1] > y_atual + distanciaUnitaria_y + erro_y:
                break
            
            # Marcação do voto na matriz
            coluna = int(round((square[0] - menor_x) / float(distanciaUnitaria_x)) - 1)
            matrix[i][coluna] = 1
            del(posicaoQuadrados[0])
        
        # Passagem para a próxima linha dos campos de votos e da matriz
        y_atual += distanciaUnitaria_y
        i += 1

        # Salto entre os campos de votos de presidente e deputado
        if i == 2:
            y_atual += salto

    return matrix


# Implementação da leitura dos votos da matriz --- Paulo
def imprime_votos1(m):

    # Matriz de teste
    # m = [[0,0,1,0,0,0,0,0,0,0],
    #     [0,0,0,0,1,0,0,0,0,0,],
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [1,0,0,0,0,0,0,0,0,0],
    #     [0,1,0,0,0,0,0,0,0,0]]
    
    presidente = ""
    deputado = ""
    cont = 0
    flag = 0

    while cont < 2 and flag == 0:
        invalido = 0
        con = 0
        while con < 10:
            if m[cont][con] == 0:
                con = con + 1
                continue
            if m[cont][con] == 1:
                invalido = invalido + 1
                if con == 9:
                    presidente = presidente + str(0)
                else:
                    presidente = presidente + str(con + 1)
                    con = con + 1
        if invalido != 1:
            presidente = 'Voto invalido'
        cont = cont + 1
    flag = 0

    while cont < 7 and flag == 0:
        invalido = 0
        con = 0
        while con < 10:
            if m[cont][con] == 0:
                con = con + 1
                continue
            if m[cont][con] == 1:
                invalido = invalido + 1
                if con == 9:
                    deputado = deputado + str(0)
                    con = con + 1
                else:
                    deputado = deputado + str(con + 1)
                    con = con + 1
        if invalido != 1:
            deputado = " Voto invalido"
            flag = 1

        cont = cont + 1
        
    print(f"Presidente: {presidente}\n Deputado:{deputado}")


# Implementação da leitura dos votos da matriz --- Julio
def imprime_votos2(matriz):

    # Matriz de teste (Boleta teste.jpg)
    # matriz = np.zeros((7, 10))
    # matriz[0][0] = 1
    # matriz[0][3] = 1
    # matriz[0][6] = 1
    # matriz[1][4] = 1
    # matriz[4][5] = 1

    presidente = []
    deputado = []
    
    # Matriz para checagem da ocorrência de dígitos por linha
    check = np.zeros((len(matriz), 2))

    i = 0
    while i < (len(matriz)):
        for j in range(len(matriz[0])):

            if matriz[i][j]:
                
                # Acumula a ocorrência de retângulos na linha atual da matriz
                check[i][0] += 1
                
                # Caso em que existam dois ou mais retângulos na mesma linha
                if i < 2 and check[i][0] > 1:
                    i = 1
                    break
                elif i >= 2 and check[i][0] > 1:
                    i = len(matriz)
                    break
                
                # Armazena os dígitos do voto
                if j != len(matriz[0]) - 1:
                    check[i][1] = j + 1
                else:
                    check[i][1] = 0
                

            # Caso em que exista(m) linha(s) em branco nos campos da boleta
            if i < 2 and j == len(matriz[0]) - 1 and check[i][0] == 0:
                i = 1
                break
            elif i >= 2 and j == len(matriz[0]) - 1 and check[i][0] == 0:
                i = len(matriz)
                break

        i += 1

    #print(check)

    # Se foram identificadas 2 ou mais marcações na mesma linha dos campos, o voto é "descartado"
    i = 0
    while i < len(check):

        if i < 2 and check[i][0] == 1:
            presidente.append(str(int(check[i][1])))

        elif i < 2 and check[i][0] != 1:
            del(presidente[:])
            i = 2
            continue

        elif i >= 2 and check[i][0] == 1:
            deputado.append(str(int(check[i][1])))

        else:
            del(deputado[:])
            break

        i += 1

    return ''.join(presidente), ''.join(deputado)


if __name__ == '__main__':
    # TODO: Adicionar verificação de existencia de arquivo
    #boleta = cv.imread(os.getcwd() + '/Examples/GenerateVideo/boletaVoto.jpg')
    boleta = cv.imread(os.getcwd() + '/UrnaFisica/voto.jpg')

    # print(run('UrnaFisica/voto.jpg'))

    # TODO: Mudar print para imprimir resultado
    print(run2(boleta))
