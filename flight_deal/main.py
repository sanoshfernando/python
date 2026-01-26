
from utils import load_env, get_env, date_range_from_env
from data_store import CSVDataStore, Destination
from flight_search import FlightSearch
from notifier import ConsoleNotifier, EmailNotifier, TwilioNotifier
from typing import List, Optional

def pick_notifier():
    # Prefer email if fully configured, else Twilio, else console
    smtp_host = get_env("SMTP_HOST")
    smtp_port = get_env("SMTP_PORT", 587, int)
    smtp_user = get_env("SMTP_USER")
    smtp_pass = get_env("SMTP_PASSWORD")
    from_email = get_env("FROM_EMAIL")
    to_email   = get_env("TO_EMAIL")

    tw_sid  = get_env("TWILIO_SID")
    tw_tok  = get_env("TWILIO_AUTH_TOKEN")
    tw_from = get_env("TWILIO_FROM")
    tw_to   = get_env("TWILIO_TO")

    if smtp_host and smtp_user and smtp_pass and from_email and to_email:
        return EmailNotifier(smtp_host, smtp_port, smtp_user, smtp_pass, from_email, to_email)
    if tw_sid and tw_tok and tw_from and tw_to:
        try:
            return TwilioNotifier(tw_sid, tw_tok, tw_from, tw_to)
        except Exception:
            pass
    return ConsoleNotifier()

def update_missing_iata(destinations: List[Destination], fs: FlightSearch) -> List[Destination]:
    changed = False
    for d in destinations:
        if not d.iata_code:
            code = fs.get_iata_code(d.city)
            if code:
                d.iata_code = code
                changed = True
                print(f"Updated IATA for {d.city}: {code}")
            else:
                print(f"Warning: Could not find IATA for {d.city}")
    return destinations, changed

def main():
    load_env()

    api_key = get_env("TEQUILA_API_KEY")
    if not api_key:
        raise RuntimeError("Set TEQUILA_API_KEY in your environment or .env file.")

    origin = get_env("ORIGIN_IATA", "LON")
    currency = get_env("CURRENCY", "GBP")
    max_stopovers = get_env("MAX_STOPOVERS", 1, int)

    fs = FlightSearch(api_key=api_key, currency=currency, max_stopovers=max_stopovers)
    store = CSVDataStore("destinations.csv")
    notifier = pick_notifier()

    dests = store.load()
    if not dests:
        print("No destinations found in destinations.csv. Add some rows and try again.")
        return

    # Fill in any missing IATA codes
    dests, changed = update_missing_iata(dests, fs)
    if changed:
        store.save(dests)

    date_from, date_to = date_range_from_env()
    nights_min = get_env("NIGHTS_MIN", 3, int)
    nights_max = get_env("NIGHTS_MAX", 14, int)

    for d in dests:
        if not d.iata_code:
            print(f"Skipping {d.city}: missing IATA code")
            continue

        deal = fs.search_round_trip(
            origin_iata=origin,
            dest_iata=d.iata_code,
            date_from=date_from,
            date_to=date_to,
            nights_in_dst_from=nights_min,
            nights_in_dst_to=nights_max,
            max_price=d.lowest_price
        )

        if deal is None:
            print(f"No deal found for {d.city} under {d.lowest_price}.")
            continue

        subject = f"Flight deal to {d.city}: {deal.price} {deal.currency}"
        notifier.send(subject, deal.summary_text())

if __name__ == "__main__":
    main()
