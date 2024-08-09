# Local Text Summarizer

## Overview

This project demonstrates how to run a Large Language Model (LLM) locally to perform text summarization using the Hugging Face `transformers` library. We use the `facebook/bart-large-cnn` model to efficiently summarize long texts.

## Features

- **Local Deployment**: Run the model on your local machine for enhanced data privacy and control.
- **Text Summarization**: Uses the `facebook/bart-large-cnn` model to generate concise summaries from long texts.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/local-text-summarizer.git
    cd local-text-summarizer
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Edit the `summarizer.py` file** to replace the placeholder text with the text you want to summarize.

2. **Run the summarizer**:

    ```bash
    python summarizer.py
    ```

3. **View the summary** in the output.

## Code

The code uses the Hugging Face `transformers` library to load a pre-trained BART model and tokenizer. It provides a class `TextSummarizer` with a method `summarize_text` to generate summaries. 

## Project Structure

