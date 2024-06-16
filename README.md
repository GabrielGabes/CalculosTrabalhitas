## CalculosTrabalhitas

**CalculosTrabalhitas** é um projeto que decidi desenvolver para recalcular meus descontos na folha de pagamento e resolver a seguinte questão: Em que ponto vale mais a pena deixar de trabalhar CLT e trabalhar como PJ?

### 0. Calculando Faixas de Salários vs Descontos -> `0 - Calculando Faixas.ipynb`
Neste notebook, criei funções para cálculos dos:
- Descontos fixos: INSS, IRRF (Imposto de Renda)
- Descontos variáveis/optativos: Vale transporte, dependentes

Com base em cada faixa de salário, criei um dataframe que permite ter um panorama de como cada desconto evolui conforme a faixa salarial. Essa análise é feita no tópico/arquivo abaixo.

### 1. Análise dos Dados -> `1 - Analise Grafica.ipynb`
Neste notebook em R, realizo uma análise gráfica cruzando as variáveis entre si, trazendo insights sobre as relações delas.

### Benefícios

- **Clareza Financeira:** Compreensão detalhada dos descontos em folha de pagamento e sua evolução conforme o aumento salarial.
- **Tomada de Decisão:** Identificação do ponto em que pode ser mais vantajoso financeiramente trabalhar como PJ em vez de CLT.

### Conclusão

O projeto CalculosTrabalhitas fornece uma ferramenta valiosa para entender os impactos financeiros dos descontos na folha de pagamento e auxilia na decisão de migração entre regimes de trabalho. A análise detalhada e visual dos dados oferece uma visão clara e prática para trabalhadores que buscam otimizar seus ganhos.
