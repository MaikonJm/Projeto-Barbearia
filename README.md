# Gestão Barbearia

Este projeto tem como objetivo fornecer uma solução para gerenciar os serviços prestados em uma barbearia, com funcionalidades de registro de serviços, visualização de histórico, relatórios de caixa por funcionário e controle de dados financeiros.

## Funcionalidades

- **Adicionar Serviço**: Permite o registro de serviços prestados pelos funcionários, incluindo seleção de funcionário e serviço.
- **Histórico de Lançamentos**: Exibe o histórico de serviços registrados, com paginação.
- **Zerar Histórico**: Permite a exclusão do histórico de lançamentos, se necessário.
- **Relatório de Caixa**: Exibe um relatório com o total de caixa por funcionário, cálculo da comissão e total de acerto.

## Tecnologias Utilizadas

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **Banco de Dados**: SQLite (ou outro banco conforme a configuração)
- **Bibliotecas**: 
  - jQuery para manipulação de DOM e requisições AJAX.

## Como Rodar o Projeto

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/gestao-barbearia.git
    ```

2. **Instale as dependências**:
    Caso não tenha as dependências instaladas, crie um ambiente virtual e instale-as:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate     # Para Windows
    pip install -r requirements.txt
    ```

3. **Configure o Banco de Dados**:
    Se estiver utilizando SQLite, o banco de dados será criado automaticamente na primeira execução. Caso utilize outro banco, ajuste as configurações no arquivo de conexão.

4. **Execute o servidor**:
    ```bash
    flask run
    ```

    O servidor estará disponível em `http://127.0.0.1:5000/`.

## Estrutura de Arquivos

- `app.py`: Arquivo principal do backend (Flask).
- `templates/`: Contém os arquivos HTML do frontend (como `index.html`, `relatorio.html`, etc.).
- `static/`: Contém arquivos estáticos, como CSS e JavaScript.
- `requirements.txt`: Arquivo com as dependências do projeto.

## Endpoints

- **GET /**: Página inicial com o formulário para adicionar serviços e o histórico.
- **POST /add**: Registra um novo serviço.
- **POST /reset-historico**: Zera o histórico de lançamentos.
- **GET /relatorio**: Exibe o relatório de caixa por funcionário.
  
## Contribuições

Contribuições são bem-vindas! Para colaborar com o projeto:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas modificações.
3. Envie um pull request detalhando as alterações realizadas.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [Seu Nome]([https://github.com/seu-usuario](https://github.com/MaikonJm))
