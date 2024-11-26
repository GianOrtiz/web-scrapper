# Agregador de produtos

Agregador de produtos em diferentes sites como validação de conhecimentos sobre web scrap e web crawling. O agregador funciona com base em uma quantidade de seeds e a partir dele explora outros links nas páginas.

Atualmente, funciona apenas com alguns sites selecionados: MercadoLivre, MagazineLuiza e Zoom. Podemos adaptá-lo para outro site adicionando uma nova estratégia específica para esse site. Para relacionar dados entre os sites utilizamos uma função de distância de Levenshtein para agrupar produtos com títulos relacionados.

Construímos um BI que permite a análise dos dados com base nos dados coletados [aqui](https://lookerstudio.google.com/reporting/c67437c8-5a93-4a74-9f14-18d8cb389470).

## Requisitos

* Python 3+

## Execução

Para executar, basta executar no Linux o comando para configurar o ambiente isolado de Python com:

```
source ./venv/bin/activate
```

Instalar os pacotes obrigatórios:

```
pip3 install -r requirements.txt
```

Depois disso basta executar o projeto com:

```
python3 main.py
```

Isto irá gerar um arquivo CSV, `products.csv`, com os dados coletados do dia.
