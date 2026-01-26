
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class FlightSegment:
    city_from: str
    city_to: str
    fly_from: str
    fly_to: str
    local_departure: str
    local_arrival: str
    airline: Optional[str] = None

@dataclass
class FlightDeal:
    price: float
    currency: str
    nights_in_dest: int
    route: List[FlightSegment]
    deep_link: str

    def summary_text(self) -> str:
        if not self.route:
            return f"Deal: {self.price} {self.currency} (no route details)"
        outward = self.route[0]
        inbound = self.route[-1]
        return (
            f"\n🔥 Flight deal found: {outward.city_from} ({outward.fly_from}) → "
            f"{outward.city_to} ({outward.fly_to}) for {self.price} {self.currency}\n"
            f"Out: {outward.local_departure} • Back: {inbound.local_departure}\n"
            f"Nights at destination: {self.nights_in_dest}\n"
            f"Book: {self.deep_link}\n"
        )
