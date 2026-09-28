"""
Export every table of the database to CSV files, one file per table.

Why this exists: exporting a result grid from MySQL Workbench wraps a value in
quotes but does not escape the quotes inside it. A value such as
    {"webdriver":0,"keys":932}
or a participant writing  "gut feeling"  is then split across several columns
when the CSV is read back. Python's csv module writes these correctly (the
inner quote becomes "" and the field is enclosed in quotes), so this script is
the supported way to get the data out.

Usage
    python export_csv.py                 # writes into ./export/
    python export_csv.py --out some/dir  # writes there instead

It connects to the same database as app.py: DATABASE_URL from the environment
if set, otherwise database_url from config.txt. To export the live Scalingo
database from your own machine, open a tunnel first (see README.md).

The files are named like the tables (pre_post_conf.csv, mem_task_data.csv, ...)
and hold every column in the model's order. NULL is written as an empty field.
"""
import argparse
import csv
import os
from pathlib import Path

from app import app, db
import models


TABLES = [
    models.PrePostConf,
    models.MemPreTutorialData,
    models.MemTutorialData,
    models.MemQuizTest,
    models.MemTaskData,
    models.PerTutorialData,
    models.PerQuizTest,
    models.PerTaskData,
    models.PsychQuiz,
    models.Feedback,
]


def export_table(model, out_dir):
    """Write one table to <out_dir>/<table name>.csv and return the row count."""
    columns = [c.name for c in model.__table__.columns]
    path = out_dir / f"{model.__tablename__}.csv"
    n = 0
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(columns)
        for row in db.session.query(model).order_by(model.id):
            writer.writerow(["" if getattr(row, c) is None else getattr(row, c) for c in columns])
            n += 1
    return n


def main():
    parser = argparse.ArgumentParser(description="Export every table to CSV, one file per table.")
    parser.add_argument("--out", default="export", help="output directory (default: ./export)")
    args = parser.parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    with app.app_context():
        for model in TABLES:
            n = export_table(model, out_dir)
            print(f"{model.__tablename__}.csv: {n} rows")
    print(f"Done. Files are in {out_dir.resolve()}")


if __name__ == "__main__":
    main()
