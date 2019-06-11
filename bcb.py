def bcb(codigo, nome = "Valor", media_movel=1):
  """
  codigo (int, default = None): codigo da série no site https://dadosabertos.bcb.gov.br/ 
  nome (str, default = "Valor"): Nome a ser dado a série
  media_movel (int, default = 1): Número de perídos móveis
    - 1: para série original
    - 4: trimestre móvel
    - 12: mês móvel
  
  ===================
  Exemplo
  
  bcb(11427, "Variação Mensal")
  """
  url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.'+ str(codigo) +'/dados?formato=csv'

  df = pd.read_csv(
    url, 
    sep = ';', 
    index_col = 'data', 
    parse_dates=True, 
    decimal= ',', 
    date_parser = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')
  )
  df.index.name = ''
  df.columns = [nome]
  return df
