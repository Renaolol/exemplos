import requests
import os
import base64
from requests_pkcs12 import Pkcs12Adapter
from pprint import pprint
from dotenv import load_dotenv
import json
#Carrega o .env
load_dotenv()
session = requests.Session()
caminho_cert = r"C:\Users\gcont\OneDrive\Desktop\GCONT.pfx" 
senha = os.getenv("SENHA_CERTIFICADO")
session.mount("https://",Pkcs12Adapter(pkcs12_filename=caminho_cert,pkcs12_password=senha))
url = "https://cff.svrs.rs.gov.br/api/v1/consultas/anexos"
#Parametros aceitos cst ou NomeCst
response = session.get(url)
#Utilizado pprint para uma visualização encadeada
with open("CclassTrib", "w", encoding="utf-8") as arquivo:
    json.dump(response.json(),arquivo,indent=4,ensure_ascii=False)
