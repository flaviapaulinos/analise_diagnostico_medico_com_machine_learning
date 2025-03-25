![Imagem](relatorios/imagens/pexels-cottonbro-5701676.jpg)
Foto de cottonbro studio: https://www.pexels.com/pt-br/foto/mulher-sem-rosto-luta-combate-5701676/

# Análise de Diagnóstico Médico com Machine Learning
(Medical Diagnosis Analysis with Machine Learning)

### 🔍 Visão Geral / Overview
PT: Comparação de modelos de classificação para diagnóstico benigno/maligno, com:

Seleção de features (Mutual Information)

Pré-processamento adaptativo (PowerTransformer para modelos lineais)

Otimização de hiperparâmetros

Análise comparativa (Regressão Logística vs XGBoost vs SVC)

EN: Classification model comparison for benign/malignant diagnosis featuring:

Feature selection (Mutual Information)

Adaptive preprocessing (PowerTransformer for linear models)

Hyperparameter tuning

Comparative analysis (Logistic Regression vs XGBoost vs SVC)

## Base de Dados/ Dataset

### Descrição
O câncer de mama é o tipo de câncer mais comum entre as mulheres no mundo, representando 25% de todos os casos de câncer. Em 2015, afetou mais de 2,1 milhões de pessoas. A doença começa quando as células da mama começam a crescer descontroladamente, formando tumores que podem ser detectados por meio de raio-X ou como nódulos na região da mama.

O principal desafio para sua detecção é classificar os tumores em **malignos** (cancerosos) ou **benignos** (não cancerosos). Este projeto utiliza o conjunto de dados Breast Cancer Wisconsin (Diagnostic) para realizar essa classificação.

### Características do Conjunto de Dados
- **Número de Instâncias:** 569 (malignas e benignas)
- 
- **Número de Atributos:** 30 (características extraídas de imagens digitalizadas de núcleos celulares)
- 
- **Atributos Incluem:** raio, textura, perímetro, área, suavidade, compactação, concavidade, pontos côncavos, simetria, dimensão fractal, etc.
- 
- **Variável Alvo:** Diagnóstico (Maligno = `M`, Benigno = `B`)

### Fonte dos Dados
O conjunto de dados foi obtido do [Kaggle](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset/data).

### Agradecimentos
Este conjunto de dados foi referenciado a partir do Kaggle. Originalmente, os dados foram criados pelo Dr. William H. Wolberg da Universidade de Wisconsin.

EN: 
### Description
Breast cancer is the most common cancer among women worldwide, accounting for 25% of all cancer cases. In 2015 alone, it affected over 2.1 million people. The disease begins when breast cells grow uncontrollably, forming tumors that can be detected via X-ray or as lumps in the breast area.

The key challenge lies in classifying tumors as either malignant (dangerous) or benign (harmless). This project uses the Breast Cancer Wisconsin dataset to perform this classification.

### Dataset Characteristics

Number of Instances: 569 (malignant and benign)

Number of Attributes: 30 (numeric features extracted from digitized cell nuclei images)

Attributes Include: radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, fractal dimension, etc.

Target Variable: Diagnosis (M = malignant, B = benign)

### Data Source

The dataset was obtained from Kaggle.

Acknowledgments

This dataset was referenced from Kaggle. Original data was created by Dr. William H. Wolberg (University of Wisconsin).

### 📈 Principais Resultados / Key Findings

### 🏆 Performance dos Modelos (F2-Score)

Modelo	          F2-Score	      Tempo (s)

XGBClassifier	    0.945	      0.598

LogisticRegression	0.937	      0.706

SVC	                0.922	     0.716

### 🔑 Features Mais Importantes

concave_points_mean (Odds Ratio: 41.79)

area_worst (Importância: 17.31)

radius_worst (SHAP value: 1.71)

### 💡 Insights Técnicos / Technical Insights

PT
Seleção de Features:

Redução de 30 para 15 features sem perda de performance

Métodos concordaram em 11 features críticas

Pré-processamento:

PowerTransformer essencial para modelos lineares

Árvores performaram melhor com dados originais

EN
Feature Selection:

Reduced from 30 to 15 features without performance loss

Methods agreed on 11 critical features

Preprocessing:

PowerTransformer critical for linear models

Trees performed better with raw data




Clique no botão **Use this template** para criar um novo repositório com base neste modelo.

## Organização do projeto

```

├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── requirements.txt   <- O arquivo para instalar dependências via pip
├── LICENSE            <- Licença de código aberto se uma for escolhida
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── modelos            <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
|
├── notebooks          <- Cadernos Jupyter. A convenção de nomenclatura é um número (para ordenação),
│                         as iniciais do criador e uma descrição curta separada por `-`, por exemplo
│                         `01-fb-exploracao-inicial-de-dados`.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── auxiliares.py<- Funções auxiliares do projeto
|      ├── config.py    <- Configurações básicas do projeto
|      ├── graficos.py  <- Scripts para criar visualizações exploratórias e orientadas a resultados
|      └── modelos.py   <- Funções utilizadas no modelo
|
├── referencias        <- Dicionários de dados.
|
├── relatorios         <- Análises geradas em HTML, PDF, LaTeX, etc.
│   └── imagens        <- Gráficos e figuras gerados para serem usados em relatórios
```

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone ENDERECO_DO_REPOSITORIO
    ```

Para mais informações sobre como usar Git e GitHub, [clique aqui](https://cienciaprogramada.com.br/2021/09/guia-definitivo-git-github/). Sobre ambientes virtuais, [clique aqui](https://cienciaprogramada.com.br/2020/08/ambiente-virtual-projeto-python/).


