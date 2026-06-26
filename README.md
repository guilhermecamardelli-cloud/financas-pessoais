# App de Finanças Pessoais

Este é um aplicativo de terminal desenvolvido em Python para gerenciamento de finanças pessoais. O programa permite registrar receitas e despesas com validação de dados, visualizar extratos detalhados, gerar relatórios de saldo por categoria e exportar esses dados para um arquivo de texto.

## Funcionalidades

1 - REGISTRAR: Permite cadastrar uma nova movimentação, solicitando o tipo (receita ou despesa), o valor, a categoria e uma descrição curta. Os dados são validados para evitar erros.

2 - VER EXTRATO: Exibe na tela uma lista de todos os lançamentos realizados até o momento, mostrando a data, tipo, categoria e o valor formatado.

3 - RELATÓRIO: Mostra um resumo financeiro com o total de receitas, total de despesas, o saldo total atual e um agrupamento dos gastos/ganhos por categoria.

4 - EXPORTAR: Gera um arquivo texto chamado relatorio.txt com o conteúdo detalhado do relatório financeiro atual.

5 - SAIR: Encerra o programa com segurança (todas as operações são salvas automaticamente a cada registro).


## Funções implementadas

carregar() - Lê o arquivo lancamentos.json no início do programa. Se o arquivo não existir, inicializa uma lista vazia.

salvar() - Grava a lista atualizada de lançamentos no arquivo lancamentos.json sempre que um novo registro é feito.

registrar_lancamento() - Orquestra a entrada de dados do novo registro e valida as entradas antes de salvar.

exibir_extrato() - Percorre a lista de lançamentos e imprime cada um deles de forma organizada e formatada na tela.

calcular_saldo() - Processa as operações matemáticas para somar receitas, despesas e consolidar o saldo líquido.

gerar_relatorio() - Exibe o breakdown (detalhamento) dos valores acumulados por cada categoria cadastrada.

exportar_relatorio() - Abre e grava as informações consolidadas do relatório dentro do arquivo relatorio.txt.

## Como rodar

Para executar o aplicativo, certifique-se de ter o Python 3 instalado e rode o seguinte comando no terminal:

python financas.py
