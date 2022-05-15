import pandas as pd
import openpyxl
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
account_sid = 'ACb9ce54b7c6dd4a892f93a47634a7470c'
auth_token  = '85948ad536bfec0ecece00db52e31c72'
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro','março','abril','maio','junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel (f'{mes}.xlsx')
    if (tabela_vendas['Vendas']>55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']>55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']>55000,'Vendas']. values[0]
        print(f'no mes {mes} o vendedor: {vendedor}, bateu a meta com  o seguinte numero de vendas: {vendas}.')
        message=client.messages.create(
            from_='+17166870458',
            to='+5582999298820',
            body=f'no mes {mes} o vendedor: {vendedor}, bateu a meta com  o seguinte numero de vendas: {vendas}.')
        print(message.sid)




