# Event Data ETL Pipeline

## Overview
This project demonstrates a production-style ETL pipeline that ingests event data from an external API, processes nested entities, removes duplicates, and loads structured data into a database.

## Features
- Scheduled pipeline execution using cron
- Modular ETL architecture
- Data deduplication logic
- Batch data loading
- Structured logging
- Config-driven pipeline settings

## Tech Stack
- Python
- REST API Integration
- ETL Design Patterns
- Cron Scheduling
- YAML Configuration

## Architecture
API → Processing Layer → Deduplication → Database Storage

## How to Run

```bash
pip install -r requirements.txt
python main.py
