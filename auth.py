import base64
login ='meu-login'
senha = 'minha-senha-super-secreta'

auth_string = f'{login}:{senha}'.encode()
auth_string = base64.b64encode(auth_string)
auth_string = auth_string.decode()
print (auth_string)

