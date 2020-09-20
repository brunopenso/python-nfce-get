# python_nfce_get

Biblioteca em python que recupera as informações de uma nota fiscal consumidor eletronica

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=alert_status)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=bugs)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=code_smells)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=coverage)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=9b6a84d1-544b-4413-8c39-bb02a0de21ea&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=9b6a84d1-544b-4413-8c39-bb02a0de21ea)



## Como recuperar

Uma das opções que achei é:

[Sped Paraná](http://www.sped.fazenda.pr.gov.br/modules/conteudo/conteudo.php?conteudo=97)

Porém todos os WS dão problema de certificado

### Urls Paraná

```python
NFCE_MODELO: {
        AMBIENTE_PRODUCAO: {
            "servidor": "nfce.sefa.pr.gov.br",
            WS_NFE_RECEPCAO_EVENTO: "nfce/NFeRecepcaoEvento4?wsdl",
            WS_NFE_AUTORIZACAO: "nfce/NFeAutorizacao4?wsdl",
            WS_NFE_RET_AUTORIZACAO: "nfce/NFeRetAutorizacao4?wsdl",
            WS_NFE_CADASTRO: "nfce/CadConsultaCadastro4?wsdl",
            WS_NFE_INUTILIZACAO: "nfce/NFeInutilizacao4?wsdl",
            WS_NFE_CONSULTA: "nfce/NFeConsultaProtocolo4?wsdl",
            WS_NFE_SITUACAO: "nfce/NFeStatusServico4?wsdl",
            WS_NFCE_QR_CODE: "www.fazenda.pr.gov.br/nfce/qrcode?",
        },
        AMBIENTE_HOMOLOGACAO: {
            "servidor": "homologacao.nfce.sefa.pr.gov.br",
            WS_NFE_RECEPCAO_EVENTO: "nfce/NFeRecepcaoEvento4?wsdl",
            WS_NFE_AUTORIZACAO: "nfce/NFeAutorizacao4?wsdl",
            WS_NFE_RET_AUTORIZACAO: "nfce/NFeRetAutorizacao4?wsdl",
            WS_NFE_CADASTRO: "nfce/CadConsultaCadastro4?wsdl",
            WS_NFE_INUTILIZACAO: "nfce/NFeInutilizacao4?wsdl",
            WS_NFE_CONSULTA: "nfce/NFeConsultaProtocolo4?wsdl",
            WS_NFE_SITUACAO: "nfce/NFeStatusServico4?wsdl",
            WS_NFCE_QR_CODE: "www.fazenda.pr.gov.br/nfce/qrcode?",
        },
    },
```
