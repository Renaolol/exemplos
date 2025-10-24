# Consulta de Classificação Tributária (SVRS)

Este repositório contém um script Python (`Api_conformidade.py`) que consulta a API pública de conformidade fiscal da Secretaria da Fazenda do Rio Grande do Sul (SVRS) para recuperar informações de classificação tributária.

## Pré-requisitos
- Python 3.10 ou superior.
- Certificado digital no formato `.pfx` com acesso ao serviço da SVRS.
- Pacotes Python: `requests`, `requests-pkcs12`, `python-dotenv`.

Instale as dependências com:

```powershell
python -m pip install requests requests-pkcs12 python-dotenv
```

## Configuração
1. **Certificado**: atualize a variável `caminho_cert` em `Api_conformidade.py` com o caminho completo do seu certificado `.pfx`.
2. **Senha do certificado**: crie um arquivo `.env` na raiz do projeto e adicione:
   ```
   SENHA_CERTIFICADO=suasenha
   ```
3. **Variável de consulta**: ajuste o valor do parâmetro `cst` em `params` conforme o código de situação tributária que deseja consultar.

## Uso
Execute o script com:

```powershell
python Api_conformidade.py
```

O script:
- carrega a senha do certificado a partir do `.env`;
- monta uma sessão autenticada com o certificado digital;
- acessa o endpoint `https://cff.svrs.rs.gov.br/api/v1/consultas/classTrib` enviando o parâmetro `cst`;
- imprime o primeiro item retornado pela API.

## Tratamento do retorno
- As respostas são retornadas em JSON pelo serviço da SVRS. O script atual exibe apenas o primeiro registro (`response.json()[0]`).
- Em caso de falha na autenticação ou consulta, a API retornará códigos HTTP de erro. Adicione verificações extras conforme necessário (`response.status_code`, `response.raise_for_status()` etc.).

## Próximos passos sugeridos
- Parametrizar o caminho do certificado e o `cst` via variáveis de ambiente ou argumentos de linha de comando.
- Adicionar validações e tratamento de exceções para respostas inesperadas.
- Persistir os resultados em arquivos CSV/JSON ou em um banco de dados conforme a necessidade do projeto.
