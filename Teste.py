############################################################
print('*'*10, 'SALARIO/ENTRADAS', '*'*10)


salario = 4300.00
print('salario =', round(salario,2))

adicional_insalubridade = 282.4 # Grau médio
print('insalubridade =', adicional_insalubridade)
#fonte: https://genyo.com.br/adicional-de-insalubridade/

arredond_mes = 0.87

salario_total_0 = salario + adicional_insalubridade
salario_total = salario + adicional_insalubridade + arredond_mes
print('salario bruto =', round(salario_total,2), '\n')


############################################################
print('*'*10, 'DESCONTOS/SAIDAS', '*'*10,'\n')


print('*'*5, 'INSS', '*'*5)
# primeira parte -> até 1.412,00
p1 = 1412*(7.5/100)
# segunda parte -> 1.412,00 - 2.666,68
p2 = (2666.68 - 1412.00)*(9/100)
# terceira parte -> 2.666,68 - 4.000,03
p3 = (4000.03 - 2666.68)*(12/100)
# quarta parte -> 4.000,03 - 7.786,02
p4 = (salario_total_0 - 4000.03)*(14/100)
print('faixa de desconto INSS: (', round(p1,2),';', round(p2,2),';', round(p3,2),';', round(p4,2), ')')

INSS = round(p1+p2+p3+p4, 2)
print('INSS =', INSS,'\n')
# fonte: https://www.bloomberglinea.com.br/2024/02/20/tabela-de-desconto-do-inss-2024-valores-e-como-calcula-los/
# fonte: https://www.gov.br/inss/pt-br/assuntos/confira-as-aliquotas-de-contribuicao-ao-inss-com-o-aumento-do-salario-minimo


print('*'*5, 'OUTROS DESCONTOS', '*'*5)
qdt_dependente = 1
valor_por_dependente = 189.59 * qdt_dependente
print('dependentes =',round(valor_por_dependente, 2),'\n')


print('*'*5, 'I.R.R.F - imposto de renda', '*'*5)
IRPF = salario_total - INSS - valor_por_dependente
print('base calculo =', round(IRPF,2),'\n')
percent_IRRF = 22.5/100
print('porcentagem I.R.R.F =', str(round(percent_IRRF*100,2))+'%')
deducao_IRRF = 662.77
print('Dedução =', round(deducao_IRRF,2))

IRRF = (IRPF * percent_IRRF) - deducao_IRRF
print('I.R.R.F =', round(IRRF,2),'\n')
# fonte: " Imposto de Renda: Como calcular na folha de pagamento" [link = https://youtu.be/NfRrK5WlYNo?si=9NgyBrlDiiSvomdl]
# fonte 2: https://www.totvs.com/blog/fiscal-clientes/irrf-nova-tabela-progressiva-2024/

print('*'*5, 'VALE TRANSPORTE', '*'*5)
percent_vale_transporte = 6/100
vale_transporte = salario*percent_vale_transporte
print('Vale Transporte =', round(vale_transporte,2),'\n')


############################################################
print('*'*10, 'TOTAL DESCONTOS', '*'*10)
total_descontos = INSS + IRRF + vale_transporte
print('total descontos =', round(total_descontos,2), '\n')


############################################################
print('*'*10, 'SALARIO LIQUIDO', '*'*10)
salario_liquido = salario_total - total_descontos
print('salario liquido =', round(salario_liquido,2))