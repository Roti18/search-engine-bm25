## Simple Web Search Engine Implementation Using the BM25 Algorithm

This project aims to build a web-based search engine that can search and display the most relevant documents based on user input queries. To compute the relevance between documents and queries, the popular BM25 (Best Matching 25) algorithm is used in the field of Information Retrieval.

The project is developed using Python as the main language and Flask as the web framework. As a result, users can access the search system through a simple and intuitive web interface.

## Features

- A simple web interface for inputting search queries and displaying the results.
- Text preprocessing and relevance scoring using the BM25 algorithm.
- Ability to read documents from text files (.txt) or a local folder.
- Search results are presented in a structured and easy-to-read format.

## How It Works

```
- The user accesses the web page and enters a search query.
- The system performs preprocessing on both the query and the document corpus (tokenization, normalization, stopword removal).
- The BM25 algorithm calculates the relevance score of each document with respect to the query.
- The search results are displayed on the web page, sorted by the highest relevance score.

```

## Run Locally

Clone the project

```bash
  git clone https://github.com/Roti18/search-engine-bm25.git
```

Go to the project directory

```bash
  cd search-engine-bm25
```

Install environment

```bash
  python -m venv venv
```

Activate the environment

```bash
  .venv\Scripts\activate
```

Install Flask

```bash
  pip Install flask
```

Run Program

```bash
  python app.py
```

## Authors

- [@Zidan](https://www.github.com/zeedandp)
- [@Roni](https://www.github.com/Roti18)
