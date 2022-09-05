# selenium-puppeteer-comparison

Experimentos Realizados na comparação entre entre Selenium Python e Puppeteer.JS  

# About

Este trabalho busca comparar, de forma quantitativa, avaliando o consumo de recursos de CPU e memória, duas bibliotecas de código aberto voltadas para a automação web, São elas: Selenium e Puppeteer.Js; e avaliar em que situações possuímos alguma vantagem na escolha de uma determinada biblioteca em favor de outra. Para isto, simulamos rotinas de preenchimento de formulários e extração de dados usando ambas as ferramentas e comparamos os resultados obtidos, que mostraram valores estatisticamente semelhantes no consumo de recursos para a situação de preenchimento de formulários, porém foi observado uma grande diferença para a extração de dados.

Para executar os testes é necessário ter o [Docker](https://docs.docker.com/get-docker/) instalado no ambiente. 

# Puppeteer.Js

# Usage

Para fazer uso do robô precisamos primeiro construir a imagem do contêiner.
<!-- usage -->
```sh-session
$ cd ./puppeteer-robot
$ docker image build -t puppeteer-robot . 
```
Em seguida, podemos executar o contêiner usando o comando: 
<!-- usage -->
```sh-session
$ docker container run puppeteer-robot 
```
Este comando apenas executa o contêiner, para coletar as estatísticas de uso usamos o comando: 
<!-- usage -->
```sh-session
$ docker stats >> logs.txt
```
<!-- usagestop -->

# Selenium
Para fazer uso do robô precisamos primeiro construir a imagem do contêiner.
<!-- usage -->
```sh-session
$ cd ./selenium-robot
$ docker image build -t selenium-robot . 
```
Em seguida, podemos executar o contêiner usando o comando: 
<!-- usage -->
```sh-session
$ docker container run selenium-robot 
```
Este comando apenas executa o contêiner, para coletar as estatísticas de uso usamos o comando: 
<!-- usage -->
```sh-session
$ docker stats >> logs.txt
```
