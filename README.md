# Teste Técnico Alura

## Sobre o Desafio

A AluMind é uma startup que oferece um aplicativo focado em bem-estar e saúde mental, proporcionando aos usuários acesso a meditações guiadas, sessões de terapia e conteúdos educativos sobre saúde mental. Com o alto crescimento da base de usuários, a AluMind está enfrentando dificuldades para analisar os feedbacks dos usuários em diferentes plataformas, como canais de atendimento ao cliente, comunidades no Discord e redes sociais. 

Neste desafio, você será responsável por criar uma aplicação que analise os feedbacks dos usuários, classifique-os com base no sentimento expresso e liste as possíveis melhorias sugeridas.

Veja mais sobre o desafio em: desafio.md
## Como executar 
### Pré-requisitos
Antes de começar, verifique se você tem os seguintes requisitos:

- Python (versão 3.10) instalado

- Para o funcionamento da aplicação é necessario uma chave para a API do GPT, ela deve ser definida em `GPT_API_KEY` no .env .
Como obter uma chave para a API do GPT: https://platform.openai.com/docs/api-reference/authentication
### Instalação
Clone o repositório do GitHub:

```bash
git clone https://github.com/ricardoadley/teste-tecnico-alura.git
cd teste-tecnico-alura
```
Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
```
Ative o ambiente virtual (Windows):

```bash
venv\Scripts\activate
```
Para sistemas não Windows (Linux/macOS):

```bash
source venv/bin/activate
```
### Instale as dependências:

```bash
pip install -r requirements.txt
```
### Executando o Projeto
Execute o aplicativo Flask:

```bash
python main.py
```

Abra seu navegador e vá para http://localhost:5000 para ver o swagger da aplicação em funcionamento.

## Observando o Funcionamento
É possivel testar as rotas pelo swagger da aplicação. Para visualização dos relatorios sobre os feedbacks é possivel visualizar as paginas HTML geras de forma mais agradavel pelas rotas http://localhost:5000/report para todos os feedbacks ou:
- Clicando em um id na pagina http://localhost:5000/report para o feedback espacifico
- Acessando http://localhost:5000/feedback/< id_feedback >

