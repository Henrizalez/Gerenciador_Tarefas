## Sistema Gerenciador de Tarefas - Python 🤩

Este repositório contém um sistema de gerenciamento de tarefas, desenvolvido em Python, que permite aos usuários:

* **Adicionar tarefas:** Criar novas tarefas com título, descrição, data de vencimento e prioridade. 😜
* **Listar tarefas:** Visualizar todas as tarefas adicionadas, organizadas por data de vencimento. 🗓️
* **Editar tarefas:** Modificar a descrição e a prioridade das tarefas. ✍️
* **Excluir tarefas:** Remover tarefas da lista. 🗑️
* **Exportar para Excel:** Exportar todas as tarefas para um arquivo Excel para visualização e organização. 📊

**Recursos:**

* **Validação de dados:** O sistema valida o formato da data de vencimento, garantindo que seja uma data válida e no futuro, e verifica se a prioridade é um valor válido ("baixa", "media" ou "alta"). 💪
* **Interface de usuário amigável:** O sistema apresenta um menu interativo para navegação pelas funcionalidades, e as informações são exibidas em uma tabela formatada para melhor legibilidade. ✨
* **Organização:** O código está estruturado em funções separadas para cada funcionalidade, tornando-o fácil de entender e manter. 🧠

**Softskills utilizadas:**

* **Pensamento crítico:** Para definir as funcionalidades do sistema e a melhor forma de implementá-las. 🤔
* **Criatividade:** Para encontrar soluções inovadoras para os desafios durante o desenvolvimento. 💡
* **Organização:** Para estruturar o código de forma eficiente e legível, facilitando a manutenção e a colaboração. 🗂️
* **Atenção aos detalhes:** Para garantir que o código funcione corretamente e atenda aos requisitos do sistema. 🔍
* **Comunicação:** Para escrever mensagens de erro claras e informativas para o usuário. 🗣️
* **Persistência:** Para superar os desafios durante o desenvolvimento e continuar trabalhando até alcançar o resultado desejado. 💪

**Instalação:**

Para executar o sistema, certifique-se de ter o Python instalado em seu sistema. Você também precisará instalar as seguintes bibliotecas:

* `openpyxl`
* `tabulate`

Você pode instalá-las usando o comando `pip`:

```bash
pip install openpyxl tabulate

Uso:
Execute o arquivo main.py (ou o nome do arquivo principal do seu projeto). O menu principal do sistema será apresentado. Selecione a opção desejada (1-6) digitando o número correspondente e pressionando Enter. Siga as instruções do sistema para adicionar, listar, editar, excluir ou exportar tarefas.
Exemplo de uso:
=-=-=-=-=-=--=-=-=-=-=-=-=-=-=
          Sistema Gerenciador de Tarefas
          =-=-=-=-=-=--=-=-=-=-=-=-=-=-=
          
          [1] Adicionar Tarefas
          [2] Listar Tarefas
          [3] Editar Tarefas
          [4] Excluir Tarefas
          [5] Exportar para excel
          [6] Sair
          
          Escolha uma opção: 1
          
          Qual tarefa? Fazer compras
          Qual a descrição da tarefa? Comprar leite, pão e ovos
          Qual a data máxima de realizar dessa tarefa? dd/mm/aaaa 20/10/2023
          Qual a prioridade dessa tarefa? (baixa, media, alta) alta
          Tarefa adicionada com sucesso! 😄
          
          =-=-=-=-=-=--=-=-=-=-=-=-=-=-=
          Sistema Gerenciador de Tarefas
          =-=-=-=-=-=--=-=-=-=-=-=-=-=-=
          
          [1] Adicionar Tarefas
          [2] Listar Tarefas
          [3] Editar Tarefas
          [4] Excluir Tarefas
          [5] Exportar para excel
          [6] Sair
          
          Escolha uma opção: 2

+-------+------------+-------------+------------+
| Índice | Vencimento | Tarefa       | Prioridade |
+-------+------------+-------------+------------+
|     0 | 20/10/2023 | Fazer compras | alta       |
+-------+------------+-------------+------------+

Contribuições para este projeto são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou entrar em contato comigo se você tiver alguma dúvida ou sugestão. 😊
