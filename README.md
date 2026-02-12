📊 Dashboard BI – Business Intelligence com Python & Dash

Dashboard interativo de Business Intelligence desenvolvido em Python utilizando Dash, Plotly e PostgreSQL, focado em análise de vendas, indicadores financeiros e comparação de períodos.

O projeto demonstra domínio de:

Modelagem de dados

Consumo de banco de dados

Visualização interativa

Arquitetura modular

Indicadores de desempenho (KPIs)

Análise comparativa entre períodos

🚀 Funcionalidades

KPIs financeiros:

Total de Vendas

Quantidade de Produtos

Faturamento

Comparação automática com período anterior (%)

Filtros interativos:

Produto

Intervalo de datas

Gráficos:

Barras

Linha

Pizza

Atualização automática (refresh)

Layout responsivo

```text
Dasboard-BI/
│
├── app.py                  # Arquivo principal (start do projeto)
├── app_instance.py         # Instância do Dash
│
├── layouts/
│   ├── __init__.py
│   └── layout.py           # Layout da interface
│
├── callbacks/
│   ├── __init__.py
│   └── dashboard_callbacks.py
│
├── services/
│   └── kpi_service.py      # Cálculos de período e variação
│
├── utils/
│   ├── data_source.py      # Funções de acesso ao banco
│   └── db_connection.py   # Conexão com PostgreSQL
│
├── requirements.txt
└── README.md
```
🛠 Tecnologias Utilizadas

Python 3.13+

Dash

Dash Bootstrap Components

Plotly

Pandas

PostgreSQL

psycopg2 / SQLAlchemy

Instalação
1️⃣ Clonar repositório
```text
git clone https://github.com/seuusuario/Dashboard-BI.git
cd Dashboard-BI
```
2️⃣ Criar ambiente virtual (opcional)
```text
python -m venv venv
venv\Scripts\activate
```
3️⃣ Instalar dependências
```text
pip install -r requirements.txt
```
🗄 Configurar Banco de Dados

Crie um banco PostgreSQL e uma tabela exemplo:
```text
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    produto VARCHAR(100),
    categoria VARCHAR(100),
    quantidade INT,
    valor NUMERIC(10,2),
    data DATE
);
```

Configure a conexão em:
```text
utils/db_connection.py
```

Exemplo:
```text
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://usuario:senha@localhost:5432/dashboard_bi"
)
```
▶ Executar Projeto
```text
python app.py
```

Acesse no navegador:
```text
http://127.0.0.1:8050
```
📈 Como Funciona a Comparação de Períodos

Ao selecionar um intervalo de datas:

O sistema calcula automaticamente:

Período atual

Período anterior equivalente

Calcula variação percentual:
```text
((atual - anterior) / anterior) * 100
```

Exemplo de KPI:
```text
Faturamento: R$ 12.500,00 (+8.4%)
```
📤 Próximas Funcionalidades Planejadas

Exportação para Excel / CSV

Metas por indicador

Semáforo de desempenho (verde, amarelo, vermelho)

Drill-down (clique no gráfico para detalhar)

📷 Prints do Sistema

![Dashboard](screenshots/dashboard.png)

👨‍💻 Autor

Evair Siqueira
Graduando em Análise e Desenvolvimento de Sistemas
Desenvolvedor Web

📄 Licença

Este projeto é de uso educacional e para portfólio.
