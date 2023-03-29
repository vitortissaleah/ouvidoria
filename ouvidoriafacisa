from metodos import *

conexao = abrirBancoDados('localhost','root', 'root', 'bdouvidoria')

opcao = 6

while opcao != 5:
    opcao = menu()

    if opcao == 1:
      listaReclamacoes(conexao)

    elif opcao == 2:
        novaReclamacao(conexao)
        listaReclamacoes(conexao)


    elif opcao == 3:
        listaReclamacoes(conexao)
        pesquisarReclamacaoPeloCodigo(conexao)

    elif opcao == 4:
        listaReclamacoes(conexao)
        removerPeloCodigo(conexao)


    elif opcao == 5:
        break


print('Obrigado, volte sempre!!')
