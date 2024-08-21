# Pipeline ETL

Este projeto se trata de uma pequena demonstração de como fazer a extração de dados a partir de uma página web qualquer, neste caso é utilizado o ETL que que significa Extract, Transform, Load (Extrair, Transformar, Carregar), no qual é um processo fundamental em projetos de integração de dados. Este processo envolve a extração de dados de diversas fontes, a transformação desses dados para um formato adequado, e a carga dos dados transformados em um sistema de armazenamento, como um banco de dados.

## Arquitetura do Projeto

O projeto foi desenvolvido em Python, seguindo uma arquitetura baseada em princípios de Clean Code. Isso garante que o código seja modular, fácil de entender e manter. A separação clara de responsabilidades foi uma prioridade, com cada etapa do processo ETL sendo encapsulada em classes e funções distintas.

## Banco de Dados Utilizado

Para armazenar os dados processados, foi utilizado um banco de dados MySQL. Este banco foi escolhido por sua robustez e ampla adoção no mercado.

## Instalação das dependências do projeto

~~~ bash
pip3 install -r requirements.txt
~~~

## Testes Unitários

Os testes unitários foram implementados usando a biblioteca `pytest`, uma ferramenta poderosa para garantir que cada parte do código funcione como esperado. Para executar os testes, basta rodar o seguinte comando no terminal:

~~~ bash
pytest
~~~

## Execução do projeto
~~~ bash
python3 main.py
~~~

## Materiais utilizados

> Principais bibliotecas
* https://pypi.org/project/mysql-connector-python/
* https://pypi.org/project/beautifulsoup4/
> Estilização do códico e API
* https://peps.python.org/pep-0008/
* https://pylint.readthedocs.io/en/stable/

> Commits personalizados
* https://pre-commit.com/