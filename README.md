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

O projeto foi estruturado de forma modular para separar claramente a camada de manipulação de dados da camada de visualização:

1. **📂 data/**: Armazena as bases de dados utilizadas no projeto.
   * `spotify.csv`: Base de dados bruta baixada do Kaggle (massa de dados sintética).
   * `spotify_tratado.csv`: Base de dados após o processo de limpeza e higienização.
2. **📂 dashboard/**: Contém a estrutura do painel interativo.
   * `app.py`: Código base e visualizações desenvolvidas em Python utilizando a biblioteca Streamlit.

> 📊 **Planejamento Técnico:** Inicialmente planejado para plataformas *low-code* (Power BI / Looker Studio), o escopo evoluiu para o desenvolvimento de um painel dinâmico e customizado totalmente em **Streamlit (Python)**, centralizando a criação de KPIs e visualizações em código.

---

## ⚙️ Processo de ETL (Extração, Transformação e Carga)

A etapa de higienização, análise exploratória e preparação dos dados foi documentada e executada por meio de um arquivo Jupyter Notebook (`.ipynb`).

### 🔍 Etapas de Validação e Limpeza:
* **Exploração Inicial:** Verificação estrutural do dataset, que conta com **50.000 linhas e 18 colunas**.
* **Validação de Duplicatas:** Busca por registros duplicados na base (nenhuma ocorrência identificada).
* **Padronização Categórica:** Inspeção de consistência textual nas variáveis categóricas (como checar e corrigir grafias inconsistentes do tipo *“Brazil, brazil ou brasil”*). Todas as categorias encontravam-se devidamente padronizadas.
* **Análise Numérica:** Avaliação das colunas de dados inteiros para verificar o equilíbrio de distribuição das variáveis e mitigar a existência de *outliers* ou anomalias drásticas.
* **Transformação de Tipos de Dados:**
  * Conversão da coluna de data (que estava originalmente configurada como `string`) para o formato adequado de data e hora (`datetime`).
  * Ajuste da coluna indicativa de inatividade (3 meses): estava tipada como número inteiro (`int`), porém foi convertida para valor booleano (`bool`), em conformidade com as especificações do Kaggle.

---

## 📊 Desenvolvimento do Dashboard & Streamlit

O arquivo `dashboard/app.py` foi configurado para consumir de forma direta o arquivo final limpo (`data/spotify_tratado.csv`).

### 💻 Validação Local
O dashboard foi testado localmente carregando com sucesso a totalidade das 50.000 linhas e 18 colunas do dataset tratado. Todas as estruturas de dados foram lidas sem lentidão, rodando de forma fluida no Streamlit.

**Métricas e KPIs Principais Implementados:**
* 👥 Total de Usuários Únicos
* 💎 % de Assinantes do Plano Premium
* 💤 % de Usuários Inativos nos últimos 3 meses
* ⏳ Média de Horas de Uso Semanais
* ⏭️ Média de Skips (Pulos de música) por dia
* 📈 Taxa de Conversão de Anúncios

---

## 🛠️ Tratamento de Erros & Refatoração (Edge Cases)

Durante a evolução do projeto, implementamos tratativas para mitigar falhas de interface e garantir uma navegação robusta:

* **Tratamento de Filtro Vazio:** Adicionada uma lógica para prevenir cenários onde a aplicação de múltiplos filtros resulte em um DataFrame filtrado (`df_filtrado`) inteiramente vazio ou com valores `NaN`. Isso evita a exibição de erros na interface e mantém os KPIs íntegros.
* **Otimização do Gráfico de Idade:** O agrupamento direto por idade (`groupby("age")`) gerava poluição visual no layout devido ao excesso de barras. O problema foi solucionado com a categorização dos dados em faixas etárias específicas (*bins*).
* **Consistência em Filtros (Selectboxes):** Filtros laterais foram ajustados para remover valores nulos (`NaN`) e garantir listagens exibidas estritamente de forma ordenada.

---

## 📦 Dependências

Para que o ambiente funcione corretamente (tanto localmente quanto no servidor em nuvem), o arquivo `requirements.txt` deve estar localizado na raiz do repositório.

As principais bibliotecas utilizadas neste projeto são:
* `streamlit` (Interface gráfica e estrutura do web app)
* `pandas` (Manipulação, análise e tratamento de dados)
* `plotly` (Biblioteca integrada para estender as capacidades nativas do Streamlit com gráficos interativos)

---

## ▶️ Como Executar o Projeto Localmente

Caso queira clonar o repositório e executar a aplicação em sua máquina, siga os passos abaixo no terminal:

1. **Instale as dependências do projeto:**
   ```bash
   pip install -r requirements.txt

2. **Execute a aplicação do Streamlit:**
   ```bash
   streamlit run dashboard/app.py

---

## 📈 Histórico de Visualizações & Commits Principais

* **Distribuição de Assinaturas:** Gráfico focado no rateio volumétrico dos tipos de plano.
* **Filtro Lateral Dinâmico:** Integração do filtro de tipos de assinaturas interagindo diretamente com os dados de faixa etária.
* **Commit: Usuários por País** ✅
  * Inclusão do gráfico de distribuição geográfica com um componente de *slider* dinâmico. O valor máximo do seletor adapta-se automaticamente à quantidade de países presentes no recorte do filtro atual.
* **Commit: Heatmap de Conversão por Dispositivo** ✅
  * Gráfico de calor desenvolvido em Plotly relacionando interações e conversões por tipo de dispositivo, exibindo valores calculados em porcentagem e arredondados.
* **Commit: Funil de Conversão de Usuários** ✅
  * Implementação do fluxo de conversão (Total de Usuários → Interação → Conversão Final) com taxas de quebra calculadas dinamicamente com base nos filtros da página.
* **Commit: Evolução Temporal de Usuários** ✅
  * Gráfico de linha demonstrando a tendência de crescimento e novos cadastros ao longo do tempo.
* **Commit: Gêneros por Plano (Barras Empilhadas)** ✅
  * Criação do gráfico de barras empilhadas para análise de perfil demográfico por plano.
  * *Nota de Engenharia:* Foi observado que ao aplicar o filtro lateral para um plano específico, o gráfico limitava-se a exibir apenas uma coluna. Para manter a comparação contextual de mercado, planejou-se o uso do dataset completo para este componente ou a adoção de seleção múltipla no filtro.
* **Commit: Gráfico de Dispersão (Plotly)** ✅
  * Adição da última visualização analítica utilizando os eixos dinâmicos e *tooltips* interativos do Plotly.

---

## 🚀 Painel Concluído & Deploy

Com os testes locais validados com sucesso e a aplicação operando perfeitamente de ponta a ponta, realizamos a publicação oficial do sistema.

O projeto está disponível publicamente através da plataforma Streamlit Cloud e pode ser acessado pelo link abaixo:

🔗 **[Acesse o Dashboard Interativo do Spotify aqui](https://projetointegradoradsgrupo38.streamlit.app/)**
