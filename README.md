
# Valheim User Reviews Analysis

This project aims to analyze user reviews about the game Valheim on Steam to understand why a game with such low quality graphics has a great reception from players.

## Problem Statement

The main question that this project wants to answer is:

- What are the main factors that influence the ratings and sentiments of user reviews about Valheim?

Some sub-questions that this project will explore are:

- How do the ratings and sentiments vary by region, playtime, genre preference, etc.?
- What are the most common topics and keywords that users mention in their reviews?
- How can we predict the rating or sentiment of a review based on its text?
- How can we cluster similar reviews or find outliers?

## Data Collection and Preparation

The data for this project consists of user reviews from Steam. The data was collected using public API. The data was stored in a file (potential DB). The data was cleaned, preprocessed, and feature engineered. Some of the steps involved in this process are:

- Remove stopwords, punctuation, and emojis
- Tokenize and lemmatize the text
- Extract sentiment, topic, and keywords from the reviews

## Data Exploration and Analysis

The data was explored and analyzed using descriptive and inferential statistics, visualizations, and hypothesis testing. Some of the methods and tools used in this process are:

- Compute histograms, boxplots, word clouds, etc. to see the distribution of ratings, sentiments, topics, etc.
- Test if there is a significant difference in ratings or sentiments between different groups of users using t-tests, ANOVA, chi-square tests, etc.

## Model Building and Evaluation

A suitable model was built and evaluated for the objective of the project. Some of the algorithms and techniques used in this process are:

- Regression or classification model to predict the rating or sentiment of a review based on its text
- Clustering or anomaly detection model to cluster similar reviews or find outliers
- Cross-validation or hold-out set to train and test the model
- Accuracy, precision, recall, F1-score, MSE, MAE, etc. to evaluate the model
- Grid search or random search to tune the model

## Results Communication and Presentation

The results were communicated and presented using a report or a dashboard that summarizes the findings and recommendations. Some of the features and elements used in this process are:

- Clear and concise language, charts, tables, etc. to communicate the results
- Main takeaways and implications of the analysis
- Suggestions for future work or improvements

## Tools and Libraries

Some of the tools and libraries used for this project are:

- Python
- API for reviews retrieval
- Pandas or numpy for data manipulation
- Scikit-learn or TensorFlow for machine learning
- Matplotlib or seaborn for visualization
- Jupyter notebook or Google Colab for coding
- GitHub or GitLab for version control


```mermaid
graph TB
  A[Start] --> B[Define question]
  B --> C[Collect data]
  C --> D[Prepare data]
  D --> E[Data Exploration]
  E --> F{Hypothesis Testing}
  F --> G[Model building and evaluation]
  G5 --> J[Summarize findings]
  C --public APIs --> L((Reviews Data))
  L -.-> C
  D --> |nltk| D1[Remove stopwords]
  D --> |re| D2[Remove punctuation and emojis]  
  D1 -->|nltk| D11[Tokenize the text]
  D2 --> |spacy| D12[Lemmatize the text]
  D11 --> |TextBlob| D111[Extract sentiment]
  D12 --> |LDA| D112[Extract topic]
  D111 --> |RAKE| D113[Extract keywords]
  E --> |matplotlib| E1[Compute histograms]
  E --> |seaborn| E2[Compute boxplots]
  E --> |wordcloud| E3[Compute word clouds]
  F --> |scipy| F1[t-tests]
  F --> |statsmodels| F2[ANOVA]
  F --> |scipy| F3[chi-square tests]
  G --> G1{Choose suitable model}
  G1 -->|scikit-learn| G11[Linear regression] 
  G11 -->|Test| G12[Cross-validation] 
  G31 -->|Test| G12[Cross-validation] 
  G1 -->|TensorFlow| G21[Logistic regression]
  G21 -->|Test| G22[hold-out set]
  G41 -->|Test| G22[hold-out set] 
  G1 -->|scikit-learn| G31[K-means]
  G1 -->|TensorFlow| G41[Isolation forest]
  G12 -->|scikit-learn| G121[Evaluate using MSE and MAE]
  G22 --> |TensorFlow| G221[Evaluate using accuracy and F1-score]
  G12 --> |scikit-learn| G321[Evaluate using silhouette score and inertia]
  G22 --> |TensorFlow| G421[Evaluate using accuracy and recall]
  G121 --> |grid search| G5[Tune model]
  G221 --> |random search| G5[Tune model]
  G321 --> |grid search| G5[Tune model]
  G421 --> |random search| G5[Tune model]
    ```
