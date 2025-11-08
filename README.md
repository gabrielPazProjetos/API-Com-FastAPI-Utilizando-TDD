--- Store API
API RESTful desenvolvida com FastAPI, MongoDB, Pydantic e Pytest, com foco em TDD (Test-Driven Development). 

--- Objetivo
Desenvolver uma API funcional que permita:
Criar, listar, buscar, atualizar e deletar produtos
Aplicar filtros por faixa de preço
Validar dados com Pydantic
Testar funcionalidades com Pytest
Utilizar MongoDB como banco de dados
Aplicar TDD na prática

--- Tecnologias Utilizadas
FastAPI
MongoDB
Motor (driver assíncrono para MongoDB)
Pydantic
Pytest
Uvicorn (servidor ASGI)

--- Funcionalidades
POST /products → Criação de produto
GET /products → Listagem de todos os produtos
GET /products/{id} → Consulta de produto por ID
PUT /products/{id} → Atualização de produto
DELETE /products/{id} → Exclusão de produto
GET /products/filter?min_price=5000&max_price=8000 → Filtro por faixa de preço

--- Testes Automatizados
Os testes foram desenvolvidos com Pytest, cobrindo:
Criação de produto
Listagem
Filtros
Validação de dados
Tratamento de erros
