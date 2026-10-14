import csv
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "raw"

# Display files
for file in DATA_DIR.iterdir():
    print(file.name)

# Define the CSV path
CSV_PATH = DATA_DIR / "backloggd-maxb059-2026-10-13.csv"

# Open the CSV file
with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        games = list(reader)
        print(reader.fieldnames)

        for index, row in enumerate(games, start = 1):
            print(index, row)


# Challenge 1 -- Count rated games
#   Count how many records have a nonempty "Rating" field

# Challenge 2 -- Counting backlog games
#   Count how many records have "In Backlog" set to "true"

# Challenge 3 -- Check for duplicate IDs
#   Determine whether any records share the same "ID"