from operacoesbd import *



def menu():
    print()
    print("1) Listar todas as reclamações: ")
    print("2) Adicionar nova reclamação: ")
    print("3) Pesquisar pelo código da reclamção: ")
    print("4) Remover pelo código da reclamação: ")
    print("5) Sair: ")
    opcao = int(input('Digite sua opção: '))
    return opcao

def listaReclamacoes(conexao):

    print()
    print('OUVIDORIA FACISA | RECLAMAÇÕES:')
    print()
    consultaListagemReclamacoes = 'select * from ouvidoriafacisa'
    listaReclamacoes = listarBancoDados(conexao, consultaListagemReclamacoes)

    if len(listaReclamacoes) == 0:
        print('Não existem reclamações a serem exibido.')
    else:
        for i in listaReclamacoes:
            print('-CÓDIGO DA RECLAMAÇÃO:', i[0])
            print('-RECLAMAÇÃO:', i[1])
            print()
def novaReclamacao(conexao):
        novaReclamacao = input('Digite uma nova Reclamação: ')

        consultaNovaReclamacao = 'insert into ouvidoriafacisa(reclamacao)values(%s)'
        dados = (novaReclamacao,)
        insertNoBancoDados(conexao, consultaNovaReclamacao, dados)

def pesquisarReclamacaoPeloCodigo(conexao):

    print("|PESQUISE PELO CODIGO| ")
    codigo = input('digite o codigo:')
    print()
    consultaReclamacaoCodigo = 'select * from ouvidoriafacisa where codigo_Reclamacao=' + codigo
    listaReclamacoes = listarBancoDados(conexao, consultaReclamacaoCodigo)

    for i in listaReclamacoes:
        if len(listaReclamacoes) == 0:
            print('Não existem reclamações a serem exibido.')
        else:
            for i in listaReclamacoes:
                print('-CÓDIGO DA RECLAMAÇÃO:', i[0])
                print('-RECLAMAÇÃO:', i[1])
                print()

def removerPeloCodigo(conexao):
    codigo =  input('Digite o codigo da reclamação a ser removido: ')
    consultaRemoverReclamacaoCodigo = 'delete from ouvidoriafacisa where codigo_Reclamacao = %s '
    dados = (codigo,)

    excluirBancoDados(conexao, consultaRemoverReclamacaoCodigo, dados)
    print('-Removido com sucesso')
