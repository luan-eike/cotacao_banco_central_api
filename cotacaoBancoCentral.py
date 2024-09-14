import requests
import datetime


dateTimeNow = datetime.datetime.today()
EndDate     = dateTimeNow.strftime('%m-%d-%Y')
StartDate   = (dateTimeNow - datetime.timedelta(days=30)).strftime('%m-%d-%Y')
TipoBoletim = 'Fechamento'
MoedaMMM    = 'USD'
url         = f'''https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='{MoedaMMM}'&@dataInicial='{StartDate}'&@dataFinalCotacao='{EndDate}'&$top=100&$filter=tipoBoletim%20eq%20'{TipoBoletim}'&$format=json'''

cotacao = requests.get(url).json()

for i in cotacao['value']:
    print(i)