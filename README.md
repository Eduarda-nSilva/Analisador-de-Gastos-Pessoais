# 📑 Analisador de Gastos Pessoais (Python CLI)

Olá! Este é um projeto desenvolvido para consolidar meus estudos em **Lógica de Programação com Python**. O objetivo é oferecer uma ferramenta simples via terminal para que usuários possam registrar e categorizar seus gastos, gerando um extrato formatado e exportável.

## 🚀 Funcionalidades

- **Validação de Usuário:** Sistema que garante nomes de usuário válidos (não aceita entradas vazias ou apenas numéricas).
- **Tratamento de Erros:** Validação de entradas monetárias para evitar que o programa encerre por erros de digitação (`ValueErrors`).
- **Categorização Inteligente:** Menu interativo para classificar gastos em Moradia, Alimentação, Lazer ou Outros, aceitando tanto o nome quanto o número da opção.
- **Acúmulo de Dados:** Soma recorrente de gastos por categoria durante a execução, mantendo o histórico na sessão.
- **Persistência em TXT:** Geração automática de um arquivo `extrato_gastos.txt` ao encerrar o programa, permitindo que o usuário guarde seu relatório físico.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Biblioteca `time` (para controle de fluxo e experiência do usuário).
- Manipulação de arquivos (`with open`).

## 🧠 Desafios e Aprendizados

Durante o desenvolvimento deste projeto, foquei em aplicar conceitos de **Clean Code** e **UX (User Experience)** no terminal:

1. **Loops Aninhados:** Gerenciar `while` dentro de `while` para criar menus que validam as respostas sem perder o progresso ou os dados já inseridos.
2. **Flags de Controle:** Uso de variáveis booleanas para gerenciar o encerramento das múltiplas camadas de repetição de forma elegante.
3. **Formatação de Strings:** Uso intensivo de `f-strings` com alinhadores (`^`, `>`, `<`) para garantir que o extrato no terminal e no arquivo ficasse organizado e profissional.


## 🔧 Como executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `.py`.
