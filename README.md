# Airbnb Ops — Dockerized Neighbourhood Summary Pipeline

Airbnb Ops is a small reproducible data pipeline that converts raw Airbnb listing data into a clean neighbourhood summary. It reads the raw CSV files, removes direct PII, creates aggregated neighbourhood metrics, validates the result, and saves the output as a CSV plus a Markdown report. The project is packaged as a Python CLI so the whole pipeline can run with one command. Docker makes the project portable by running it in the same environment everywhere, and DVC helps track the pipeline stages, inputs, and outputs so the workflow can be reproduced when the data or code changes.

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
