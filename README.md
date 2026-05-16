# Projeto_Integrador_ADS_Grupo_38
# 📊 Desenvolvimento Low Code em Ciência de Dados
## Etapa 1 — Planejamento Inicial

---

## 📌 Tema do Projeto
Comportamento de Usuários no Spotify — Análise Low Code.


---

## 🗄️ Base de Dados
**Spotify User Behavior and Pattern — Kaggle**
- Link do dataset: https://www.kaggle.com/datasets/sahilislam007/spotify-user-behavior-and-pattern


---

## 👥 Integrantes do Grupo
- CAIO ALVES GOMES  
- LUIS FELIPE BATISTA HOLANDA  
- LUIZ GUSTAVO BARBOSA  
- LUCAS RIOS AYRES  
- LEANDRO SACOMANI FREDO  
- TAINA SILVA CONCEICAO  
- VITORIA SILVA DE LIMA  

---

## 🎯 Objetivo da Análise
O objetivo do projeto é analisar o comportamento de usuários do Spotify utilizando
ferramentas Low Code, avaliando métricas como engajamento (horas de escuta, skips,
playlists), tipos de assinatura, dispositivos utilizados, gêneros favoritos, inatividade e
conversão de anúncios.
A partir dos dados, será desenvolvido um dashboard interativo, que permitirá visualizar
padrões de uso, analisar retenção e apoiar decisões relacionadas à jornada do usuário.

---

## 🛠️ Planejamento das Tarefas  
### Organização e Dados
- **LEANDRO SACOMANI FREDO** — Criar e organizar o repositório no GitHub; adicionar
colaboradores; configurar `.gitignore`.

- **CAIO ALVES GOMES** — Estruturar o projeto (pastas `/data`, `/notebooks`, `/scripts`,
`/dashboard`) e inserir a base bruta do Kaggle.

### Qualidade, Transformações e EDA
- **LUIZ GUSTAVO BARBOSA** — Tratar nulos/duplicatas; padronizar tipos; normalizar
categorias como planos, dispositivos e gêneros.
- **LUCAS RIOS AYRES** — Criar transformações: coortes por `signup_date`, faixas de
engajamento, taxa de conversão de anúncios e indicadores de inatividade (`months_inactive`,
`inactive_3_months_flag`).
- **LUIS FELIPE BATISTA HOLANDA** — Realizar a EDA: estatísticas, gráficos exploratórios,
correlações e validação de consistência dos dados.
### Dashboard e Documentação
- **TAINA SILVA CONCEICAO** — Criar o dashboard Low Code (Power BI / Looker Studio);
montar KPIs e visualizações.
- **VITORIA SILVA DE LIMA** — Documentar todo o projeto; atualizar o README; descrever
transformações, decisões e evolução do dashboard.

---

## 📅 Cronograma de Execução
A divisão do projeto será feita em 4 fases principais, seguindo a ordem de tratamento dos dados.

### **Fase 1: Configuração e Infraestrutura (Início imediato)**
  Leandro e Caio: Disponibilizar o ambiente e estrutura de massas.

### **Fase 2: Pipeline de Dados (Tratamento e Engenharia)**
  Luiz Gustavo: Entregar a base limpa para o Lucas.\
  Lucas Rios: Aplicar as transformações complexas (coortes e bandeiras de inatividade).

### **Fase 3: Exploração e Inteligência (EDA)**
  Luis Felipe: Analisar a base transformada para encontrar padrões (Ex.: Por que os usuários ficam inativos?).

### **Fase 4: Visualização e Entrega Final**
  Tainá Silva: Desenvolvedora do dashboard final com base nos KPIs validados na fase anterior.\
  Vitória: Finalizar a documentação, descrevendo a evolução do dashboard e documentando cada fase anterior.

---

## 📊 Ideia Inicial do Dashboard  
A ideia inicial do dashboard é oferecer uma visão clara e estratégica do comportamento dos usuários na plataforma, combinando métricas de engajamento, conversão e preferências. A proposta é permitir que, de forma visual e intuitiva, seja possível identificar padrões de uso e compreender melhor como diferentes perfis de usuários interagem com o serviço.

### KPIs
- **Usuários ativos**
- **% de usuários inativos (3 meses)**
- **Horas médias de escuta por semana**
- **Taxa de conversão de anúncios** (ad_interaction → ad_conversion_to_subscription)
- **Distribuição de tipos de assinatura** (Free, Premium Individual, Duo, Family, Student)
### Visualizações Propostas
- **Barras**: Quantidade de usuários por tipo de assinatura e país.
- **Linha por coortes**: Análise temporal por `signup_date` (retenção simples).
- **Heatmap**: Dispositivo × taxa de conversão de anúncios.
- **Barras empilhadas**: Gêneros favoritos por plano.
- **Dispersão**: `avg_skips_per_day` × `avg_listening_hours_per_week`.
- **Funil**: `ad_interaction` → `ad_conversion_to_subscription`.

---


## 📁 Estrutura do Projeto e Configuração Inicial

O projeto foi estruturado para separar a camada de manipulação de dados (ETL) da camada de visualização (Dashboard):

1. **Base de Dados:** Download da base de dados do Spotify realizada através do Kaggle. O arquivo original foi renomeado para `spotify.csv` e armazenado na pasta `data/`.
2. **Dashboard:** Criação da pasta dedicada ao dashboard contendo o arquivo base do projeto (`app.py`).

---

## ⚙️ Processo de ETL (Extração, Transformação e Carga)

O processo de higienização e preparação dos dados foi documentado e executado em um arquivo Jupyter Notebook (`.ipynb`), ambiente ideal para a análise exploratória.

### Passos Realizados:
* **Exploração Inicial:** Verificação da estrutura do dataset, constatando o volume inicial de 5.000 linhas e 18 colunas.
* **Validação de Duplicatas:** Checagem de linhas duplicadas (nenhuma ocorrência encontrada).
* **Padronização Categórica:** Inspeção de consistência em strings (ex: checagem de grafias como *“Brazil, brazil ou brasil”*). Todas as categorias estavam devidamente padronizadas.
* **Análise Numérica:** Verificação das colunas de dados inteiros para garantir o equilíbrio da distribuição, confirmando a ausência de *outliers* ou anomalias drásticas de ocorrência.
* **Ajustes e Tipagem de Dados:**
  * Conversão da coluna de data de `string` para `datetime`.
  * Correção da coluna de inatividade (3 meses), que constava como `int`, mas documentada no Kaggle como valor booleano (`bool`).

Ao final do tratamento, a base limpa foi exportada para a pasta `data/` com o nome de `spotify_tratado.csv`. O repositório conta atualmente com as duas versões:
* `data/spotify.csv` (Base bruta)
* `data/spotify_tratado.csv` (Base tratada)

---

## 📊 Desenvolvimento do Dashboard & Streamlit

O arquivo `dashboard/app.py` foi configurado para consumir diretamente a base tratada.

### Validação Local
* Execução do Streamlit localmente com carregamento bem-sucedido de 50.000 linhas e 18 colunas (validação de nomes e integridade das colunas). Tudo rodando de forma fluida.
* **KPIs Principais:** Implementação e validação com sucesso dos indicadores de:
  * Total de Usuários
  * % de Assinantes Premium
  * % de Inativos (3 meses)
  * Média de Horas Semanais
  * Skips (Pulos de música) por dia
  * Taxa de Conversão de Anúncios

---

## 🛠️ Tratamento de Erros & Refatoração (Edge Cases)

Durante a evolução do layout, foram aplicadas correções importantes para prevenir quebras na interface (*Streamlit*):

* **Tratamento de Filtro Vazio:** Evita que o DataFrame filtrado (`df_filtrado`) fique inteiramente vazio (caso ocorram valores `NaN` em `subscription_type` ou combinações exclusivas do usuário), impedindo que os KPIs e gráficos quebrem com exibição de `NaN`.
* **Otimização do Gráfico de Idade:** Agrupamentos simples por idade (`groupby("age")`) geravam poluição visual com excesso de barras. O problema foi resolvido criando faixas etárias (*bins*).
* **Consistência em Selectboxes:** Correção de listas de filtros desalinhadas ou contendo opções nulas (`NaN`), garantindo exibição ordenada e limpa.

---

## 📈 Novas Funcionalidades & Histórico de Commits

### 🚀 Evolução e Visualizações Avançadas
Para enriquecer a experiência visual além dos 3 gráficos nativos e limitados do Streamlit, integramos a biblioteca **Plotly**, permitindo interações dinâmicas e análises visuais profundas.

* **Distribuição de Assinaturas:** Adicionado gráfico focado na divisão dos tipos de plano.
* **Filtro Lateral Dinâmico:** Implementação de filtro por tipo de assinatura integrado ao gráfico de idades.
* **Commit: Usuários por País** ✅
  * Adicionado gráfico de usuários por país com *slider* dinâmico baseado no contexto filtrado. O valor máximo do componente acompanha proporcionalmente a quantidade de países presentes no recorte atual.
* **Commit: Heatmap de Conversão por Dispositivo** ✅
  * Implementação de um gráfico de calor (*Heatmap*) via Plotly para analisar a conversão por tipo de dispositivo. A taxa de conversão é calculada com base na relação direta entre conversões e interações, exibida em formato percentual e com valores arredondados para facilitar a leitura dos insights.
