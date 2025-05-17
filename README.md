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
source venv/Scripts/activate
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

## Documentos
A documentação está disponivel tanto em Markdown como em .docx caso queira fazer download, segue o link [Documentação do Projeto de Automação de Testes - Sauce Demo](/docs/documentacao.md) - contém detalhes sobre o desenvolvimento e implementação do projeto

---
### Demonstração dos Resultados

[O Video está no youtube porem está como não listado, para ver o video clique no link](https://www.youtube.com/watch?v=93YxwHye3Ps)




