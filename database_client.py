class DatabaseClient:
    """
    Simulated database client.
    """

    def __init__(self, batch_size):
        self.batch_size = batch_size

    def save(self, table, records):
        print(f"Saved {len(records)} records to {table}")
