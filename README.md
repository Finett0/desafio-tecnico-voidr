# Automação de Testes - Sauce Demo

Projeto de automação de testes para a aplicação web [Sauce Demo](https://www.saucedemo.com/) utilizando **Playwright** e **Python**, seguindo o padrão **Page Object Model (POM)**.

##  Requisitos

- Python 3.8 ou superior  
- Playwright  
- Pytest  

---

##  Configuração do Ambiente

1. Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/desafio-tecnico-voidr.git
cd desafio-tecnico-voidr
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Instale os navegadores do Playwright:
```bash
playwright install
```

## Executando os Testes
```bash
pytest tests/
```
Para executar testes específicos:
```bash
# Testes de autenticação
pytest tests/authentication/

# Testes de inventário
pytest tests/inventory/

# Testes de carrinho
pytest tests/cart/

# Testes de checkout
pytest tests/checkout/
```
Executar o relatório detalhado:
```bash
pytest -v
```
## Testes implementados
Este projeto inclui 18 testes automatizados, cobrindo as principais funcionalidades da aplicação:

### Autenticação (6 testes)

- Login com credenciais válidas
- Login com credenciais inválidas
- Validação de mensagem de erro para username vazio
- Validação de mensagem de erro para password vazio
- Login com usuário bloqueado
- Funcionalidade de logout

### Inventário (4 testes)

- Verificação da contagem de itens no inventário
- Ordenação de produtos por preço (baixo para alto)
- Ordenação de produtos alfabeticamente (A-Z)
- Ordenação de produtos alfabeticamente (Z-A)

### Carrinho (5 testes)

- Verificação do ícone do carrinho
- Adicionar item ao carrinho
- Verificar item correto no carrinho
- Adicionar múltiplos itens ao carrinho
- Remover item do carrinho

# Checkout (3 testes)

- Processo completo de checkout
- Validação de campos obrigatórios
- Verificação de mensagem de sucesso


## Boas Práticas Implementadas
1. Isolamento de testes: Cada teste é independente e pode ser executado isoladamente
2. Organização por funcionalidade: Testes agrupados por funcionalidade da aplicação
3. Page Object Model: Separação clara entre lógica de teste e interação com a página
4. Seletores estáveis: Uso de seletores CSS robustos e atributos de data-test quando disponíveis
5. Asserções claras: Cada teste possui asserções específicas e significativas
6. Nomes descritivos: Nomes de métodos e variáveis auto-explicativos
7. Fixture scoped: Uso de fixture com escopo de função para garantir ambiente limpo para cada teste


