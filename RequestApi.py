import requests
from pprint import pprint
import streamlit as st
nome = input("Insira o nome a ser consultado, selecione mais com o separador |")
url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

response=requests.get(url)
try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Não foi possível concluir: {e}")    
else:
    pprint(response.json())
