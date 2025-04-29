# Projeto de Testes Automatizados - Sistema de Cadastro de Clientes

Este projeto foi desenvolvido como parte do meu portfólio técnico para demonstrar habilidades em automação de testes, validações e boas práticas de QA. O sistema simula uma aplicação web de cadastro de clientes e cobre casos funcionais e de integração via API.

## Tecnologias Utilizadas
- Cypress
- JavaScript
- GitHub Actions
- HTML Reports

## Casos de Teste
- Cadastro com dados válidos
- Cadastro com CPF inválido
- Campos obrigatórios não preenchidos
- Teste de API: POST /clientes

## Como Executar
```bash
git clone https://github.com/seuusuario/projeto-teste-clientes
cd projeto-teste-clientes
npm install
npx cypress open
