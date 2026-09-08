# Playground

Runnable examples for the prompt engineering guide.

## Prerequisites

- Python 3.14 or newer
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
- An OpenAI API key

## Setup

From this directory, synchronize the project environment and dependencies:

```bash
uv sync
```

If you are creating this playground from scratch, initialize the project and add its dependencies with:

```bash
uv init
uv add openai pydantic
```

Create a `.env` file in the `playground` directory:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual key. Do not commit `.env` or share the key.

## Run the foundations example

Run the classification playground with the `.env` file loaded:

```bash
uv run --env-file .env 01-foundations/classify.py
```

The script loads the sample messages from `01-foundations/inputs.json` and sends each message to the classifier.
