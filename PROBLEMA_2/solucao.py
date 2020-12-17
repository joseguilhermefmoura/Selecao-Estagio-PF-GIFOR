import csv
import operator


def get_registers(csv_file):
    """
    Essa função lê um arquivo csv e retorna uma lista de registros (dicionários)
    O delimitador deve ser ';' e deve seguir o cabeçalho <Id;nome;telefone;idade>
    """

    # Inicializa uma lista vazia para guardar os registros (dicionários)
    registers_list = []

    # Para cada linha do arquivo, faça:
    for line in csv_file.readlines():
        # Armazena os valores lidos
        id_, name_, fone_, age_ = line.strip('\n').split(';')
        # Transforma esses valores em dicionários e armazena na lista
        registers_list.append(
            {'id': id_, 'name': name_, 'fone': fone_, 'age': age_})

    # Retira o cabeçalho presente no arquivo ("Id;nome;telefone;idade")
    del registers_list[0]

    # Ordena a lista de dicionários pela chave 'name'
    registers_list.sort(key=operator.itemgetter('name'))

    # Retorna a lista
    return registers_list


def __main__():
    # Abre o arquivo
    with open('entrada.csv', 'r') as csv_file:
        # Chama a função e imprime cada dicionário dentro do retorno
        for dictionary in get_registers(csv_file):
            print(dictionary)


__main__()
