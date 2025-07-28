# Text classification with transformers
ML training template, especially for DL tasks.

## Setup

- if you want different framework like tensorflow, change the dockerfile in `docker-compose.yml`

```
docker compose up --build
```

- use notebook, open `http://localhost:8888/?token=12345`

## Pipeline

- synthetic data
- train
  - train deberta
  - train llama
- inference
  - vllm inference
  - batch inference
