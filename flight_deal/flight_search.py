
from typing import Optional, Dict, Any, List
import requests
from flight_data import FlightDeal, FlightSegment

TEQUILA_BASE = "https://api.tequila.kiwi.com"

class FlightSearch:
    def __init__(self, api_key: str, currency: str = "GBP", max_stopovers: int = 1):
        self.session = requests.Session()
        self.session.headers.update({"apikey": api_key})
        self.currency = currency
        self.max_stopovers = max_stopovers

    def get_iata_code(self, city_name: str) -> Optional[str]:
        resp = self.session.get(
            f"{TEQUILA_BASE}/locations/query",
            params={"term": city_name, "location_types": "city", "limit": 1},
            timeout=20,
        )
        resp.raise_for_status()
        data = resp.json()
        if data.get("locations"):
            return data["locations"][0].get("code")
        return None

    def search_round_trip(self,
                          origin_iata: str,
                          dest_iata: str,
                          date_from: str,
                          date_to: str,
                          nights_in_dst_from: int,
                          nights_in_dst_to: int,
                          max_price: Optional[float] = None) -> Optional[FlightDeal]:
        """Search a round trip deal. Returns the cheapest deal within constraints, or None."""
        params = {
            "fly_from": origin_iata,
            "fly_to": dest_iata,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "flight_type": "round",
            "curr": self.currency,
            "max_stopovers": self.max_stopovers,
            "one_for_city": 1,  # deduplicate by city
            "limit": 1,         # we just need the best/cheapest
            "sort": "price",
        }
        if max_price is not None:
            params["price_to"] = max_price

        resp = self.session.get(f"{TEQUILA_BASE}/v2/search", params=params, timeout=30)
        resp.raise_for_status()
        payload = resp.json()
        data = payload.get("data", [])
        if not data:
            return None

        best = data[0]
        route_segments: List[FlightSegment] = []
        for seg in best.get("route", []):
            route_segments.append(FlightSegment(
                city_from=seg.get("cityFrom", ""),
                city_to=seg.get("cityTo", ""),
                fly_from=seg.get("flyFrom", ""),
                fly_to=seg.get("flyTo", ""),
                local_departure=seg.get("local_departure", ""),
                local_arrival=seg.get("local_arrival", ""),
                airline=seg.get("airline"),
            ))

        return FlightDeal(
            price=best.get("price", 0.0),
            currency=self.currency,
            nights_in_dest=best.get("nightsInDest", 0),
            route=route_segments,
            deep_link=best.get("deep_link", ""),
        )
