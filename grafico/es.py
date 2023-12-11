import numpy as np
import matplotlib.pyplot as plt

#recebe a função


def leitor_funcao() -> str:
    """
    Apresenta um menu contendo as funções afim, quadrática, logarítmica e exponencial.

    Retorna a escolha do usuário como uma string.
    """
    # Implementação para apresentar o menu de funções
    print("Escolha a função a ser plotada:")
    print("1. Função afim")
    print("2. Função quadrática")
    print("3. Função logarítmica")
    print("4. Função exponencial")
    
    escolha = input("Digite o número correspondente à função: ")
    return escolha

#recebe coeficientes

def leitor_coeficiente(nome_funcao) -> list:
    """
    Lê os coeficientes para função afim ou quadrática, caso escolhida pelo usuário.

    Parâmetros:
    - nome_funcao: string representando o tipo da função escolhida.

    Retorna uma lista de coeficientes.
    """
    coeficientes = []

    if nome_funcao == "1":
        coeficientes.append(float(input("Digite o coeficiente a: ")))
        coeficientes.append(float(input("Digite o coeficiente b: ")))
    elif nome_funcao == "2":
        coeficientes.append(float(input("Digite o coeficiente a: ")))
        coeficientes.append(float(input("Digite o coeficiente b: ")))
        coeficientes.append(float(input("Digite o coeficiente c: ")))

    return coeficientes


#imprime o gráfico
def impressora(pontos, modulo_plotagem=plt):
    """
    Imprime na tela o gráfico usando os pontos da função escolhida.

    Parâmetros:
    - pontos: lista de tuplas (x, y) representando pontos do gráfico.
    - modulo_plotagem: módulo de plotagem (por padrão, Matplotlib).

    Esta função utiliza o método plot do módulo de plotagem para exibir o gráfico.
    """
    x, y = zip(*pontos)
    modulo_plotagem.plot(x, y)
    modulo_plotagem.title("Gráfico da Função")
    modulo_plotagem.xlabel("x")
    modulo_plotagem.ylabel("y")
    modulo_plotagem.show()