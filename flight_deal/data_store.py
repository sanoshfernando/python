
from dataclasses import dataclass
from typing import List, Optional
import csv
import pathlib

@dataclass
class Destination:
    city: str
    iata_code: Optional[str]
    lowest_price: float

class CSVDataStore:
    def __init__(self, csv_path: str):
        self.csv_path = pathlib.Path(csv_path)

    def load(self) -> List[Destination]:
        if not self.csv_path.exists():
            return []
        rows: List[Destination] = []
        with self.csv_path.open(newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(Destination(
                    city=r.get("city", "").strip(),
                    iata_code=(r.get("iataCode") or "").strip() or None,
                    lowest_price=float(r.get("lowestPrice", 0) or 0),
                ))
        return rows

    def save(self, dests: List[Destination]):
        with self.csv_path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["city", "iataCode", "lowestPrice"])
            writer.writeheader()
            for d in dests:
                writer.writerow({"city": d.city, "iataCode": d.iata_code or "", "lowestPrice": d.lowest_price})
