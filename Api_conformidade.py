import requests
import os
import base64
from requests_pkcs12 import Pkcs12Adapter
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()
session = requests.Session()
caminho_cert = r"C:\Users\gcont\OneDrive\Desktop\GCONT.pfx" 
senha = os.getenv("SENHA_CERTIFICADO")
session.mount("https://",Pkcs12Adapter(pkcs12_filename=caminho_cert,pkcs12_password=senha))
url = "https://cff.svrs.rs.gov.br/api/v1/consultas/classTrib"
params = {'cst': "000"}
response = session.get(url,params = params)
pprint(response.json()[0])