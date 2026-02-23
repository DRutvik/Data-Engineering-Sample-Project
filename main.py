import time
from datetime import datetime, timezone
from logging import Logger, StreamHandler, Formatter, DEBUG

from croniter import croniter

from utils.config_loader import ConfigLoader
from clients.api_client import EventAPIClient
from storage.database_client import DatabaseClient
from etl_pipeline import run_pipeline


# Load configuration
config = ConfigLoader("config.yaml")

constants = config.get("pipeline").get("constants")
schedule = config.get("pipeline").get("schedule")
api_url = config.get("pipeline").get("data_source").get("base_url")

# Logger setup
logger = Logger("ETL-Logger")
logger.setLevel(DEBUG)

handler = StreamHandler()
formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Initialize clients
api_client = EventAPIClient(api_url, logger)
database = DatabaseClient(constants.get("batch_size", 100))


def main():
    cron = croniter(schedule, datetime.now(timezone.utc))

    while True:
        next_run = cron.get_next(datetime)
        now = datetime.now(timezone.utc)
        sleep_time = (next_run - now).total_seconds()

        logger.info(f"Next run at {next_run}")
        time.sleep(sleep_time)

        run_pipeline(api_client, database, constants, logger)


if __name__ == "__main__":
    main()
