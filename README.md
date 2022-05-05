# Bandit Simulator

Ask any question to Bandit (Bluey's Dad).

## Requirements
You'll need to install the OpenAI python library:

```
pip install --upgrade openai
```

## Setup
First generate the fine-tuned model:

```
openai api fine_tunes.create -t bandit.jsonl -m davinci --suffix "bandit"
```

Next, create a file called `config.txt`:

On the first line, paste your OpenAI API key.
On the second line, paste the fine tuned model name.

For example:
```
sk-123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM
davinci:ft-personal:bandit-2022-01-01-01-01-01
```

## Usage
```
python3 bandit.py "Where do babies come from?"
```
