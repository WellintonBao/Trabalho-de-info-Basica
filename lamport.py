def resumo():
    mensagem = "Leslie Lamport é um cientista da computação estadunidense. Formou-se em matemática pelo Massachusetts Institute of Technology em 1960, com mestrado e doutorado em matemática pela Universidade Brandeis."
    return mensagem


def doutorado():
    mensagem = "O tema de sua tese de doutorado foi singularidades em equações diferenciais parciais analíticas..."
    return mensagem


def contribuicoes():
    mensagem = "Suas pesquisas contribuíram com a fundação da teoria de sistemas distribuídos. Além de introduzir novos conceitos na ciência computacional, tais como relógios lógicos (logical clocks) e a relação antes-depois, bem como as falhas Bizantinas."
    return mensagem


def artigos():
    mensagem = "Time, Clocks, and the Ordering of Events in a Distributed System","\nDistributed snapshots: determining global states of distributed systems","\nThe Byzantine Generals Problem."
    return mensagem


def citacoes():
    mensagem = "'A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable.'", "\n'I think in other things that I've done, I can look back and see: This idea developed from something else.'" , "\n'Thinking doesn't guarantee that we won't make mistakes. But not thinking guarantees that we will.'"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Leslie Lamport.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
