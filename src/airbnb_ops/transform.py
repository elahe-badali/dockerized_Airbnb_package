import pandas as pd


REQUIRED_LISTING_COLUMNS = [
    "listing_id",
    "neighbourhood",
    "price",
    "minimum_nights",
    "availability_365",
    "number_of_reviews",
]

REQUIRED_SEGMENT_COLUMNS = [
    "neighbourhood",
    "tourism_segment",
    "priority_level",
]

OUTPUT_COLUMNS = [
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


def build_neighbourhood_summary(listings, segments):
    missing_listing_cols = set(REQUIRED_LISTING_COLUMNS) - set(listings.columns)
    if missing_listing_cols:
        raise ValueError(f"Missing listing columns: {missing_listing_cols}")

    missing_segment_cols = set(REQUIRED_SEGMENT_COLUMNS) - set(segments.columns)
    if missing_segment_cols:
        raise ValueError(f"Missing segment columns: {missing_segment_cols}")
    
    summary = listings.groupby("neighbourhood").agg(num_listings=("listing_id", "count"),
                                                    avg_price=("price", "mean"),
                                                    median_price=("price", "median"),
                                                    avg_minimum_nights=("minimum_nights", "mean"),
                                                    availability_365_avg=("availability_365", "mean"),
                                                    total_reviews=("number_of_reviews", "sum"),
                                                    ).reset_index()
    
    summary["reviews_per_listing"] =  (summary["total_reviews"] / summary["num_listings"])

    summary = summary.merge(
        segments,
        on="neighbourhood",
        how="left",
    )

    summary[["tourism_segment", "priority_level"]] = summary[
        ["tourism_segment", "priority_level"]
    ].fillna("unknown")

    return summary[OUTPUT_COLUMNS]
