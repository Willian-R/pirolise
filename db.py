import sqlite3
from uteis import *
cel = list()
hemi = list()
lig = list()
umidade = list()
mv = list()
cinzas = list()
cf = list()
temp = list()
tx = list()
bio = list()
oleo = list()
gas = list()


class BancoDeDados:

    def pegadados():
        # cria a conexão com o banco de dados
        conexao = sqlite3.connect('pirolise.db')
        c = conexao.execute('select * from dados')
        dados = c.fetchall()

        for i in range(12):
            for j in range(len(dados)):
                if i == 0:
                    cel.append(dados[j][i])
                elif i == 1:
                    hemi.append(dados[j][i])
                elif i == 2:
                    lig.append(dados[j][i])
                elif i == 3:
                    umidade.append(dados[j][i])
                elif i == 4:
                    mv.append(dados[j][i])
                elif i == 5:
                    cinzas.append(dados[j][i])
                elif i == 6:
                    cf.append(dados[j][i])
                elif i == 7:
                    temp.append(dados[j][i])
                elif i == 8:
                    tx.append(dados[j][i])
                elif i == 9:
                    bio.append(dados[j][i])
                elif i == 10:
                    oleo.append(dados[j][i])
                elif i == 11:
                    gas.append(dados[j][i])
        cel_n = normalizar(cel)
        hemi_n = normalizar(hemi)
        lig_n = normalizar(lig)
        umidade_n = normalizar(umidade)
        mv_n = normalizar(mv)
        cinzas_n = normalizar(cinzas)
        cf_n = normalizar(cf)
        temp_n = normalizar(temp)
        tx_n = normalizar(tx)
        bio_n = normalizar(bio)
        oleo_n = normalizar(oleo)
        gas_n = normalizar(gas)
        entrada_t = [cel_n, hemi_n, lig_n, umidade_n, mv_n, cinzas_n, cf_n, temp_n, tx_n]
        target = [bio_n, oleo_n, gas_n]
        c.close()
        return entrada_t, target

    def guardarDados(peso1, peso2, bias1, bias2):
        try:
            conexao = sqlite3.connect('pirolise.db')
            c = conexao.cursor()
            try:
                c.executemany('INSERT INTO w1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', peso1)
            except:
                print('Deu erro w1')
            try:
                c.executemany('INSERT INTO w2 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                          '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                          '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                          '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                          '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                          '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                          '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', peso2)
            except:
                print('Deu erro w2')
            try:
                c.executemany('INSERT INTO b1 VALUES (?)', bias1)
            except:
                print('Deu erro b1')
            try:
                c.executemany('INSERT INTO b2 VALUES (?)', bias2)
            except:
                print('Deu erro b2')
            conexao.commit()
        except:
            print('DEU ERRO conexão')
        finally:
            c.close()
