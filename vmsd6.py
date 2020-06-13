import numpy as np
import random


def pesos(nentrada, noculta, nsaida):
    w1 = np.zeros((noculta, nentrada))
    w2 = np.zeros((nsaida, noculta))
    for c in range(noculta):
        for cc in range(nentrada):
            w1[c][cc] = random.normalvariate(0, 1)
    for a in range(nsaida):
        for aa in range(noculta):
            w2[a][aa] = random.normalvariate(0, 1)
    return w1, w2


def bias(noculta, nsaida):
    b1 = np.ones((noculta, 1))
    b2 = np.ones((nsaida, 1))
    for a in range(noculta):
        b1[a][0] = random.random()
    for aa in range(nsaida):
        b2[aa][0] = random.random()
    return b1, b2


def funcao_ativacao(v):
    f = 1 / (1 + np.exp(-v))
    return f


def treinamento(n_entrada, n_oculta, n_saida, x, amostra, w1, w2, b1, b2):

    erro_rede = np.zeros(n_saida)
    # camada oculta
    res_oculto = np.zeros((n_oculta, 1))
    for neuronio_oculto in range(len(w1)):
        soma = 0
        for c in range(n_entrada):
            soma = soma + x[c][amostra] * w1[neuronio_oculto][c]
        v_oculto = soma + b1[neuronio_oculto][0]
        res_oculto[neuronio_oculto][0] = funcao_ativacao(v_oculto)

    # camada de saída
    y = np.zeros((n_saida, 1))
    for neuronio_saida in range(len(w2)):
        soma2 = 0
        for cc in range(len(res_oculto)):
            soma2 = soma2 + res_oculto[cc][0] * w2[neuronio_saida][cc]
        v_saida = soma2 + b2[neuronio_saida][0]
        y[neuronio_saida][0] = funcao_ativacao(v_saida)
        erro_rede[neuronio_saida] = (y[neuronio_saida][0] - d[neuronio_saida][amostra])**2

    # backpropagation: camada de saída -> camada oculta
    delta_saida = np.zeros((n_saida, n_oculta))
    for neuronio_saida in range(len(w2)):
        for cc in range(len(res_oculto)):
            delta_saida[neuronio_saida][cc] = (y[neuronio_saida][0] - d[neuronio_saida][amostra]) * y[neuronio_saida][0] * (1 - y[neuronio_saida][0])
            w2[neuronio_saida][cc] = w2[neuronio_saida][cc] - (((y[neuronio_saida][0] - d[neuronio_saida][amostra]) * y[neuronio_saida][0] * (1 - y[neuronio_saida][0])) * res_oculto[cc][0] * taxa_de_aprendizagem)
            b2[neuronio_saida][0] = b2[neuronio_saida][0] - (y[neuronio_saida][0] - d[neuronio_saida][amostra]) * y[neuronio_saida][0] * (1 - y[neuronio_saida][0]) * taxa_de_aprendizagem

    # backpropagation: camada oculta -> camada de entrada
    for neuronio_saida in range(len(w2)):
        soma3 = 0
        for c in range(len(res_oculto)):
            soma3 = soma3 + delta_saida[neuronio_saida][c] * w2[neuronio_saida][c]
        for neuronio_oculto in range(len(w1)):
            for i in range(len(x)-1):
                w1[neuronio_oculto][i] = w1[neuronio_oculto][i] - (taxa_de_aprendizagem * (res_oculto[neuronio_oculto][0] * (1 - res_oculto[neuronio_oculto][0]) * soma3) * x[i][amostra])
                b1[neuronio_oculto][0] = b1[neuronio_oculto][0] - (taxa_de_aprendizagem * (res_oculto[neuronio_oculto][0] * (1 - res_oculto[neuronio_oculto][0]) * soma3))

    return erro_rede


def simulacao(n_entrada, n_oculta, n_saida, x, amostra, w1, w2, b1, b2):
    # camada oculta
    res_oculto = np.zeros((n_oculta, 1))
    for neuronio_oculto in range(len(w1)):
        soma = 0
        for c in range(n_entrada):
            soma = soma + x[c][amostra] * w1[neuronio_oculto][c]
        v_oculto = soma + b1[neuronio_oculto][0]
        res_oculto[neuronio_oculto][0] = funcao_ativacao(v_oculto)

    # camada de saída
    y = np.zeros((n_saida, 1))
    for neuronio_saida in range(len(w2)):
        soma2 = 0
        for cc in range(len(res_oculto)):
            soma2 = soma2 + res_oculto[cc][0] * w2[neuronio_saida][cc]
        v_saida = soma2 + b2[neuronio_saida][0]
        y[neuronio_saida][0] = funcao_ativacao(v_saida)
    return y


# main
# Parâmetros
n_entrada = 8
n_oculta = 30
n_saida = 3
taxa_de_aprendizagem = 0.01
epocas = 10000

amostra = 9  # só para treinamento
x = [[1.0, 1.0, 0.0, 0.0, 0.7, 0.7, 0.4, 0.4, 0.4],
     [1.0, 1.0, 0.6, 0.6, 0.0, 0.0, 0.3, 0.3, 0.3],
     [0.0, 0.0, 0.5, 0.5, 0.6, 0.6, 1.0, 1.0, 1.0],
     [0.5, 0.5, 0.6, 0.6, 0.0, 0.0, 1.0, 1.0, 1.0],
     [0.2, 0.2, 0.6, 0.6, 1.0, 1.0, 0.0, 0.0, 0.0],
     [0.5, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0],
     [1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0],
     [0.2, 0.8, 0.7, 1.0, 0.8, 1.0, 0.0, 0.4, 0.7]]

d = [[0.7, 0.5, 0.8, 0.6, 0.0, 0.0, 1.0, 0.4, 0.3],
     [0.3, 0.1, 0.0, 0.0, 0.3, 0.3, 0.9, 1.0, 1.0],
     [0.7, 1.0, 0.9, 1.0, 1.0, 1.0, 0.0, 0.1, 0.2]]
w1, w2 = pesos(n_entrada, n_oculta, n_saida)
b1, b2 = bias(n_oculta, n_saida)

a = 0
erro = np.zeros(amostra)
while True:
    a = a + 1
    for i in range(amostra):
        soma_erro = treinamento(n_entrada, n_oculta, n_saida, x, i, w1, w2, b1, b2)
        erro[i] = (1/2) * sum(soma_erro)
    erro_med = (1/len(erro)) * sum(erro)
    if a > epocas or erro_med < 0.01:
        break

# teste
amostra2 = 1
xx = np.zeros((n_entrada, amostra2))
pirolise = [0.4, 0.3, 1.0, 1.0, 0.0, 1.0, 0.0, 0.2]
for w in range(n_entrada):
    xx[w][0] = pirolise[w]
acerto = 0
erro_resposta = 0
for k in range(amostra2):
    resposta = simulacao(n_entrada, n_oculta, n_saida, xx, k, w1, w2, b1, b2)
print(resposta)
