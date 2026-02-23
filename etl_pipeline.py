from datetime import datetime, timedelta, timezone


def remove_duplicates_by_id(records):
    seen = set()
    unique = []

    for record in records:
        record_id = record.get("id")
        if record_id not in seen:
            seen.add(record_id)
            unique.append(record)

    return unique


def run_pipeline(api_client, database, constants, logger):
    days_to_fetch = constants["days_to_fetch"]

    try:
        logger.info("Pipeline started")

        start_date = datetime.now(timezone.utc).date()

        for i in range(days_to_fetch):
            data_date = start_date + timedelta(days=i)

            logger.info(f"Fetching events for {data_date}")
            events = api_client.fetch_events_for_day(data_date)

            if not events:
                continue

            processed_events = api_client.process_events(events)
            processed_venues = api_client.process_venues(events)
            processed_performers = api_client.process_performers(events)

            processed_events = remove_duplicates_by_id(processed_events)
            processed_venues = remove_duplicates_by_id(processed_venues)
            processed_performers = remove_duplicates_by_id(processed_performers)

            database.save("events", processed_events)
            database.save("venues", processed_venues)
            database.save("performers", processed_performers)

            logger.info(f"Saved data for {data_date}")

        logger.info("Pipeline completed successfully")

    except Exception:
        logger.error("Pipeline failed", exc_info=True)
