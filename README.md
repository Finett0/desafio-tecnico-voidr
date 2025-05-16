# Automação de Testes - Sauce Demo

Projeto de automação de testes para a aplicação web [Sauce Demo](https://www.saucedemo.com/) utilizando **Playwright** e **Python**, seguindo o padrão **Page Object Model (POM)**.

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

---

## Comandos para executar os testes
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
---



