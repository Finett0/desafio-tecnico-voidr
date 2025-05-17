# Documentação do Projeto de Automação de Testes -- Sauce Demo

## 1. Introdução

Esse documento descreve o desenvolvimento e implementação dos testes automatizados na aplicação web [**Sauce Demo**](https://www.saucedemo.com/). Os testes foram desenvolvidos utilizando Playwright, Python e pytest.

## 2. Estrutura do Projeto

O projeto segue o padrão de design Page Object Model (POM) para organizar o código de forma que facilite a manutenção e ajude na escalabilidade.

## 3. Page Objects (Diretório pages/)

### 3.1. login_page.py

**Propósito:** Modelar a página de login da aplicação Sauce demo.

**Funções:**
- **goto** -- Navegar para a página de login
- **login** -- Preencher os campos de usuário e senha
- **get_error_message** - Capturar mensagem de erro

### 3.2. inventory_page.py

**Propósito:** Modelar a página de produtos da aplicação

**Funções:**
- **get_inventory_items_count** -- Conta o total de itens exibidos na pagina
- **add_item_to_cart** -- Adiciona um item específico ao carrinho com base em seu índice na lista
- **go_to_cart** -- Vai para página de compras ao clicar no ícone do carrinho
- **sort_products** -- Ordena os produtos na página de acordo com a opção selecionada no menu dropdown
- **get_product_names** -- Retorna uma lista com os nomes de todos os produtos exibidos na página

## 4. Arquivos de Teste (Diretório tests/)

### 4.1. authentication/test_login.py

**Propósito:** Testar todas as funcionalidades da página de login

**Testes Implementados:**
- **test_login_valid_user** -- Login com credenciais válidas
- **test_login_invalid_user** -- Login com credenciais inválidas
- **test_error_message_on_empty_login** -- Validação do campo de usuário vazio
- **test_error_message_on_empty_password** -- Validação do campo de senha vazio
- **test_login_locked_user** -- Login com usuário bloqueado

### 4.2. authentication/test_logout.py

**Propósito:** Testar a funcionalidade de logout

**Testes Implementados:**
- **test_logout_functionality** -- Verificação do processo completo de logout após login

### 4.3. cart/test_cart.py

**Propósito:** Testar as funcionalidades relacionadas ao carrinho de compras

**Testes implementados:**
- **test_cart_icon** -- Verificação da atualização do ícone do carrinho
- **test_add_item_to_cart** -- Adição de item no carrinho
- **test_correct_item** -- Verificação do item correto no carrinho
- **test_add_multiple_items_to_cart** -- Adição de múltiplos itens no carrinho
- **test_cart_remove_item** -- Remove item do carrinho

### 4.4. checkout/test_checkout.py

**Propósito:** Testar o processo de finalização de compra

**Testes implementados:**
- **test_checkout_process** -- Verificação do fluxo completo de checkout
- **test_checkout_required_fields** -- Validação de campos obrigatórios
- **test_checkout_success_message** -- Verificação da mensagem de sucesso após finalização

### 4.5. inventory/test_inventory.py

**Propósito:** Testar as funcionalidades da página de listagem de produtos

**Testes Implementados:**
- **test_inventory_items_count** -- Verifica a existência de produtos na pagina
- **test_sort_inventory_items** -- Ordenação de produtos por preço
- **test_sort_products_a_z** -- Ordenação de produtos de A-Z
- **test_sort_products_z_a** -- Ordenação de produtos Z-A

## 5. Arquivos de Configuração

### 5.1. conftest.py

**Propósito:** Definir configurações e fixtures para os testes

**Funções:**
- **setup** -- Fornecera fixture setup que é utilizada por todos os testes, e configurar o ambiente de teste (browser)

### 5.2. requirements.txt

**Propósito:** Listar todas as dependências para o projeto

### 5.3. README.md

**Propósito:** Fornecer instruções de configuração e execução dos testes

## 6. Considerações Finais

A estrutura do projeto segue boas práticas de automação de testes, sendo elas:

- **Page Object Model**
- **Organização de testes por funcionalidades**
- **Testes independentes**
- **Fixture reutilizável**

Com essa abordagem o projeto se torna escalável, permitindo adição de novos testes e manutenção dos existentes