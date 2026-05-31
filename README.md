# Airbnb Ops — Dockerized Neighbourhood Summary Pipeline

Airbnb Ops is a small, reproducible Python data pipeline for building a neighbourhood-level summary from sample Airbnb listing data.

The project demonstrates a basic MLOps/data-ops workflow:

- package code with a `src/` layout
- read raw CSV inputs
- remove direct PII and pseudonymize host identifiers
- transform listing-level data into neighbourhood-level metrics
- validate the final output
- expose the pipeline through a Typer CLI
- run the same workflow locally, with Docker, or with DVC

---

## What the pipeline does

The CLI command:

```bash
airbnb-ops run
```

runs the full pipeline:

```text
read raw data
    ↓
validate input file existence
    ↓
remove direct PII
    ↓
create stable host_key from host_id
    ↓
aggregate listings by neighbourhood
    ↓
join neighbourhood segment metadata
    ↓
validate final summary
    ↓
write CSV output and Markdown report
```

---

## Inputs

The project uses two raw CSV files.

### `data/raw/listings_sample.csv`

Listing-level Airbnb sample data.

Important columns include:

- `listing_id`
- `neighbourhood`
- `price`
- `minimum_nights`
- `availability_365`
- `number_of_reviews`
- `host_id`
- `host_name`

### `data/raw/neighbourhood_segments.csv`

Neighbourhood metadata used to enrich the summary.

Important columns include:

- `neighbourhood`
- `tourism_segment`
- `priority_level`

---

## Outputs

After running the pipeline, the project writes:

```text
data/processed/airbnb_neighbourhood_summary.csv
reports/hw01_a_run_report.md
```

The summary CSV contains one row per neighbourhood with these columns:

- `neighbourhood`
- `num_listings`
- `avg_price`
- `median_price`
- `avg_minimum_nights`
- `availability_365_avg`
- `total_reviews`
- `reviews_per_listing`
- `tourism_segment`
- `priority_level`

Direct PII fields such as `host_name` and `host_id` are not included in the final output.

---

## Installation

Create and activate a Python environment first.

Example with Conda:

```bash
conda create -n airbnb-ops python=3.11 -y
conda activate airbnb-ops
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

Install the package in editable mode:

```bash
pip install -e .
```

If your environment uses a custom PyPI mirror, for example `https://pypi.devneeds.ir/simple/`, you can run:

```bash
pip install -e . --no-build-isolation -i https://pypi.devneeds.ir/simple/ --trusted-host pypi.devneeds.ir
```

---
