import pandas as pd

REQUIRED_OUTPUT_COLUMNS = [
    "neighbourhood",
    "num_listings",
    "avg_price",
    "median_price",
    "avg_minimum_nights",
    "availability_365_avg",
    "total_reviews",
    "reviews_per_listing",
    "tourism_segment",
    "priority_level",
]

PII_COLUMNS = [
    "host_name",
    "host_id",
]


def validate_summary(summary: pd.DataFrame) -> None:
    if summary.empty:
        raise ValueError("Summary output is empty")

    missing_columns = set(REQUIRED_OUTPUT_COLUMNS) - set(summary.columns)
    if missing_columns:
        raise ValueError(f"Missing required output columns: {missing_columns}")

    pii_columns_found = set(PII_COLUMNS) & set(summary.columns)
    if pii_columns_found:
        raise ValueError(f"PII columns found in output: {pii_columns_found}")

    if summary["neighbourhood"].isna().any():
        raise ValueError("neighbourhood contains null values")

    if (summary["num_listings"] <= 0).any():
        raise ValueError("num_listings must be greater than 0")

    if (summary["avg_price"] < 0).any():
        raise ValueError("avg_price must be greater than or equal to 0")

    if (~summary["availability_365_avg"].between(0, 365)).any():
        raise ValueError("availability_365_avg must be between 0 and 365")
    
