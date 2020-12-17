def find_values(dictionary_list):
    """
    Essa função recebe uma lista de dicionarios e retorna a lista dos valores
    associados à chave 'nome' (caso exista), sem que haja repetição.
    """

    values_list = []  # Inicializa a lista de resultados (vazia)

    for dictionary in dictionary_list:  # Laço que acessa cada dicionário na lista de dicionários
        if "nome" in dictionary:  # Caso exista a chave 'nome', prossiga
            if dictionary["nome"] not in values_list:
                # Caso o valor da chave 'nome' ainda não exista na lista de
                # resultados:
                # Insira na lista de resultados
                values_list.append(dictionary["nome"])
            else:
                # Caso já tenha sido inserido, imprima no console:
                print("Ops! O valor '{}' é uma duplicata!"
                      .format(dictionary["nome"]))
                print("Portanto, não foi armazenado.")
        else:
            # Caso não exista a chave 'nome', imprima no console:
            print("Não foi encontrado o índice 'nome' para esse dicionário.")

    return values_list


def __main__():
    # Declara lista de dicionários
    dictionary_list = [
        {"nome": "José"},
        {"nome": "Pedro"},
        {"nome": "Robson"},
        {"nome": "Mateus"},
        {"nome": "Iago"},
        {"nome": "José"}
    ]

    # Chama a função e imprime seu valor de retorno (lista) como string.
    print("O resultado final é: " + str(find_values(dictionary_list)))


__main__()
