import sqlite3
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

    def normalizar(v):
        resp = list()
        for c in v:
            r = (c - min(v)) / (max(v) - min(v))
            resp.append(r)
        return resp

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
        cel_n = BancoDeDados.normalizar(cel)
        hemi_n = BancoDeDados.normalizar(hemi)
        lig_n = BancoDeDados.normalizar(lig)
        umidade_n = BancoDeDados.normalizar(umidade)
        mv_n = BancoDeDados.normalizar(mv)
        cinzas_n = BancoDeDados.normalizar(cinzas)
        cf_n = BancoDeDados.normalizar(cf)
        temp_n = BancoDeDados.normalizar(temp)
        tx_n = BancoDeDados.normalizar(tx)
        bio_n = BancoDeDados.normalizar(bio)
        oleo_n = BancoDeDados.normalizar(oleo)
        gas_n = BancoDeDados.normalizar(gas)
        entrada_t = [cel_n, hemi_n, lig_n, umidade_n, mv_n, cinzas_n, cf_n, temp_n, tx_n]
        target = [bio_n, oleo_n, gas_n]
        return entrada_t, target
