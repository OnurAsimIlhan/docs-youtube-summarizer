# LangChain Summarizer App

This Streamlit app utilizes LangChain to summarize content from YouTube videos or web pages. The application leverages the `ChatGroq` model for natural language processing to create concise summaries of the provided content.

![project demo photo](https://github.com/OnurAsimIlhan/docs-youtube-summarizer/blob/main/summarizer.png)

## Overview

This project demonstrates how to build a web-based summarization tool using:
- **Streamlit** for the web interface.
- **LangChain** for building NLP chains.
- **ChatGroq** for generating summaries.
- **Document loaders** such as `YoutubeLoader` and `UnstructuredURLLoader` to fetch data.

## Features

- Accepts a URL (either a YouTube link or a website).
- Uses `ChatGroq` to generate summaries of up to 300 words.
- Provides a user-friendly interface for interacting with the summarization model.
- Error handling and input validation included.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/OnurAsimIlhan/docs-youtube-summarizer.git
    cd docs-youtube-summarizer
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Enter your Groq API Key** in the sidebar of the app.

3. **Input the URL** of the YouTube video or website you want to summarize.

4. **Click the "Summarize the Content from YT or Website" button** to generate a summary.

