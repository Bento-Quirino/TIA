# Análise Exploratória de Dados com Python

Para realizar uma análise exploratória de dados (EDA) completa no dataset escolhido, siga os passos descritos abaixo. A análise deve ser bem documentada e apresentar visualizações que ajudem a entender os dados. 

# ***A NOTA NÃO SERÁ COM BASE EM CÓDIGO, MAS SIM EM EXPLICAÇÕES DO GRUPO SOBRE O DATASET E RESPOSTAS AS PERGUNTAS DO PROFESSOR***

# Grupos e seus datasets
| Nome               | Dataset                                         | Observação                          | Target                     |
|--------------------|-------------------------------------------------|-------------------------------------|----------------------------|
| Pedro Meira        | [Titanic Dataset](https://www.kaggle.com/c/titanic/data) | Análise de sobrevivência por faixa etária, gênero e classe | Sobrevivência              |
| Haroldo Kimura     | [Planets](https://www.openml.org/d/462)         | Distribuição de tipos de planetas e suas características    | Tipo de planeta            |
| Mário Andrade      | [Penguins](https://allisonhorst.github.io/palmerpenguins/) | Comparação de espécies de pinguins por tamanho e peso     | Espécie                    |
| Lucas Xavier       | [20 News Group](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html) | Frequência de palavras por categoria de notícia | Categoria de notícia       |
| Gabriell Gonçalves | [Flights](https://www.kaggle.com/datasets/giovamata/airline-passenger-satisfaction) | Satisfação por tipo de serviço e frequência de voos       | Satisfação do passageiro   |
| Matheus Pereira    | [Exercícios](https://www.geeksforgeeks.org/seaborn-datasets-for-data-science/#7-exercise-dataset) | Comparação de atividades físicas por idade e frequência    | Tipo de exercício          |
| Alessandra Cristina       | [MPG Dataset](https://archive.ics.uci.edu/ml/datasets/auto+mpg) | Consumo médio de combustível por tipo de veículo          | Consumo de combustível (MPG) |
| Richard Vinicius   | [Housing Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) | Análise de preços por tamanho, localização e ano de construção | Preço do imóvel            |

[DATASETS E IMPORTAÇÕES](https://www.geeksforgeeks.org/seaborn-datasets-for-data-science/)

## Instruções

1. **Explicação do Dataset**
   - Explique de forma breve o que é o dataset, seu contexto e objetivo principal. Mencione o tema do dataset, por exemplo, se trata de sobrevivência em um naufrágio, satisfação de passageiros, entre outros.

2. **Colunas do Dataset**
   - Liste o nome de cada coluna do dataset e explique seu significado. Por exemplo, se a coluna é `age`, explique que se refere à idade dos indivíduos. Indique também se a coluna contém informações qualitativas (categóricas) ou quantitativas (numéricas).

3. **Tipos de Dados**
   - Classifique as colunas como variáveis qualitativas ou quantitativas. 

4. **Medidas Descritivas**
   - Calcule e apresente as seguintes medidas descritivas para as variáveis quantitativas do dataset:
     - Média
     - Menor valor (mínimo)
     - Maior valor (máximo)
     - Primeiro quartil (Q1)
     - Mediana (Q2)
     - Terceiro quartil (Q3)

5. **Correlação de Pearson**
   - Explique o conceito de correlação de Pearson: um valor que mede a força e a direção da relação linear entre duas variáveis quantitativas.
   - Utilize o dataset para calcular a matriz de correlação e plote um heatmap para visualizar as correlações entre variáveis numéricas. Explique quais relações apresentam uma correlação mais forte, se positiva ou negativa, e o que isso pode significar no contexto do dataset.

6. **Visualizações Gráficas**
   - Plote no mínimo **3 gráficos** para explorar o dataset.
   - As visualizações devem incluir:
     - Pelo menos **um gráfico** que utilize o *target* do dataset como uma das variáveis. Por exemplo, um gráfico de barras ou de pizza para mostrar a distribuição do target.
     - Pelo menos **um gráfico de dispersão** para observar a relação entre duas variáveis numéricas.
   - Exemplos de gráficos que você pode incluir:
     - **Histograma** para ver a distribuição de uma variável numérica
     - **Gráfico de barras** para comparar valores de diferentes categorias
     - **Gráfico de dispersão** (scatter plot) para observar correlações entre duas variáveis numéricas
     - **Boxplot** para visualizar a distribuição e identificar possíveis outliers em uma variável
     - **Heatmap** para a matriz de correlação (relacionado ao item 5)

## Resultados Esperados
- Um documento **bem estruturado** que contenha as análises e visualizações descritas acima.
- **Conclusões relevantes** sobre o dataset, com base nas visualizações e medidas descritivas apresentadas.
  
Certifique-se de documentar bem cada passo, explicando o que cada visualização representa e o que podemos interpretar a partir dela.
