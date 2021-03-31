# python-nfce-get

Biblioteca em python que recupera as informações de uma nota fiscal consumidor eletronica (NFCE) e converte em um JSON para processamento da forma que você precisar.

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=alert_status)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=bugs)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=code_smells)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=coverage)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)

[![Known Vulnerabilities](https://snyk.io/test/github/brunopenso/python-nfce-get/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/brunopenso/python-nfce-get?targetFile=requirements.txt)

## Uso

### Paraná

A biblioteca faz o parse de duas formas:

#### Link QR Code
Ao receber a nota fiscal do estabelecimento você irá ver no final dela um QRCode. Faça o scan desse qr code com seu celular e use este link para processar (veja instruções no final dessa página)

Modelo de url: http://www.fazenda.pr.gov.br/nfce/qrcode?p=41210276489406104970651080002472271201438086|2|1|1|85901C8C5A58990BA3026CB2DDDF75CF1580BC93

#### Html do Site Nota Parana
- Acesse o site `http://www.notaparana.pr.gov.br`
- Faça seu login, encontre a nota e clique para visualizar
- A imagem será algo como [imagem](./assets/notaparana.png)
- Clique em exibir o código fonte e depois salve o html em um arquivo em seu computador

#### Site Receita Estadual
- Acesse o site `http://www.sped.fazenda.pr.gov.br/modules/conteudo/nfce.php?consulta=completa`
- Informe o numero da nota e digite o código de verificação
- Encontre a Aba *Informações Adicionais*  
- Depois procure o campo **QR-Code**.
- Copie o link do QR Code e use a opção de QR Code

#### Limitações
- Para consulta de notas no site da receita estadual através de API/WebServices é necessário um certificado o que acaba não sendo viável para essa biblioteca
- O site da nota paraná precisa de usuário e senha para funcionar, então não entramos nesse nível de detalhe no desenvolvimento.

## Uso
### Uso - Link QR Code

*Observação:* O link abaixo não é válido

```python
from nfceget import app

json = app.json_from_qrcode_link('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41200976430438005123450150002022071015187452|2|1|1|E9C67EF7E8B75CD401B3F6D3B1FD716ED22B3890')

print(json)
```

### Uso - Arquivo HTML

1. Acesse o site do Nota Paraná e visualize a sua nota
2. Botão direito na página e view html
3. Salvar o html
4. Executar o código abaixo

```python
from nfceget import app

json = app.json_from_file( './file.html' )

print(json)
```

### Uso - Resultado

O resultado será algo como:

```json
{'local': {'name': 'IRMAOS MUFFATO E CIA LTDA', 'cnpj': '76.430.438/0053-00', 'address': 'Av Victor Ferreira do Amaral,1088,,Taruma,Curitiba,PR'}, 'itens': [{'name': 'CEBOLA KG', 'code': '3355', 'quantity': '0,79', 'unit': 'Kg', 'unitaryValue': '2,98', 'totalValue': '2,35'}, .... ], 'totals': {'quantityItens': '26', 'total': '281,03', 'discounts': '5,09', 'valueToPay': '275,94', 'taxes': '62,65'}, 'nfce': {'numero': '204507', 'serie': '15', 'date': '01/09/2020 15:22:18', 'protocolo': '141201044877471', 'version': '4.00', 'chave': '41200976430438005123450150002022071015187452'}}
```

## Local

### Como instalar

```bash
make ci-dependencies
```

### Como testar

```bash
make test-coverage
make test
```
