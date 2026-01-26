
# Flight Deal Finder (Clean Room Implementation)

A small, production-ready Python project that searches for cheap round-trip flights using the
**Tequila (Kiwi.com) API** and sends notifications (email/Twilio optional). This mirrors the *features*
of common "flight search / deal finder" exercises but is entirely original code written for you.

## Features
- Look up IATA codes for destination cities.
- Search round-trip flights from your origin to each destination across a date window.
- Set per-destination maximum prices and get alerts when deals are found.
- Store destinations in a CSV file (easy to edit) or wire up a Google Sheet via Sheety.
- Pluggable notification backends (email via SMTP, Twilio SMS, or console print).

## Requirements
- Python 3.10+
- A free **Tequila/Kiwi** API key: https://tequila.kiwi.com/portal/login
- (Optional) SMTP credentials for email or Twilio account for SMS

## Quick Start

1) Create and activate a virtual environment, then install deps:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2) Copy `.env.example` to `.env` and fill in your values:
```bash
cp .env.example .env
```

Set at least:
- `TEQUILA_API_KEY` (required)
- `ORIGIN_IATA` (e.g., LON, MAN, EDI)
- `CURRENCY` (e.g., GBP, EUR, USD)

Optional (for notifications):
- SMTP: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `FROM_EMAIL`, `TO_EMAIL`
- Twilio: `TWILIO_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_FROM`, `TWILIO_TO`

3) Edit `destinations.csv` with your target cities and max prices.

4) Run it:
```bash
python main.py
```

## Files
- `main.py` — coordinates the workflow
- `flight_search.py` — Tequila API client (IATA lookup + flight search)
- `flight_data.py` — dataclasses for search results
- `data_store.py` — CSV-based destinations store (can be replaced with Sheety later)
- `notifier.py` — email/Twilio/console notification backends
- `utils.py` — helpers (dates, env loading)
- `destinations.csv` — sample destinations
- `.env.example` — environment variable template

## Notes
- Tequila free tier has request limits; add small delays if you scale up.
- The search defaults are sensible (e.g., 1 stop max). Tweak them in `main.py` or `flight_search.py`.

Enjoy and customize!
