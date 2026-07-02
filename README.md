# ProjetoSistemaBancario
  Este projeto foi desenvolvido para a disciplina de Banco de Dados II com o objetivo de aplicar conceitos de integração entre Python e MySQL, utilizando transações e rollbakcs para garantir a consistência dos dados durante operações bancárias.
 
  O sistema simula um ambiente bancário simples, permitindo realizar consultas de saldo, depósitos, saques, transferências entre contas e testes de concorrência utilizando múltiplas threads.


## Tecnologias utilizadas

- Python 3
- MySQL 8
- MySQL Connector for Python
- Threading


## Funções
- Consultar saldo de uma conta
- Realizar depósitos
- Realizar saques
- Transferência de valores entre contas
- Teste de concorrência
- Uso de commit para melhor controle de transações
- Bloqueio de registros
- Tratamento de exceções

## Como executar

### 1. Execute o script SQL

Execute o arquivo:

```
sql/banco.sql
```

no MySQL Workbench.

### 2. Configure a conexão

No arquivo `src/db.py`, altere as informações de conexão conforme seu ambiente:

```python
host = "localhost"
user = "root"
password = "SUA_SENHA"
database = "sistema_projetofinalBD2"
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

### 4. Execute o sistema

```
python src/main.py
```


## Conceitos de Banco de Dados aplicados

- Integração entre Python e MySQL
- Transações
- COMMIT
- ROLLBACK
- Controle de concorrência
- Bloqueio de registros (`FOR UPDATE`)
- Atualização de dados
- Tratamento de exceções
- Threads em Python

Desenvolvido por **Cauã Maia Muniz de Alencar**.
