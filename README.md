# Mineracao de Texto
Projeto de mineração de texto. Classificação de possíveis casos de depressão baseado em Tweets.

# Instalação

## Criar o virtual environment

Na raiz do projeto insira os comandos abaixo para realizar a criação do virtual environment. Esse passo é importante pois evita a instalação de packages globalmente.

Primeiramente, instale o virtualenv caso ainda não tenha instalado anteriormente.

    python3 -m pip install --user virtualenv
Logo após, realize a criação de uma virtualenv chamada **venv** através do comando abaixo:

    python3 -m venv venv
Pode ser necessário fornecer permissão de execução para o arquivo activate utilizado para ativar o virtualenv.

    cd venv/bin/
    chmod +x activate

## Instale as dependências

Todas as dependências do projeto estão informadas no arquivo requirements.txt. Para instalar todas as dependências, faça o passo-a-passo a seguir:

Ative o virtualenv através do comando abaixo:

    cd venv/bin/
    source activate
    cd ../../
    
Finalmente, importe todas as dependências do projeto:
        
    pip install -r requirements.txt