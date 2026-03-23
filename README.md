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
