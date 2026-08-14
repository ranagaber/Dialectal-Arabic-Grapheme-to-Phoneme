# Dialectal Arabic Grapheme-to-Phoneme

A **country-level Dialectal Arabic Grapheme-to-Phoneme (G2P) model** that converts written dialectal Arabic text (graphemes) into its corresponding phoneme representation.

The model supports 15 country-level Arabic dialects: Egypt, Jordan, Syria, Lebanon, Palestine, Saudi Arabia, Qatar, Oman, Kuwait, Iraq, Yemen, Algeria, Libya, Tunisia, and Morocco. It was trained on the **CAPHI** phonological lexicon.

## API

The model is served through a **FastAPI** application.

Start the API with:

```bash
uv run uvicorn g2p.main:app --reload --app-dir src
```

Once the API is running, you can send requests using Python's `requests` library:

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/get_phoneme",
    json={
        "country_id": "Egypt",
        "text": "ازيك عامل ايه؟"
    }
)

print(response.json())
```

The API takes a country identifier and dialectal Arabic text, and returns the corresponding phoneme representation.

## Project Structure

```text
g2p/
├── src/
│   └── g2p/
│       ├── __init__.py
│       ├── main.py
│       └── app.py
├── pyproject.toml
└── uv.lock
```
## Evaluation

| Metric | Score |
|---|---:|
| **Word Accuracy** | 44.30% |
| **Edit Distance** | 1.3533 |
| **PER (Phoneme Error Rate)** | 16.35% |
