# Setup

## Pre-requisites

Very importantly for the setup you need to make sure you have poetry installed locally, to do that, just run:

```bash
poetry --version
```

If you got an error, above, then you need to download poetry. To download and install Poetry run:

```bash
make poetry-download
```

To uninstall poetry run:

```bash
make poetry-remove
```

Also, you would need to have an Open AI api key stored in your .env file 
as "OPENAI_API_KEY" and a Mistral API key "MISTRAL_API_KEY"

## Installation

To install most of the dependencies run:

```bash
make install
```

Besides that, you will need to run the following with pip:

```bash
pip install pypdf
pip install python-dotenv
pip install openai
pip install weaviate-client
pip install tiktoken
pip install pyupgrade
pip install isort
pip install black
pip install chromadb
pip install spacy
python -m spacy download de_core_news_sm
pip install langchainhub
```

## Running the app

### Precompute some stuff

```bash
python src/main.py
```

### Run the streamlit app

```bash
streamlit run src/api.py
```

If you encounter import issues when running the streamlit app, then you might need 
to run this from the terminal:

```bash
export PYTHONPATH=`pwd`
```


## Maintenance of the code quality / linting

For this, run:

```bash
make codestyle
```
