📑 Analisador de Gastos Pessoais (Python CLI)
Olá! Este é um projeto desenvolvido para consolidar meus estudos em Lógica de Programação com Python. O objetivo é oferecer uma ferramenta simples via terminal para que usuários possam registrar e categorizar seus gastos, gerando um extrato formatado e exportável.

🚀 Funcionalidades
Validação de Usuário: Sistema que garante nomes de usuário válidos (não aceita entradas vazias ou apenas numéricas).

Tratamento de Erros: Validação de entradas monetárias para evitar que o programa encerre por erros de digitação (ValueErrors).

Categorização Inteligente: Menu interativo para classificar gastos em Moradia, Alimentação, Lazer ou Outros.

Acúmulo de Dados: Soma recorrente de gastos por categoria durante a execução.

Persistência em TXT: Geração automática de um arquivo extrato_gastos.txt ao encerrar o programa, permitindo que o usuário guarde seu relatório.

🛠️ Tecnologias Utilizadas
Python 3.x

Biblioteca time (para controle de fluxo e UX).

Manipulação de arquivos (with open).

🧠 Desafios e Aprendizados
Durante o desenvolvimento deste projeto, foquei em aplicar conceitos de Clean Code e UX (User Experience) no terminal:

Loops Aninhados: Gerenciar while dentro de while para criar menus que insistem em respostas válidas sem perder o progresso do usuário.

Flags de Controle: Uso de variáveis booleanas para gerenciar o encerramento do programa de forma elegante.

Formatação de Strings: Uso intensivo de f-strings para alinhar colunas e centralizar textos, tornando o extrato legível.

🔧 Como executar
Certifique-se de ter o Python instalado.

Clone o repositório ou baixe o arquivo .py.

Execute o comando:

Bash

python nome_do_arquivo.py
