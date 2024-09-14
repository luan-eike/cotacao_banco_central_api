# cotacao_banco_central_api
Esse script traz a cotação do fechamento das moedas de acordo com o banco central do Brasil.

dateTimeNow - data atual  
EndDate     - data atual formatada  
StartDate   - data de inicio da pesquisa de moedas (está programado para pegar 30 dias anteriores a data atual)  
TipoBoletim - existem alguns tipos de boletim que o Banco central divulga, mas está programado para mostrar apenas o boletim de "Fechamento"  
MoedaMMM    - código da moeda que será pesquisada, esse código tem 3 letras. Ex.: USD, EUR, BRL  

Fonte:
- [Tabela de cotação](https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes)
- [API utilizada](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos/CotacaoMoedaPeriodo#eyJmb3JtdWxhcmlvIjp7IiRmb3JtYXQiOiJqc29uIiwiJHRvcCI6MTAwLCJtb2VkYSI6IlVTRCIsImRhdGFJbmljaWFsIjoiMDgtMTUtMjAyNCIsImRhdGFGaW5hbENvdGFjYW8iOiIwOS0xNC0yMDI0IiwiJGZpbHRlciI6IgQ1BCBlcSAnRmVjaGFtZW50bycifSwicGVzcXVpc2FkbyI6dHJ1ZSwiYWN0aXZlVGFiIjoiZGFkb3MiLCJncmlkU3RhdGUiOnsDMAM6W3sDQgMiBDAEIiwDQQN9LHsDQgMiBDEEIiwDQQN9LHsDQgMiBDIEIiwDQQN9LHsDQgMiBDMEIiwDQQN9LHsDQgMiBDQEIiwDQQN9LHsDQgMiBDUEIiwDQQN9XSwDMQM6e30sAzIDOltdLAMzAzp7fSwDNAM6e30sAzUDOnt9fSwicGl2b3RPcHRpb25zIjp7A2EDOnt9LANiAzpbXSwDYwM6NTAwLANkAzpbXSwDZQM6W10sA2YDOltdLANnAzoia2V5X2FfdG9feiIsA2gDOiJrZXlfYV90b196IiwDaQM6e30sA2oDOnt9LANrAzo4NSwDbAM6ZmFsc2UsA20DOnt9LANuAzp7fSwDbwM6IkNvbnRhZ2VtIiwDcAM6IlRhYmxlIn19)
