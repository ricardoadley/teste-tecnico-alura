# Teste vaga de Python com foco em LLM

Nesta etapa, sua tarefa será realizar o protótipo de uma aplicação web para um cenário específico que imaginamos. É esperado que alguns requisitos possam gerar dúvidas. Recomendamos que você anote o que não ficou claro e explique por que tomou as decisões que tomou, considerando apenas o contexto deste desafio.

## Tecnologias que devem ser utilizadas

- Python (recomendamos 3.10+)
- Flask
- SQL (recomendamos MySQL ou PostgreSQL, mas fique à vontade para usar o que for mais confortável)
- LLMs
- Git & Github

### Tecnologias opcionais

- Langchain

## Avaliação

Durante o processo, iremos avaliar:

- Sua capacidade técnica com a linguagem e o framework
- Uso das LLMs
- Sua linha de pensamento ao desenvolver as funcionalidades pedidas
- Capacidade de derivar e entender requisitos
- Capacidade de organização:
  - Organização de código
  - Divisão de arquivos
  - Nomenclatura
  - Commits coesos
  - Organização do repositório (README)
- Comunicação

## Para a entrega

Para a entrega, seu desafio deverá estar em um repositório hospedado no Github. Recomendamos um repositório público, mas caso prefira criar privado, adicione as seguintes contas como colaboradores:

Seu repositório deverá conter um README explicando como executar o seu projeto. Fique à vontade para incluir informações que você achar pertinentes.

## Sobre o desafio

### Cenário

A AluMind é uma startup que oferece um aplicativo focado em bem-estar e saúde mental. Com o crescimento da base de usuários, surge a necessidade de analisar feedbacks de diversas plataformas.

#### 1. Classificação de Feedbacks

Neste desafio, você criará uma aplicação que receberá feedbacks dos usuários e os classificará com base no sentimento e nas funcionalidades sugeridas.

Exemplo de requisição:
```json
POST /feedbacks
Content-Type: application/json

{
  "id": "4042f20a-45f4-4647-8050-139ac16f610b",
  "feedback": "Gosto muito de usar o Alumind! Está me ajudando bastante em relação a alguns problemas que tenho. Só queria que houvesse uma forma mais fácil de eu mesmo realizar a edição do meu perfil dentro da minha conta"
}
```

Exemplo de resposta:
```json
{
  "id": "4042f20a-45f4-4647-8050-139ac16f610b",
  "sentiment": "POSITIVO",
  "requested_features": [
    {
      "code": "EDITAR_PERFIL",
      "reason": "O usuário gostaria de realizar a edição do próprio perfil"
    }
  ]
}
```

Cada feedback será classificado como "POSITIVO", "NEGATIVO" ou "INCONCLUSIVO" e poderá conter funcionalidades sugeridas.

#### 2. Relatório

Você deve criar uma página web que forneça um relatório simples do andamento de todos os feedbacks recebidos até o momento.

Alguns pontos que o relatório deve incluir:
- Porcentagem de feedbacks positivos em relação ao total
- Funcionalidades mais pedidas através dos feedbacks

#### 3. Resumo Semanal

Ao final de cada semana, um email deve ser enviado para stakeholders da AluMind com um resumo dos principais feedbacks da semana, incluindo percentagens de feedbacks positivos/negativos e principais funcionalidades solicitadas.

#### 4. Bônus (não obrigatório)

Implementação de um sistema de filtragem para garantir que apenas feedbacks legítimos e não classificados como spam sejam processados e armazenados.
