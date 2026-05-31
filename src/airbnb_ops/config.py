from dataclasses import dataclass
from pathlib import Path

@dataclass
class PipelineConfig:
    listings_path: Path = Path("data/raw/listings_sample.csv")
    segments_path: Path = Path("data/raw/neighbourhood_segments.csv")
    output_path: Path = Path("data/processed/neighbourhood_summary.csv")
    report_path: Path = Path("reports/neighbourhood_report.md")
