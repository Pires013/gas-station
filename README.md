Sistema simples de gerenciamento de vendas de combustíveis desenvolvido em Python, com controle de estoque, registro de vendas e geração de relatórios.

Este projeto foi criado com o objetivo de praticar conceitos de programação, organização de código em módulos e manipulação de dados, sendo um bom exemplo de projeto inicial para portfólio.

📌 Funcionalidades

✔ Registrar venda de combustível

✔ Controle de estoque dos combustíveis

✔ Geração de relatório de vendas

✔ Exportação das vendas para arquivo CSV

✔ Interface simples via terminal

🧱 Estrutura do Projeto
---
gas-station/

├── main.py      # Arquivo principal com o menu do sistema

├── data.py      # Dados iniciais (combustíveis e lista de vendas)

├── services.py  # Lógica de registro de vendas

├── reports.py   # Geração de relatórios e exportação CSV


⛽ Combustíveis disponíveis

---
O sistema trabalha com os seguintes tipos de combustível:

G → Gasolina

GC → Gasolina Grid

GP → Gasolina Podium

D → Diesel

Cada combustível possui:

Nome

Preço por litro

Estoque disponível

▶ Como executar o projeto
1️⃣ Clonar o repositório

git clone https://github.com/seu-usuario/gas-station.git

2️⃣ Entrar na pasta do projeto

cd gas-station

3️⃣ Executar o programa

python main.py

📊 Menu do Sistema

Ao executar o programa, o usuário verá o seguinte menu:

=== POSTO DE GASOLINA ===

1 - Vender combustível

2 - Ver estoque

3 - Relatório de vendas

4 - Exportar vendas (CSV)

0 - Sair

📁 Exportação de Dados

A opção Exportar vendas (CSV) gera um arquivo com todas as vendas registradas, permitindo:

análise de dados

importação para Excel

geração de relatórios externos

🧠 Conceitos aplicados

Este projeto utiliza diversos conceitos importantes de programação:

Programação modular

Separação de responsabilidades

Manipulação de listas e objetos

Tratamento de erros (try/except)

Entrada de dados do usuário

Escrita de arquivos CSV

Organização de projeto Python

🎯 Objetivo do projeto

Este projeto foi desenvolvido como exercício de aprendizado e prática em Python, com foco em:

lógica de programação

organização de código

criação de projetos para portfólio

👨‍💻 Autor

Matheus Pires

🔗 GitHub
https://github.com/Pires013

🔗 LinkedIn
https://www.linkedin.com/in/matheus-pires-3b17b3240
