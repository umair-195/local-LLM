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

- **`summarizer.py`**: Contains the main code for text summarization.
- **`requirements.txt`**: Lists the dependencies required for the project.

## Example Usage

Here’s how the summarizer performs on a real-world example:

**Original Text**:
You can refer to the blog post [here](https://edition.cnn.com/2024/08/09/sport/pakistan-olympics-javelin-arshad-nadeem-intl-hnk-spt/index.html).

**Summary**:
"
Arshad Nadeem wins Pakistan's first ever Olympic gold medal in the men's javelin throw. He threw a record 92.97 meters to win the gold medal. His brother says they will celebrate with rice pudding when he gets home."


