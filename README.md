# Sentence Autocomplete Bot

`sentence-autocomplete-bot` is a machine learning-powered web application designed to autocomplete sentences. It utilizes the GPT-2 model from the Hugging Face `transformers` library to predict and complete sentences based on user input. This project is divided into two main components: the frontend, an HTML and Bootstrap-based interface for user interaction, and the backend, a Flask API for processing and predicting sentence completions.

This was built by Evan Chen and the Spring 2024 cohort of the Workshops committee of Northwestern's Responsible AI Student Organisation (RAISO).

## Features

- Completes sentences based on user input.
- Uses a pre-trained GPT-2 model for accurate and contextually relevant predictions.
- Simple and intuitive web interface built with Bootstrap for a modern look and feel.

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/sentence-autocomplete-bot.git
cd sentence-autocomplete-bot
```

### Step 2: Install dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Prepare models

Before running the application, you need to prepare the models. This involves loading datasets, tokenization, and preprocessing. Ensure that you have a prepare_models.py script to handle this. Run the script to prepare the models:

```bash
python prepare_models.py
```

### Step 4: Run the Application

Once the models are prepared, you can run the Flask application using the following command:

```bash
python3 app.py
```

### Step 5: Access the Application

Open a web browser and go to the URL address provided to use the sentence autocomplete bot.

## Usage

To use the sentence autocomplete bot, follow these steps:

1. Enter a partial sentence in the input box.
2. Click the "Complete Sentence" button to generate predictions.
3. View the predicted completions based on the input sentence.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.