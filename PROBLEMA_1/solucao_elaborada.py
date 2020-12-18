def find_values(dictionary_list):
    """
    Essa função recebe uma lista de dicionarios e retorna a lista dos valores
    associados à chave 'nome' (caso exista), sem que haja repetição.
    """

    # Solução em uma linha. Explicação:

    """
    Um set não pode possuir duplicatas, então transformamos o nosso return em um set,
    que está englobando um compressor de lista ("[]", responsável por transformar em lista),
    que engloba um laço de uma linha, que itera cada dicionario na lista de dicionarios e retorna
    o valor associado a chave 'nome' - caso este exista.
    """
    return set([dictionary['nome'] for dictionary in dictionary_list if 'nome' in dictionary])

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
