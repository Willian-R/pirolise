import random
import numpy as np
import matplotlib.pyplot as plt
import db


class RedeNeural:

    def pesos(nentrada, noculta, nsaida):
        """Função que gera aleatoriamente o valor dos pesos
        :returns w1 - pesos da camada oculta, w2 - pesos da camada de saída"""

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
        """Função que gera aleatoriamente o bias para as camadas da rede
        :returns b1 - bias dos neurônios da camada oculta, b2 - bias dos neurônios da camada de saída"""

        b1 = np.ones((noculta, 1))
        b2 = np.ones((nsaida, 1))
        for a in range(noculta):
            b1[a][0] = random.random()
        for aa in range(nsaida):
            b2[aa][0] = random.random()
        return b1, b2

    def funcao_ativacao(v):
        """Função para a função de ativação sigmoide
        :return f - resultado da aplicação do campo local induzido na função de ativação"""

        f = 1 / (1 + np.exp(-v))
        return f

    def treinamento(n_entrada=9, n_oculta=10, n_saida=3, amostra=28, taxa_de_aprendizagem=0.01, epocas=10000):
        """Função para treinamento da rede neural
        :returns w1, w2, b1, b2 - sendo pesos e bias atualizados da camada oculta e da camada de saída. \
        True - identificando o fim do treinamento"""

        # pegas os dados de entrada e target do banco de dados
        x, d = db.BancoDeDados.pegadados()
        # cria os pesos e bias da camada oculta e de saída
        w1, w2 = RedeNeural.pesos(n_entrada, n_oculta, n_saida)
        b1, b2 = RedeNeural.bias(n_oculta, n_saida)
        erro_rede = np.zeros(n_saida)
        a = 0
        erro = np.zeros(amostra)
        eixo_x = list()
        eixo_y = list()

        # roda os dados de treianemento até que a condição de parada seja satisfeita
        while True:
            a = a + 1
            for i in range(amostra):

                # camada oculta
                res_oculto = np.zeros((n_oculta, 1))
                for neuronio_oculto in range(len(w1)):
                    soma = 0
                    for c in range(n_entrada):
                        soma = soma + x[c][i] * w1[neuronio_oculto][c]
                    v_oculto = soma + b1[neuronio_oculto][0]
                    res_oculto[neuronio_oculto][0] = RedeNeural.funcao_ativacao(v_oculto)

                # camada de saída
                y = np.zeros((n_saida, 1))
                for neuronio_saida in range(len(w2)):
                    soma2 = 0
                    for cc in range(len(res_oculto)):
                        soma2 = soma2 + res_oculto[cc][0] * w2[neuronio_saida][cc]
                    v_saida = soma2 + b2[neuronio_saida][0]
                    y[neuronio_saida][0] = RedeNeural.funcao_ativacao(v_saida)
                    erro_rede[neuronio_saida] = (y[neuronio_saida][0] - d[neuronio_saida][i]) ** 2
                    erro[i] = (1 / 2) * sum(erro_rede)

                # backpropagation: camada de saída -> camada oculta
                delta_saida = np.zeros((n_saida, n_oculta))
                for neuronio_saida in range(len(w2)):
                    for cc in range(len(res_oculto)):
                        delta_saida[neuronio_saida][cc] = (y[neuronio_saida][0] - d[neuronio_saida][i]) * \
                                                          y[neuronio_saida][0] * (1 - y[neuronio_saida][0])
                        w2[neuronio_saida][cc] = w2[neuronio_saida][cc] - (((y[neuronio_saida][0] - d[neuronio_saida][
                            i]) * y[neuronio_saida][0] * (1 - y[neuronio_saida][0])) * res_oculto[cc][
                                                                               0] * taxa_de_aprendizagem)
                        b2[neuronio_saida][0] = b2[neuronio_saida][0] - (y[neuronio_saida][0] - d[neuronio_saida][i]) *\
                                                y[neuronio_saida][0] * (1 - y[neuronio_saida][0]) * taxa_de_aprendizagem

                # backpropagation: camada oculta -> camada de entrada
                for neuronio_saida in range(len(w2)):
                    soma3 = 0
                    for c in range(len(res_oculto)):
                        soma3 = soma3 + delta_saida[neuronio_saida][c] * w2[neuronio_saida][c]
                    for neuronio_oculto in range(len(w1)):
                        for ii in range(len(x) - 1):
                            w1[neuronio_oculto][ii] = w1[neuronio_oculto][ii] - (taxa_de_aprendizagem * (
                                        res_oculto[neuronio_oculto][0] * (1 - res_oculto[neuronio_oculto][0]) * soma3) * x[ii][
                                                                                   i])
                            b1[neuronio_oculto][0] = b1[neuronio_oculto][0] - (taxa_de_aprendizagem * (
                                        res_oculto[neuronio_oculto][0] * (1 - res_oculto[neuronio_oculto][0]) * soma3))

            erro_med = (1 / len(erro)) * sum(erro)
            eixo_y.append(erro_med)
            eixo_x.append(a)

            # condição de parada para o treinamento
            if a > epocas or erro_med < 0.01:
                break
        print(erro_med)
        # gera o gráfico curva de aprendizagem
        plt.plot(eixo_x, eixo_y)
        plt.xlabel('Épocas')
        plt.ylabel('Erro médio quadrático')
        plt.title('Curva de aprendizagem')
        plt.show()
        return w1, w2, b1, b2, True

    def simulacao(x, w1, w2, b1, b2):
        """função que prediz os produtos da pirólise
        :parameter n_entrada, n_oculta, n_saida, amostra, w1, w2, b1, b2
        :returns y = lista com os valores normalizados de saída"""
        n_entrada = 9
        n_oculta = 10
        n_saida = 3

        # camada oculta
        res_oculto = np.zeros((n_oculta, 1))
        for neuronio_oculto in range(len(w1)):
            soma = 0
            for c in range(n_entrada):
                soma = soma + x[c] * w1[neuronio_oculto][c]
            v_oculto = soma + b1[neuronio_oculto][0]
            res_oculto[neuronio_oculto][0] = RedeNeural.funcao_ativacao(v_oculto)

        # camada de saída
        y = np.zeros((n_saida, 1))
        for neuronio_saida in range(len(w2)):
            soma2 = 0
            for cc in range(len(res_oculto)):
                soma2 = soma2 + res_oculto[cc][0] * w2[neuronio_saida][cc]
            v_saida = soma2 + b2[neuronio_saida][0]
            y[neuronio_saida][0] = RedeNeural.funcao_ativacao(v_saida)
        return y
