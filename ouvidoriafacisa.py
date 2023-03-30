from metodosouvidoria import *

conexao = abrirBancoDados('localhost','root', '12345', 'bdouvidoria')

opcao = 6

while opcao != 5:
    opcao = menu()

    if opcao == 1:
      listaTodasReclamacoes(conexao)
    elif opcao == 2:
        novaReclamacao(conexao)
        listaTodasReclamacoes(conexao)
    elif opcao == 3:
        listaTodasReclamacoes(conexao)
        pesquisarReclamacaoPeloCodigo(conexao)

    elif opcao == 4:
        listaTodasReclamacoes(conexao)
        removerPeloCodigo(conexao)


    elif opcao == 5:
        break


print('Obrigado, volte sempre!!')
