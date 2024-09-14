# cotacao_banco_central_api
Esse script traz a cotação do fechamento das moedas de acordo com o banco central do Brasil.

dateTimeNow - data atual
EndDate     - data atual formatada
StartDate   - data de inicio da pesquisa de moedas (está programado para pegar 30 dias anteriores a data atual)
TipoBoletim - existem alguns tipos de boletim que o Banco central divulga, mas está programado para mostrar apenas o boletim de "Fechamento"
MoedaMMM    - código da moeda que será pesquisada, esse código tem 3 letras. Ex.: USD, EUR, BRL
