# Guará - Plataforma de Apoio às Vítimas das Enchentes no RS
![image](https://github.com/carlosrocha-dev/assistente_virtual_enchentes_rs/assets/3737837/175a88d9-d82a-4e77-93ee-e9e0e4458173)

**Introdução:**

Este assistente virtual, alimentado pela avançada tecnologia Gemini-Pro do Google, foi especialmente desenvolvido para oferecer suporte e informações cruciais a indivíduos afetados pelas recentes enchentes no Rio Grande do Sul e outros desastres naturais. Utilizando modelos de linguagem de ponta, ele é capaz de processar e fornecer respostas rápidas e precisas, ajudando a mitigar os riscos para aqueles em situações vulneráveis. Em momentos de crise, contar com informações confiáveis e acessíveis pode ser decisivo, e é nesse contexto que nosso assistente virtual se destaca, oferecendo uma ferramenta vital para a segurança e o bem-estar das pessoas afetadas.

**Como podemos ajudar:**

* **Orientações de preparação para emergências:** Fornecemos orientações sobre como se preparar para situações de emergência, incluindo a criação de um kit de emergência e a identificação de rotas de fuga.
* **Segurança durante enchentes:** Orientamos sobre o que fazer durante uma enchente para manter sua segurança, incluindo evacuar para terrenos mais altos e evitar linhas de energia caídas.
* **Gerenciamento de recuperação:** Auxiliamos no gerenciamento da recuperação após uma enchente, incluindo como solicitar assistência financeira, limpar sua casa e lidar com o trauma emocional.
* **Informações locais atualizadas:** Fornecemos informações atualizadas sobre as condições locais, incluindo níveis de água, avisos de evacuação e locais de abrigos temporários.
* **Acesso a recursos:** Conectamos você a recursos essenciais, como bancos de alimentos, serviços de saúde e apoio emocional.

**Como usar este serviço:**

* **Faça perguntas:** Digite suas perguntas ou preocupações na caixa de bate-papo abaixo.
* **Navegue pelos tópicos:** Explore os tópicos disponíveis no menu para encontrar informações específicas.
* **Obtenha suporte emocional:** Nossos assistentes virtuais estão disponíveis para fornecer apoio emocional e ouvir suas preocupações.
![image](https://github.com/carlosrocha-dev/assistente_virtual_enchentes_rs/assets/3737837/e59950c4-9f0b-4063-a677-447143cd45f0)
![image](https://github.com/carlosrocha-dev/assistente_virtual_enchentes_rs/assets/3737837/7ed5a07a-c22a-4f97-941f-9cf5b078bb57)

**Nosso compromisso:**

Estamos comprometidos em fornecer informações precisas e confiáveis para ajudá-lo a navegar por este período desafiador. Nosso objetivo é fornecer uma ferramenta acessível e útil para apoiá-lo em sua jornada de recuperação.


## Exemplos de perguntas que você pode fazer ao assistente virtual:

- Não consigo encontrar minha família, pode me ajudar?
- Onde posso encontrar abrigo temporário?
- Como posso obter informações sobre as condições locais?
- O que devo fazer para me preparar para uma enchente?
- Como posso acessar recursos como bancos de alimentos?
- O que devo fazer para manter minha segurança durante uma enchente?
- Como posso obter apoio emocional durante este período desafiador?
- O que devo fazer para me recuperar após uma enchente?
- Como posso ajudar outras pessoas afetadas pelas enchentes?


## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:
- Python 3.x
- Docker (opcional, para rodar com Docker)

## Configuração do Ambiente

### Configuração Local

1. **Clonar o Repositório**
   
```bash
git clone git@github.com:carlosrocha-dev/assistente_virtual_enchentes_rs.git
cd assistente_virtual_enchentes_rs
pip install -r requirements.txt
```

2. **Instalar Dependências**

Instale as dependências necessárias usando o pip:

```bash
pip install -r requirements.txt
```

3. **Configuração de Variáveis de Ambiente**

Crie um arquivo .env na raiz do seu projeto e adicione as seguintes variáveis:

```bash
GOOGLE_API_KEY=SuaChaveDeApiAqui
```


## Usando Docker
1. **Construir e Rodar com Docker Compose**

Utilize o Docker Compose para construir e rodar o container do seu projeto:

```bash
> docker-compose up --build
```


## Rodando o Projeto

### Sem Docker

Para iniciar o servidor Flask localmente sem Docker:

```bash
> flask run
```

Ou, alternativamente, você pode usar:

```bash
> python src/main.py
```

### Com Docker

Para iniciar o projeto usando Docker Compose, execute:

```bash
> docker-compose up
```

Acesse o aplicativo através de ```http://localhost:5000``` no navegador.

## Variáveis de Ambiente

O projeto usa as seguintes variáveis de ambiente:

GOOGLE_API_KEY: Chave de API para os serviços Google Generative AI.

Assegure-se de configurar essas variáveis no seu ambiente local ou de produção conforme necessário.
![image](https://github.com/carlosrocha-dev/assistente_virtual_enchentes_rs/assets/3737837/7223839b-b3aa-42cc-ab87-c3779190df31)
