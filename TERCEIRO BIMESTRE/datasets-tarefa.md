# Instruções de Trabalho - Análise Exploratória

## Grupos e Datasets

| Grupo  | Nome               | Dataset                                                                                           |
|--------|--------------------|---------------------------------------------------------------------------------------------------|
| 1      | Matheus Pereira     | [Iris Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset)      |
| 2      | Murilo Nascimento   | [Wine Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset) |
| 3      | Pedro Meira         | [Olivetti Faces Dataset](https://scikit-learn.org/stable/datasets/real_world.html#the-olivetti-faces-dataset) |
| 4      | Xavier              | [Tips Dataset](https://www.geeksforgeeks.org/seaborn-datasets-for-data-science/#1-tips-dataset)    |
| 5      | Cauan Guerra        | [LFW Dataset](https://scikit-learn.org/stable/datasets/real_world.html#the-labeled-faces-in-the-wild-face-recognition-dataset) |
| 6      | Alessandra          | [Linnerrud Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#linnerrud-dataset)   |
| 7      | Mário Andrade       | [Diabetes Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset)     |
| 8      | Haroldo Kimura      | [Breast Cancer Dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-wisconsin-diagnostic-dataset) |
| 9      | Cauan Bueno         | [20 Newsgroups Dataset](https://scikit-learn.org/stable/datasets/real_world.html#the-20-newsgroups-text-dataset) |

## Objetivo do Trabalho

Cada grupo será responsável por realizar uma **análise exploratória de dados** utilizando o Google Colab ou Jupyter Notebook. O objetivo é entender as características principais do dataset atribuído ao grupo, explorando as variáveis e as relações entre elas.

A análise deve conter:

1. **Descrição do Dataset**:
    - Introduza o dataset que está sendo analisado.
    - Descreva o que é o dataset e o que ele busca representar.
    - Explique quais tipos de dados ele contém de maneira clara e objetiva.
    - Exemplos de variáveis qualitativas e quantitativas dentro do seu dataset.
   
2. **Estrutura do Dataset**:
    - Exiba as primeiras linhas do dataset (`head()`).
    - Mostre o tamanho do dataset (número de linhas e colunas).
    - Liste as colunas e explique brevemente o que elas representam.

3. **Análise Estatística**:
    - Apresente um gráfico mostrando as médias de variáveis relevantes do dataset.
    - Exemplo: Para datasets com valores contínuos, calcule e visualize as médias de variáveis numéricas.

4. **Correlação de Pearson**:
    - Gere pelo menos dois **gráficos de dispersão** que mostrem a correlação de Pearson entre variáveis relevantes do seu dataset.
    - Interprete as correlações encontradas: Quais variáveis têm correlação forte? E fraca?
    - Explique o que é a correlação de pearson e como ela pode ser utilizada.

## Como entregar

- A análise deve ser apresentada em um **Jupyter Notebook** ou **Google Colab**.
- O notebook deve ser claro, com explicações textuais que acompanhem cada etapa do processo.
- Use bibliotecas como **Pandas**, **Seaborn** e **Matplotlib** para visualizações e análises.

## Critérios de Avaliação

- Clareza e completude das explicações sobre o dataset.
- Correta distinção entre dados qualitativos e quantitativos.
- Qualidade e clareza das visualizações.
- Interpretação correta das correlações de Pearson.

## AVISOS

- Explique o que é o target em seu dataset, e o que ele representa.
- Para os datasets que contenham imagens de rostos, utilize instâncias t4 GPU no google colab
- Para datasets com imagens de rostos, crie uma função que reconhece rostos utilziando a biblioteca face_rekogntion
