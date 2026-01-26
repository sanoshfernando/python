
import os
from datetime import date, timedelta
from dotenv import load_dotenv

def load_env():
    # Load .env if present; environment vars override .env values (safe default).
    load_dotenv(override=False)

def get_env(key: str, default=None, cast=str):
    value = os.getenv(key, None)
    if value is None:
        return default
    if cast is int:
        try:
            return int(value)
        except ValueError:
            return default
    if cast is float:
        try:
            return float(value)
        except ValueError:
            return default
    return value

def date_range_from_env():
    # Define search window from env values
    from_days = get_env("DATE_FROM_DAYS", 1, int)
    to_days   = get_env("DATE_TO_DAYS", 180, int)
    start = date.today() + timedelta(days=from_days)
    end   = date.today() + timedelta(days=to_days)
    # Tequila expects DD/MM/YYYY
    return start.strftime("%d/%m/%Y"), end.strftime("%d/%m/%Y")
