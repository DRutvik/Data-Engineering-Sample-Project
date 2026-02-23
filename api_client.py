import random


class EventAPIClient:
    """
    Mock API client to simulate fetching event data.
    """

    def __init__(self, base_url, logger):
        self.base_url = base_url
        self.logger = logger

    def fetch_events_for_day(self, date):
        # Simulated API response
        return [
            {
                "id": random.randint(1, 10000),
                "name": "Sample Event",
                "venue": {"id": random.randint(1, 1000), "name": "Sample Venue"},
                "performers": [
                    {"id": random.randint(1, 5000), "name": "Artist A"}
                ],
            }
            for _ in range(5)
        ]

    def process_events(self, events):
        return [{"id": e["id"], "name": e["name"]} for e in events]

    def process_venues(self, events):
        return [e["venue"] for e in events]

    def process_performers(self, events):
        performers = []
        for e in events:
            performers.extend(e["performers"])
        return performers
