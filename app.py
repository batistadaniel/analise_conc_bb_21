import pandas as pd

def resultado_final_ti_bb_21(dados):

    colunas = [coluna.replace("\n", " ").split(";") for coluna in dados.split('/')]

    # linhas = [linha.strip() for linha in dados.split('/') if linha.strip()]
    # colunas = [linha.split(";") for linha in linhas]

    df = pd.DataFrame(colunas, columns=[
    'Nome', 'Inscricao', 'Pontuacao', 'Classificacao Micro-Macrorregiao',  'PCD', 'PPP'])

    df = df.sort_values(by='Pontuacao', ascending=False)

    csv = df.set_index('Nome')
    display(csv)

    #return df


resultado_final_ti_bb_21()
