import pandas as pd


def get_registers(csv_file):
    '''
    Essa função lê um arquivo csv e retorna uma lista de registros ordenados (dicionários)
    O delimitador deve ser ';' e deve seguir o cabeçalho <Id;nome;telefone;idade>
    '''

    # Lê o csv_file como panda dataframe
    df = pd.read_csv(csv_file, delimiter=';')
    # Ordena por nome
    df = df.sort_values('nome')

    # Retorna a lista de dicionários (registros)
    return df.T.to_dict().values()


def __main__():
    # Imprime o resultado após chamar a função:
    for register in get_registers('entrada.csv'):
        print(register)


__main__()
