#!/usr/bin/env python
import os
import csv
import argparse
import xlsxwriter
from ast import literal_eval


def csv_to_xlsx(file_in, file_out=None, force=False):
    # Generate output filename: splitext() returns tuple ( "file", "ext" )
    file_out = file_out or f"{os.path.splitext(file_in)[0]}.xlsx"
    if os.path.exists(file_out) and not force:
        raise Exception("Cannot overwrite existing .xlsx file; use --force to overwrite")

    # Create output workbook and sheet
    workbook = xlsxwriter.Workbook(file_out)
    worksheet = workbook.add_worksheet()

    # Parse CSV file
    with open(file_in, "r") as f:
        print(f"{file_in}")

        # Read some of the file to determine delimiter
        dialect = csv.Sniffer().sniff(f.read(1024))
        print(f"  > Detected delimiter={repr(dialect.delimiter)}")
        print(f"  > Detected line end={repr(dialect.lineterminator)}")
        f.seek(0)

        # Calculate total number of lines so we can give the user progress
        nb_lines = sum(1 for line in f)
        f.seek(0)

        # Parse CSV
        reader = csv.reader(f, dialect)
        for i, row in enumerate(reader):
            # Show progress
            line_nb = i + 1
            pct = int(line_nb / nb_lines * 100);
            if line_nb % 1000 == 0 or line_nb == nb_lines:
                print(f"\r  > Parsed {line_nb:,} / {nb_lines:,} rows - {pct}% done", end="")
            # Append row to worksheet
            worksheet.write_row(row=i, col=0, data=map(str_to_num, row))

    # Write XLSX file
    print(f"  > Writing to {file_out}")
    workbook.close()
    print(f"  > Done")


def str_to_num(str):
    try:
        return literal_eval(str)
    except Exception as _:
        return str


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV/TSV to convert to XLSX (e.g. input.csv)")
    parser.add_argument("--output", required=False, help="Where to output XLSX file (defaults to input.xlsx)")
    parser.add_argument("--force", required=False, action="store_true", help="Overwrite XLSX file if one exists already")
    args = parser.parse_args()
    csv_to_xlsx(
        file_in=args.input,
        file_out=args.output,
        force=args.force
    )


if __name__ == "__main__":
    cli()
