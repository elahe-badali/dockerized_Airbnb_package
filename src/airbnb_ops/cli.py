from pathlib import Path

import typer

from airbnb_ops.config import PipelineConfig
from airbnb_ops.extract import read_csv_checked
from airbnb_ops.pii import handle_pii
from airbnb_ops.transform import build_neighbourhood_summary
from airbnb_ops.validate import validate_summary


app = typer.Typer()


@app.callback()
def main() -> None:
    pass


@app.command("run")
def run_pipeline() -> None:
    config = PipelineConfig(
        output_path=Path("data/processed/airbnb_neighbourhood_summary.csv"),
        report_path=Path("reports/hw01_a_run_report.md"),
    )

    listings = read_csv_checked(config.listings_path)
    segments = read_csv_checked(config.segments_path)

    safe_listings = handle_pii(listings)
    summary = build_neighbourhood_summary(safe_listings, segments)

    validate_summary(summary)

    config.output_path.parent.mkdir(parents=True, exist_ok=True)
    config.report_path.parent.mkdir(parents=True, exist_ok=True)

    summary.to_csv(config.output_path, index=False)

    report = f"""# Airbnb Ops Run Report

                ## Status

                Run completed successfully.

                ## Outputs

                - Summary CSV: `{config.output_path}`
                - Report: `{config.report_path}`

                ## Rows written

                {len(summary)}

                ## Columns

                {", ".join(summary.columns)}
                """

    config.report_path.write_text(report, encoding="utf-8")

    typer.echo(f"Wrote summary to {config.output_path}")
    typer.echo(f"Wrote report to {config.report_path}")


if __name__ == "__main__":
    app()
    
