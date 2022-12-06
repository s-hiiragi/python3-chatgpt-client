# A Tiny ChatGPT Client

## Requirements

- Python 3.10
- Poetry
- OpenAI Account

## How to use

1. Create An OpenAI key from [OpenAI's Website](https://beta.openai.com/account/api-keys).
2. Create `.env` file in the directory contains `config.py`.
3. Write `OPENAI_API_KEY=...` into `.env` file.
4. Enter Poetry Shell and run `main.py` as follows.

```console
poetry install
poetry shell
python main.py
> ask ENTER_ANY_PROMPT
> exit
```

## License

Apache-2.0

