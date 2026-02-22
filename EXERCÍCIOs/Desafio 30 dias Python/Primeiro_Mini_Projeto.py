
# Mini-Projeto 1 – Resumo Inteligente de Faturamento
# 🎯 Objetivo

# Criar um sistema simples em Python que:

# Calcule o faturamento total de cada loja

# Calcule o faturamento geral

# Calcule a média de faturamento por loja

# Identifique qual loja teve o maior faturamento

# Retorne tudo organizado

# Enunciado Completo

# Você deverá criar uma função que:

# Parte 1 – Processamento (dentro da função)

# A função deve:

# Receber o dicionário como parâmetro

# Criar um novo dicionário com o total de cada loja

# Calcular:

# Total geral

# Média por loja

# Identificar:

# Loja com maior faturamento

# Valor desse faturamento

# Retornar:

# Dicionário com totais

# Total geral

# Média

# Nome da loja com maior faturamento

# Valor da maior loja

# ⚠️ A função não deve imprimir nada.

# Parte 2 – Relatório (fora da função)

# No programa principal você deve:

# Chamar a função

# Receber os retornos

# Imprimir um relatório organizado como este modelo:

faturamento_lojas = {
    'Matriz': [12500, 14800, 13200, 9900],
    'Filial Sul': [8200, 7900, 9100, 8700],
    'Filial Norte': [7600, 8800, 9400],
    'Filial Nordeste': [6500, 7200, 6900, 7100]

}

def verificando_faturamento_lojas(dicionario):
    faturamento_geral = 0
    faturamento_total_loja = {}
    media_faturamento_loja = {}

    primeira_loja = True

    relatorio_geral = {}

    for loja, vendas in dicionario.items():
        total_vendas = sum(vendas)
        faturamento_geral += total_vendas
        faturamento_total_loja[loja] = total_vendas
        media_faturamento_loja[loja] = faturamento_total_loja[loja] / len(vendas)

        if primeira_loja:
            nome_loja_com_mais_vendas = loja
            total_vendas_loja_com_mais_vendas = total_vendas

            nome_loja_com_menos_vendas = loja
            total_vendas_loja_com_menos_vendas = total_vendas

            primeira_loja = False
        else:   
            if total_vendas > total_vendas_loja_com_mais_vendas:
                nome_loja_com_mais_vendas = loja
                total_vendas_loja_com_mais_vendas = total_vendas

            if total_vendas < total_vendas_loja_com_menos_vendas:
                nome_loja_com_menos_vendas = loja
                total_vendas_loja_com_menos_vendas = total_vendas

    media_geral_vendas = faturamento_geral / len(faturamento_total_loja)

    relatorio_geral['Faturamento Geral de Vendas'] = faturamento_geral
    relatorio_geral['Média Geral de Vendas'] = media_geral_vendas
    relatorio_geral['Nome Loja com MAIS Vendas'] = nome_loja_com_mais_vendas
    relatorio_geral['Total de Vendas da Loja com Mais Vendas'] = total_vendas_loja_com_mais_vendas
    relatorio_geral['Nome Loja com MENOS Vendas'] = nome_loja_com_menos_vendas
    relatorio_geral['Total de Vendas da Loja com MENOS Vendas'] = total_vendas_loja_com_menos_vendas
    relatorio_geral['Faturamento Total por Loja'] = faturamento_total_loja
    relatorio_geral['Média Faturamento por Loja'] = media_faturamento_loja

    return relatorio_geral


relatorio = verificando_faturamento_lojas(faturamento_lojas)

print('=' * 60)
print(f'{'RELATÓRIO FINAL DE VENDAS'.center(60)}')
print('=' * 60)
print(f'Faturamento Geral de Vendas: {relatorio['Faturamento Geral de Vendas']:.2f}')
print(f'Média Geral de Vendas: {relatorio['Média Geral de Vendas']:.2f}')
print(f'Nome Loja com MAIS Vendas: {relatorio['Nome Loja com MAIS Vendas'].upper()}')
print(f'Total de Vendas da Loja com Mais Vendas: {relatorio['Total de Vendas da Loja com Mais Vendas']:.2f}')
print(f'Nome Loja com MENOS Vendas: {relatorio['Nome Loja com MENOS Vendas'].upper()}')
print(f'Total de Vendas da Loja com MENOS Vendas: {relatorio['Total de Vendas da Loja com MENOS Vendas']:.2f}')
print('-' * 60)
print(f'Faturamento Total por Loja:')
for loja, total in relatorio['Faturamento Total por Loja'].items():
    print(f' - {loja.upper()}: {total:.2f}')
print('-' * 60)
print(f'Média Faturamento por Loja:')
for loja, total in relatorio['Média Faturamento por Loja'].items():
    print(f' - {loja.upper()}: {total:.2f}')
print('=' * 60)
